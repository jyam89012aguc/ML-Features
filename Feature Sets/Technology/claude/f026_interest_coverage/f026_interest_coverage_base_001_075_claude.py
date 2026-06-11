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
def _f026_cov_ebit(ebit, intexp):
    return ebit / intexp.replace(0, np.nan).abs()


# 21d mean of intcov_ebit scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebit_mean_21d_base_v001_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intcov_ebit scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebit_mean_63d_base_v002_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intcov_ebit scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebit_mean_126d_base_v003_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intcov_ebit scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebit_mean_252d_base_v004_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intcov_ebit scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebit_mean_504d_base_v005_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intcov_ebitda scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebitda_mean_21d_base_v006_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intcov_ebitda scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebitda_mean_63d_base_v007_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intcov_ebitda scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebitda_mean_126d_base_v008_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intcov_ebitda scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebitda_mean_252d_base_v009_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intcov_ebitda scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ebitda_mean_504d_base_v010_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intcov_ocf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ocf_mean_21d_base_v011_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intcov_ocf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ocf_mean_63d_base_v012_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intcov_ocf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ocf_mean_126d_base_v013_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intcov_ocf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ocf_mean_252d_base_v014_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intcov_ocf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_ocf_mean_504d_base_v015_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intcov_fcf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_fcf_mean_21d_base_v016_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intcov_fcf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_fcf_mean_63d_base_v017_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intcov_fcf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_fcf_mean_126d_base_v018_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intcov_fcf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_fcf_mean_252d_base_v019_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intcov_fcf scaled by closeadj
def f026ico_f026_interest_coverage_intcov_fcf_mean_504d_base_v020_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of int_to_debt scaled by closeadj
def f026ico_f026_interest_coverage_int_to_debt_mean_21d_base_v021_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of int_to_debt scaled by closeadj
def f026ico_f026_interest_coverage_int_to_debt_mean_63d_base_v022_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of int_to_debt scaled by closeadj
def f026ico_f026_interest_coverage_int_to_debt_mean_126d_base_v023_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of int_to_debt scaled by closeadj
def f026ico_f026_interest_coverage_int_to_debt_mean_252d_base_v024_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of int_to_debt scaled by closeadj
def f026ico_f026_interest_coverage_int_to_debt_mean_504d_base_v025_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of int_to_rev scaled by closeadj
def f026ico_f026_interest_coverage_int_to_rev_mean_21d_base_v026_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of int_to_rev scaled by closeadj
def f026ico_f026_interest_coverage_int_to_rev_mean_63d_base_v027_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of int_to_rev scaled by closeadj
def f026ico_f026_interest_coverage_int_to_rev_mean_126d_base_v028_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of int_to_rev scaled by closeadj
def f026ico_f026_interest_coverage_int_to_rev_mean_252d_base_v029_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of int_to_rev scaled by closeadj
def f026ico_f026_interest_coverage_int_to_rev_mean_504d_base_v030_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebit_minus_int scaled by closeadj
def f026ico_f026_interest_coverage_ebit_minus_int_mean_21d_base_v031_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebit_minus_int scaled by closeadj
def f026ico_f026_interest_coverage_ebit_minus_int_mean_63d_base_v032_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebit_minus_int scaled by closeadj
def f026ico_f026_interest_coverage_ebit_minus_int_mean_126d_base_v033_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebit_minus_int scaled by closeadj
def f026ico_f026_interest_coverage_ebit_minus_int_mean_252d_base_v034_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebit_minus_int scaled by closeadj
def f026ico_f026_interest_coverage_ebit_minus_int_mean_504d_base_v035_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_median_63d_base_v036_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_median_252d_base_v037_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_median_504d_base_v038_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_median_63d_base_v039_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_median_252d_base_v040_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_median_504d_base_v041_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_median_63d_base_v042_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_median_252d_base_v043_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_median_504d_base_v044_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_median_63d_base_v045_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_median_252d_base_v046_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_median_504d_base_v047_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_median_63d_base_v048_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_median_252d_base_v049_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_median_504d_base_v050_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_median_63d_base_v051_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_median_252d_base_v052_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_median_504d_base_v053_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_median_63d_base_v054_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_median_252d_base_v055_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_median_504d_base_v056_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_rmax_252d_base_v057_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_rmax_504d_base_v058_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_rmax_252d_base_v059_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_rmax_504d_base_v060_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_rmax_252d_base_v061_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_rmax_504d_base_v062_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_rmax_252d_base_v063_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_rmax_504d_base_v064_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_rmax_252d_base_v065_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_rmax_504d_base_v066_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_rmax_252d_base_v067_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_rmax_504d_base_v068_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_rmax_252d_base_v069_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_rmax_504d_base_v070_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_rmin_252d_base_v071_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_rmin_504d_base_v072_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_rmin_252d_base_v073_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_rmin_504d_base_v074_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_rmin_252d_base_v075_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

