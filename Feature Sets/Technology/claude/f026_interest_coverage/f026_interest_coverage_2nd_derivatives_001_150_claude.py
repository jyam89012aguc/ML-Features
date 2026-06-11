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


# 21d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slope_21d_2d_v001_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slope_63d_2d_v002_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slope_126d_2d_v003_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slope_252d_2d_v004_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_slope_504d_2d_v005_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slope_21d_2d_v006_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slope_63d_2d_v007_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slope_126d_2d_v008_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slope_252d_2d_v009_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_slope_504d_2d_v010_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slope_21d_2d_v011_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slope_63d_2d_v012_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slope_126d_2d_v013_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slope_252d_2d_v014_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_slope_504d_2d_v015_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slope_21d_2d_v016_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slope_63d_2d_v017_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slope_126d_2d_v018_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slope_252d_2d_v019_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_slope_504d_2d_v020_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slope_21d_2d_v021_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slope_63d_2d_v022_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slope_126d_2d_v023_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slope_252d_2d_v024_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_slope_504d_2d_v025_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slope_21d_2d_v026_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slope_63d_2d_v027_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slope_126d_2d_v028_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slope_252d_2d_v029_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_slope_504d_2d_v030_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slope_21d_2d_v031_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slope_63d_2d_v032_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slope_126d_2d_v033_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slope_252d_2d_v034_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_slope_504d_2d_v035_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sm21_sl21_2d_v036_signal(ebit, intexp, closeadj):
    base = _mean(_f026_cov_ebit(ebit, intexp), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sm63_sl21_2d_v037_signal(ebit, intexp, closeadj):
    base = _mean(_f026_cov_ebit(ebit, intexp), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sm63_sl63_2d_v038_signal(ebit, intexp, closeadj):
    base = _mean(_f026_cov_ebit(ebit, intexp), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sm252_sl63_2d_v039_signal(ebit, intexp, closeadj):
    base = _mean(_f026_cov_ebit(ebit, intexp), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sm252_sl126_2d_v040_signal(ebit, intexp, closeadj):
    base = _mean(_f026_cov_ebit(ebit, intexp), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sm21_sl21_2d_v041_signal(ebitda, intexp, closeadj):
    base = _mean(ebitda / intexp.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sm63_sl21_2d_v042_signal(ebitda, intexp, closeadj):
    base = _mean(ebitda / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sm63_sl63_2d_v043_signal(ebitda, intexp, closeadj):
    base = _mean(ebitda / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sm252_sl63_2d_v044_signal(ebitda, intexp, closeadj):
    base = _mean(ebitda / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sm252_sl126_2d_v045_signal(ebitda, intexp, closeadj):
    base = _mean(ebitda / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sm21_sl21_2d_v046_signal(ncfo, intexp, closeadj):
    base = _mean(ncfo / intexp.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sm63_sl21_2d_v047_signal(ncfo, intexp, closeadj):
    base = _mean(ncfo / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sm63_sl63_2d_v048_signal(ncfo, intexp, closeadj):
    base = _mean(ncfo / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sm252_sl63_2d_v049_signal(ncfo, intexp, closeadj):
    base = _mean(ncfo / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sm252_sl126_2d_v050_signal(ncfo, intexp, closeadj):
    base = _mean(ncfo / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sm21_sl21_2d_v051_signal(fcf, intexp, closeadj):
    base = _mean(fcf / intexp.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sm63_sl21_2d_v052_signal(fcf, intexp, closeadj):
    base = _mean(fcf / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sm63_sl63_2d_v053_signal(fcf, intexp, closeadj):
    base = _mean(fcf / intexp.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sm252_sl63_2d_v054_signal(fcf, intexp, closeadj):
    base = _mean(fcf / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sm252_sl126_2d_v055_signal(fcf, intexp, closeadj):
    base = _mean(fcf / intexp.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sm21_sl21_2d_v056_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sm63_sl21_2d_v057_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sm63_sl63_2d_v058_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sm252_sl63_2d_v059_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sm252_sl126_2d_v060_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sm21_sl21_2d_v061_signal(intexp, revenue, closeadj):
    base = _mean(intexp.abs() / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sm63_sl21_2d_v062_signal(intexp, revenue, closeadj):
    base = _mean(intexp.abs() / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sm63_sl63_2d_v063_signal(intexp, revenue, closeadj):
    base = _mean(intexp.abs() / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sm252_sl63_2d_v064_signal(intexp, revenue, closeadj):
    base = _mean(intexp.abs() / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sm252_sl126_2d_v065_signal(intexp, revenue, closeadj):
    base = _mean(intexp.abs() / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sm21_sl21_2d_v066_signal(ebit, intexp, closeadj):
    base = _mean(ebit - intexp.abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sm63_sl21_2d_v067_signal(ebit, intexp, closeadj):
    base = _mean(ebit - intexp.abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sm63_sl63_2d_v068_signal(ebit, intexp, closeadj):
    base = _mean(ebit - intexp.abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sm252_sl63_2d_v069_signal(ebit, intexp, closeadj):
    base = _mean(ebit - intexp.abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sm252_sl126_2d_v070_signal(ebit, intexp, closeadj):
    base = _mean(ebit - intexp.abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_pctslope_21d_2d_v071_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_pctslope_63d_2d_v072_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_pctslope_252d_2d_v073_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_pctslope_21d_2d_v074_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_pctslope_63d_2d_v075_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_pctslope_252d_2d_v076_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_pctslope_21d_2d_v077_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_pctslope_63d_2d_v078_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_pctslope_252d_2d_v079_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_pctslope_21d_2d_v080_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_pctslope_63d_2d_v081_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_pctslope_252d_2d_v082_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_pctslope_21d_2d_v083_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_pctslope_63d_2d_v084_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_pctslope_252d_2d_v085_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_pctslope_21d_2d_v086_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_pctslope_63d_2d_v087_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_pctslope_252d_2d_v088_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_pctslope_21d_2d_v089_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_pctslope_63d_2d_v090_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_pctslope_252d_2d_v091_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sgnslope_21d_2d_v092_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sgnslope_63d_2d_v093_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_sgnslope_252d_2d_v094_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sgnslope_21d_2d_v095_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sgnslope_63d_2d_v096_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_sgnslope_252d_2d_v097_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sgnslope_21d_2d_v098_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sgnslope_63d_2d_v099_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_sgnslope_252d_2d_v100_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sgnslope_21d_2d_v101_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sgnslope_63d_2d_v102_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_sgnslope_252d_2d_v103_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sgnslope_21d_2d_v104_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sgnslope_63d_2d_v105_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_sgnslope_252d_2d_v106_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sgnslope_21d_2d_v107_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sgnslope_63d_2d_v108_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_sgnslope_252d_2d_v109_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sgnslope_21d_2d_v110_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sgnslope_63d_2d_v111_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_sgnslope_252d_2d_v112_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_logmagslope_21d_2d_v113_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_logmagslope_63d_2d_v114_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_logmagslope_252d_2d_v115_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_logmagslope_21d_2d_v116_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_logmagslope_63d_2d_v117_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_logmagslope_252d_2d_v118_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_logmagslope_21d_2d_v119_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_logmagslope_63d_2d_v120_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_logmagslope_252d_2d_v121_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_logmagslope_21d_2d_v122_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_logmagslope_63d_2d_v123_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_logmagslope_252d_2d_v124_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_logmagslope_21d_2d_v125_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_logmagslope_63d_2d_v126_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_logmagslope_252d_2d_v127_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_logmagslope_21d_2d_v128_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_logmagslope_63d_2d_v129_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_logmagslope_252d_2d_v130_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_logmagslope_21d_2d_v131_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_logmagslope_63d_2d_v132_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_logmagslope_252d_2d_v133_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intcov_ebit|
def f026ico_f026_interest_coverage_intcov_ebit_logslope_63d_2d_v134_signal(ebit, intexp, closeadj):
    base = np.log((_f026_cov_ebit(ebit, intexp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intcov_ebit|
def f026ico_f026_interest_coverage_intcov_ebit_logslope_252d_2d_v135_signal(ebit, intexp, closeadj):
    base = np.log((_f026_cov_ebit(ebit, intexp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intcov_ebitda|
def f026ico_f026_interest_coverage_intcov_ebitda_logslope_63d_2d_v136_signal(ebitda, intexp, closeadj):
    base = np.log((ebitda / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intcov_ebitda|
def f026ico_f026_interest_coverage_intcov_ebitda_logslope_252d_2d_v137_signal(ebitda, intexp, closeadj):
    base = np.log((ebitda / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intcov_ocf|
def f026ico_f026_interest_coverage_intcov_ocf_logslope_63d_2d_v138_signal(ncfo, intexp, closeadj):
    base = np.log((ncfo / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intcov_ocf|
def f026ico_f026_interest_coverage_intcov_ocf_logslope_252d_2d_v139_signal(ncfo, intexp, closeadj):
    base = np.log((ncfo / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intcov_fcf|
def f026ico_f026_interest_coverage_intcov_fcf_logslope_63d_2d_v140_signal(fcf, intexp, closeadj):
    base = np.log((fcf / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intcov_fcf|
def f026ico_f026_interest_coverage_intcov_fcf_logslope_252d_2d_v141_signal(fcf, intexp, closeadj):
    base = np.log((fcf / intexp.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|int_to_debt|
def f026ico_f026_interest_coverage_int_to_debt_logslope_63d_2d_v142_signal(intexp, debt, closeadj):
    base = np.log((intexp.abs() / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|int_to_debt|
def f026ico_f026_interest_coverage_int_to_debt_logslope_252d_2d_v143_signal(intexp, debt, closeadj):
    base = np.log((intexp.abs() / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|int_to_rev|
def f026ico_f026_interest_coverage_int_to_rev_logslope_63d_2d_v144_signal(intexp, revenue, closeadj):
    base = np.log((intexp.abs() / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|int_to_rev|
def f026ico_f026_interest_coverage_int_to_rev_logslope_252d_2d_v145_signal(intexp, revenue, closeadj):
    base = np.log((intexp.abs() / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ebit_minus_int|
def f026ico_f026_interest_coverage_ebit_minus_int_logslope_63d_2d_v146_signal(ebit, intexp, closeadj):
    base = np.log((ebit - intexp.abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ebit_minus_int|
def f026ico_f026_interest_coverage_ebit_minus_int_logslope_252d_2d_v147_signal(ebit, intexp, closeadj):
    base = np.log((ebit - intexp.abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

