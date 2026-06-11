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
def _f015_int_to_ocf(intexp, ncfo):
    return intexp.abs() / ncfo.abs().replace(0, np.nan)


def _f015_tax_to_ocf(taxexp, ncfo):
    return taxexp.abs() / ncfo.abs().replace(0, np.nan)


def _f015_intcov(ebit, intexp):
    return ebit / intexp.replace(0, np.nan).abs()


# 21d mean of int_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_ocf_mean_21d_base_v001_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of int_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_ocf_mean_63d_base_v002_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of int_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_ocf_mean_126d_base_v003_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of int_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_ocf_mean_252d_base_v004_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of int_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_ocf_mean_504d_base_v005_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_mean_21d_base_v006_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_mean_63d_base_v007_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_mean_126d_base_v008_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_mean_252d_base_v009_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_to_ocf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_mean_504d_base_v010_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of int_to_debt scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_debt_mean_21d_base_v011_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of int_to_debt scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_debt_mean_63d_base_v012_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of int_to_debt scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_debt_mean_126d_base_v013_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of int_to_debt scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_debt_mean_252d_base_v014_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of int_to_debt scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_to_debt_mean_504d_base_v015_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tax_rate_local scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_rate_local_mean_21d_base_v016_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tax_rate_local scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_rate_local_mean_63d_base_v017_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tax_rate_local scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_rate_local_mean_126d_base_v018_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tax_rate_local scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_rate_local_mean_252d_base_v019_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tax_rate_local scaled by closeadj
def f015itd_f015_interest_and_tax_drag_tax_rate_local_mean_504d_base_v020_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drag_share_rev scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_rev_mean_21d_base_v021_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drag_share_rev scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_rev_mean_63d_base_v022_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drag_share_rev scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_rev_mean_126d_base_v023_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drag_share_rev scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_rev_mean_252d_base_v024_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drag_share_rev scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_rev_mean_504d_base_v025_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of drag_share_fcf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_mean_21d_base_v026_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of drag_share_fcf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_mean_63d_base_v027_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of drag_share_fcf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_mean_126d_base_v028_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of drag_share_fcf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_mean_252d_base_v029_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of drag_share_fcf scaled by closeadj
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_mean_504d_base_v030_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of int_tax_combo scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_tax_combo_mean_21d_base_v031_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of int_tax_combo scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_tax_combo_mean_63d_base_v032_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of int_tax_combo scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_tax_combo_mean_126d_base_v033_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of int_tax_combo scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_tax_combo_mean_252d_base_v034_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of int_tax_combo scaled by closeadj
def f015itd_f015_interest_and_tax_drag_int_tax_combo_mean_504d_base_v035_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_median_63d_base_v036_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_median_252d_base_v037_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_median_504d_base_v038_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_median_63d_base_v039_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_median_252d_base_v040_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_median_504d_base_v041_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_median_63d_base_v042_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_median_252d_base_v043_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_median_504d_base_v044_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_median_63d_base_v045_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_median_252d_base_v046_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_median_504d_base_v047_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_median_63d_base_v048_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_median_252d_base_v049_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_median_504d_base_v050_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_median_63d_base_v051_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_median_252d_base_v052_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_median_504d_base_v053_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_median_63d_base_v054_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_median_252d_base_v055_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_median_504d_base_v056_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rmax_252d_base_v057_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rmax_504d_base_v058_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rmax_252d_base_v059_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rmax_504d_base_v060_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_rmax_252d_base_v061_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_rmax_504d_base_v062_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_rmax_252d_base_v063_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_rmax_504d_base_v064_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_rmax_252d_base_v065_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_rmax_504d_base_v066_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_rmax_252d_base_v067_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_rmax_504d_base_v068_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_rmax_252d_base_v069_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_rmax_504d_base_v070_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rmin_252d_base_v071_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rmin_504d_base_v072_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rmin_252d_base_v073_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rmin_504d_base_v074_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_rmin_252d_base_v075_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

