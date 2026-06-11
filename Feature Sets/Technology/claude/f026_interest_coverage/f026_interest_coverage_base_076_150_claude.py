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


# 63d z-score of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_z_63d_base_v076_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_z_126d_base_v077_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_z_252d_base_v078_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_z_504d_base_v079_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_z_63d_base_v080_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_z_126d_base_v081_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_z_252d_base_v082_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_z_504d_base_v083_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_z_63d_base_v084_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_z_126d_base_v085_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_z_252d_base_v086_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_z_504d_base_v087_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_z_63d_base_v088_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_z_126d_base_v089_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_z_252d_base_v090_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_z_504d_base_v091_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_z_63d_base_v092_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_z_126d_base_v093_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_z_252d_base_v094_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_z_504d_base_v095_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_z_63d_base_v096_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_z_126d_base_v097_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_z_252d_base_v098_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_z_504d_base_v099_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_z_63d_base_v100_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_z_126d_base_v101_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_z_252d_base_v102_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_z_504d_base_v103_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_distmax_252d_base_v104_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_distmax_504d_base_v105_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_distmax_252d_base_v106_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_distmax_504d_base_v107_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_distmax_252d_base_v108_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_distmax_504d_base_v109_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_distmax_252d_base_v110_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_distmax_504d_base_v111_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_distmax_252d_base_v112_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_distmax_504d_base_v113_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_distmax_252d_base_v114_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_distmax_504d_base_v115_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_distmax_252d_base_v116_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_distmax_504d_base_v117_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_distmed_126d_base_v118_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_distmed_252d_base_v119_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_distmed_504d_base_v120_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_distmed_126d_base_v121_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_distmed_252d_base_v122_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_distmed_504d_base_v123_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_distmed_126d_base_v124_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_distmed_252d_base_v125_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_distmed_504d_base_v126_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_distmed_126d_base_v127_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_distmed_252d_base_v128_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_distmed_504d_base_v129_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_distmed_126d_base_v130_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_distmed_252d_base_v131_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_distmed_504d_base_v132_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_distmed_126d_base_v133_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_distmed_252d_base_v134_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_distmed_504d_base_v135_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_distmed_126d_base_v136_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_distmed_252d_base_v137_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebit_minus_int
def f026ico_f026_interest_coverage_ebit_minus_int_distmed_504d_base_v138_signal(ebit, intexp, closeadj):
    base = ebit - intexp.abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_chg_63d_base_v139_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intcov_ebit
def f026ico_f026_interest_coverage_intcov_ebit_chg_252d_base_v140_signal(ebit, intexp, closeadj):
    base = _f026_cov_ebit(ebit, intexp)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_chg_63d_base_v141_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intcov_ebitda
def f026ico_f026_interest_coverage_intcov_ebitda_chg_252d_base_v142_signal(ebitda, intexp, closeadj):
    base = ebitda / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_chg_63d_base_v143_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intcov_ocf
def f026ico_f026_interest_coverage_intcov_ocf_chg_252d_base_v144_signal(ncfo, intexp, closeadj):
    base = ncfo / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_chg_63d_base_v145_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intcov_fcf
def f026ico_f026_interest_coverage_intcov_fcf_chg_252d_base_v146_signal(fcf, intexp, closeadj):
    base = fcf / intexp.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_chg_63d_base_v147_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in int_to_debt
def f026ico_f026_interest_coverage_int_to_debt_chg_252d_base_v148_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_chg_63d_base_v149_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in int_to_rev
def f026ico_f026_interest_coverage_int_to_rev_chg_252d_base_v150_signal(intexp, revenue, closeadj):
    base = intexp.abs() / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

