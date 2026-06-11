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
def _f026_cov_ebit(ebit, intexp):
    return ebit / intexp.replace(0, np.nan).abs()


# 21d acceleration of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accel_21d_3d_v001_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accel_63d_3d_v002_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accel_126d_3d_v003_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accel_252d_3d_v004_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accel_21d_3d_v005_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accel_63d_3d_v006_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accel_126d_3d_v007_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accel_252d_3d_v008_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accel_21d_3d_v009_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accel_63d_3d_v010_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accel_126d_3d_v011_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accel_252d_3d_v012_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accel_21d_3d_v013_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accel_63d_3d_v014_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accel_126d_3d_v015_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accel_252d_3d_v016_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accel_21d_3d_v017_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accel_63d_3d_v018_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accel_126d_3d_v019_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accel_252d_3d_v020_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accel_21d_3d_v021_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accel_63d_3d_v022_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accel_126d_3d_v023_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accel_252d_3d_v024_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accel_21d_3d_v025_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accel_63d_3d_v026_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accel_126d_3d_v027_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accel_252d_3d_v028_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slopez_21d_z126_3d_v029_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slopez_63d_z252_3d_v030_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slopez_126d_z252_3d_v031_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slopez_252d_z504_3d_v032_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slopez_21d_z126_3d_v033_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slopez_63d_z252_3d_v034_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slopez_126d_z252_3d_v035_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slopez_252d_z504_3d_v036_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slopez_21d_z126_3d_v037_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slopez_63d_z252_3d_v038_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slopez_126d_z252_3d_v039_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slopez_252d_z504_3d_v040_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slopez_21d_z126_3d_v041_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slopez_63d_z252_3d_v042_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slopez_126d_z252_3d_v043_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slopez_252d_z504_3d_v044_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slopez_21d_z126_3d_v045_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slopez_63d_z252_3d_v046_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slopez_126d_z252_3d_v047_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slopez_252d_z504_3d_v048_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slopez_21d_z126_3d_v049_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slopez_63d_z252_3d_v050_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slopez_126d_z252_3d_v051_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slopez_252d_z504_3d_v052_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slopez_21d_z126_3d_v053_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slopez_63d_z252_3d_v054_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slopez_126d_z252_3d_v055_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slopez_252d_z504_3d_v056_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_jerk_21d_3d_v057_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_jerk_63d_3d_v058_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_jerk_126d_3d_v059_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_jerk_21d_3d_v060_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_jerk_63d_3d_v061_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_jerk_126d_3d_v062_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_jerk_21d_3d_v063_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_jerk_63d_3d_v064_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_jerk_126d_3d_v065_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_jerk_21d_3d_v066_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_jerk_63d_3d_v067_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_jerk_126d_3d_v068_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_jerk_21d_3d_v069_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_jerk_63d_3d_v070_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_jerk_126d_3d_v071_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_jerk_21d_3d_v072_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_jerk_63d_3d_v073_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_jerk_126d_3d_v074_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_jerk_21d_3d_v075_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_jerk_63d_3d_v076_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_jerk_126d_3d_v077_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intcov_ebit smoothed over 252d
def f026ico_f026_interest_coverage_intcov_ebit_smoothaccel_63d_sm252_3d_v078_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intcov_ebit smoothed over 504d
def f026ico_f026_interest_coverage_intcov_ebit_smoothaccel_252d_sm504_3d_v079_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intcov_ebitda smoothed over 252d
def f026ico_f026_interest_coverage_intcov_ebitda_smoothaccel_63d_sm252_3d_v080_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intcov_ebitda smoothed over 504d
def f026ico_f026_interest_coverage_intcov_ebitda_smoothaccel_252d_sm504_3d_v081_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intcov_ocf smoothed over 252d
def f026ico_f026_interest_coverage_intcov_ocf_smoothaccel_63d_sm252_3d_v082_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intcov_ocf smoothed over 504d
def f026ico_f026_interest_coverage_intcov_ocf_smoothaccel_252d_sm504_3d_v083_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intcov_fcf smoothed over 252d
def f026ico_f026_interest_coverage_intcov_fcf_smoothaccel_63d_sm252_3d_v084_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intcov_fcf smoothed over 504d
def f026ico_f026_interest_coverage_intcov_fcf_smoothaccel_252d_sm504_3d_v085_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of int_to_debt smoothed over 252d
def f026ico_f026_interest_coverage_int_to_debt_smoothaccel_63d_sm252_3d_v086_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of int_to_debt smoothed over 504d
def f026ico_f026_interest_coverage_int_to_debt_smoothaccel_252d_sm504_3d_v087_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of int_to_rev smoothed over 252d
def f026ico_f026_interest_coverage_int_to_rev_smoothaccel_63d_sm252_3d_v088_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of int_to_rev smoothed over 504d
def f026ico_f026_interest_coverage_int_to_rev_smoothaccel_252d_sm504_3d_v089_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebit_minus_int smoothed over 252d
def f026ico_f026_interest_coverage_ebit_minus_int_smoothaccel_63d_sm252_3d_v090_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebit_minus_int smoothed over 504d
def f026ico_f026_interest_coverage_ebit_minus_int_smoothaccel_252d_sm504_3d_v091_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accelz_21d_z252_3d_v092_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_accelz_63d_z504_3d_v093_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accelz_21d_z252_3d_v094_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_accelz_63d_z504_3d_v095_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accelz_21d_z252_3d_v096_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_accelz_63d_z504_3d_v097_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accelz_21d_z252_3d_v098_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_accelz_63d_z504_3d_v099_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accelz_21d_z252_3d_v100_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_accelz_63d_z504_3d_v101_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accelz_21d_z252_3d_v102_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_accelz_63d_z504_3d_v103_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accelz_21d_z252_3d_v104_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_accelz_63d_z504_3d_v105_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intcov_ebit (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ebit_signflip_63d_3d_v106_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intcov_ebit (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ebit_signflip_252d_3d_v107_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intcov_ebitda (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ebitda_signflip_63d_3d_v108_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intcov_ebitda (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ebitda_signflip_252d_3d_v109_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intcov_ocf (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ocf_signflip_63d_3d_v110_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intcov_ocf (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_ocf_signflip_252d_3d_v111_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intcov_fcf (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_fcf_signflip_63d_3d_v112_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intcov_fcf (raw count, no price scaling)
def f026ico_f026_interest_coverage_intcov_fcf_signflip_252d_3d_v113_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in int_to_debt (raw count, no price scaling)
def f026ico_f026_interest_coverage_int_to_debt_signflip_63d_3d_v114_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in int_to_debt (raw count, no price scaling)
def f026ico_f026_interest_coverage_int_to_debt_signflip_252d_3d_v115_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in int_to_rev (raw count, no price scaling)
def f026ico_f026_interest_coverage_int_to_rev_signflip_63d_3d_v116_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in int_to_rev (raw count, no price scaling)
def f026ico_f026_interest_coverage_int_to_rev_signflip_252d_3d_v117_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebit_minus_int (raw count, no price scaling)
def f026ico_f026_interest_coverage_ebit_minus_int_signflip_63d_3d_v118_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebit_minus_int (raw count, no price scaling)
def f026ico_f026_interest_coverage_ebit_minus_int_signflip_252d_3d_v119_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ebit normalized by 252d range
def f026ico_f026_interest_coverage_intcov_ebit_rngaccel_63d_r252_3d_v120_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ebit normalized by 504d range
def f026ico_f026_interest_coverage_intcov_ebit_rngaccel_252d_r504_3d_v121_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ebitda normalized by 252d range
def f026ico_f026_interest_coverage_intcov_ebitda_rngaccel_63d_r252_3d_v122_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ebitda normalized by 504d range
def f026ico_f026_interest_coverage_intcov_ebitda_rngaccel_252d_r504_3d_v123_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_ocf normalized by 252d range
def f026ico_f026_interest_coverage_intcov_ocf_rngaccel_63d_r252_3d_v124_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_ocf normalized by 504d range
def f026ico_f026_interest_coverage_intcov_ocf_rngaccel_252d_r504_3d_v125_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intcov_fcf normalized by 252d range
def f026ico_f026_interest_coverage_intcov_fcf_rngaccel_63d_r252_3d_v126_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intcov_fcf normalized by 504d range
def f026ico_f026_interest_coverage_intcov_fcf_rngaccel_252d_r504_3d_v127_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_debt normalized by 252d range
def f026ico_f026_interest_coverage_int_to_debt_rngaccel_63d_r252_3d_v128_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_debt normalized by 504d range
def f026ico_f026_interest_coverage_int_to_debt_rngaccel_252d_r504_3d_v129_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_rev normalized by 252d range
def f026ico_f026_interest_coverage_int_to_rev_rngaccel_63d_r252_3d_v130_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_rev normalized by 504d range
def f026ico_f026_interest_coverage_int_to_rev_rngaccel_252d_r504_3d_v131_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_minus_int normalized by 252d range
def f026ico_f026_interest_coverage_ebit_minus_int_rngaccel_63d_r252_3d_v132_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_minus_int normalized by 504d range
def f026ico_f026_interest_coverage_ebit_minus_int_rngaccel_252d_r504_3d_v133_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_cumslope_21d_3d_v134_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_cumslope_63d_3d_v135_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_cumslope_252d_3d_v136_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_cumslope_21d_3d_v137_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_cumslope_63d_3d_v138_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_cumslope_252d_3d_v139_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_cumslope_21d_3d_v140_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_cumslope_63d_3d_v141_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_cumslope_252d_3d_v142_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_cumslope_21d_3d_v143_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_cumslope_63d_3d_v144_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_cumslope_252d_3d_v145_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_cumslope_21d_3d_v146_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_cumslope_63d_3d_v147_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_cumslope_252d_3d_v148_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_cumslope_21d_3d_v149_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_cumslope_63d_3d_v150_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

