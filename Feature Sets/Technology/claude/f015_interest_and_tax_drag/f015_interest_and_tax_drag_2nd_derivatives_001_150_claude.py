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
def _f015_int_to_ocf(intexp, ncfo):
    return intexp.abs() / ncfo.abs().replace(0, np.nan)


def _f015_tax_to_ocf(taxexp, ncfo):
    return taxexp.abs() / ncfo.abs().replace(0, np.nan)


def _f015_intcov(ebit, intexp):
    return ebit / intexp.replace(0, np.nan).abs()


# 21d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slope_21d_2d_v001_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slope_63d_2d_v002_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slope_126d_2d_v003_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slope_252d_2d_v004_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slope_504d_2d_v005_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slope_21d_2d_v006_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slope_63d_2d_v007_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slope_126d_2d_v008_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slope_252d_2d_v009_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slope_504d_2d_v010_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slope_21d_2d_v011_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slope_63d_2d_v012_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slope_126d_2d_v013_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slope_252d_2d_v014_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slope_504d_2d_v015_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slope_21d_2d_v016_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slope_63d_2d_v017_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slope_126d_2d_v018_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slope_252d_2d_v019_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slope_504d_2d_v020_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slope_21d_2d_v021_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slope_63d_2d_v022_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slope_126d_2d_v023_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slope_252d_2d_v024_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slope_504d_2d_v025_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slope_21d_2d_v026_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slope_63d_2d_v027_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slope_126d_2d_v028_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slope_252d_2d_v029_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slope_504d_2d_v030_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slope_21d_2d_v031_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slope_63d_2d_v032_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slope_126d_2d_v033_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slope_252d_2d_v034_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slope_504d_2d_v035_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sm21_sl21_2d_v036_signal(intexp, ncfo, closeadj):
    base = _mean(_f015_int_to_ocf(intexp, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sm63_sl21_2d_v037_signal(intexp, ncfo, closeadj):
    base = _mean(_f015_int_to_ocf(intexp, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sm63_sl63_2d_v038_signal(intexp, ncfo, closeadj):
    base = _mean(_f015_int_to_ocf(intexp, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sm252_sl63_2d_v039_signal(intexp, ncfo, closeadj):
    base = _mean(_f015_int_to_ocf(intexp, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sm252_sl126_2d_v040_signal(intexp, ncfo, closeadj):
    base = _mean(_f015_int_to_ocf(intexp, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sm21_sl21_2d_v041_signal(taxexp, ncfo, closeadj):
    base = _mean(_f015_tax_to_ocf(taxexp, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sm63_sl21_2d_v042_signal(taxexp, ncfo, closeadj):
    base = _mean(_f015_tax_to_ocf(taxexp, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sm63_sl63_2d_v043_signal(taxexp, ncfo, closeadj):
    base = _mean(_f015_tax_to_ocf(taxexp, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sm252_sl63_2d_v044_signal(taxexp, ncfo, closeadj):
    base = _mean(_f015_tax_to_ocf(taxexp, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sm252_sl126_2d_v045_signal(taxexp, ncfo, closeadj):
    base = _mean(_f015_tax_to_ocf(taxexp, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sm21_sl21_2d_v046_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sm63_sl21_2d_v047_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sm63_sl63_2d_v048_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sm252_sl63_2d_v049_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sm252_sl126_2d_v050_signal(intexp, debt, closeadj):
    base = _mean(intexp.abs() / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sm21_sl21_2d_v051_signal(taxexp, ebt, closeadj):
    base = _mean(taxexp / ebt.replace(0, np.nan).abs() * 1.0, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sm63_sl21_2d_v052_signal(taxexp, ebt, closeadj):
    base = _mean(taxexp / ebt.replace(0, np.nan).abs() * 1.0, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sm63_sl63_2d_v053_signal(taxexp, ebt, closeadj):
    base = _mean(taxexp / ebt.replace(0, np.nan).abs() * 1.0, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sm252_sl63_2d_v054_signal(taxexp, ebt, closeadj):
    base = _mean(taxexp / ebt.replace(0, np.nan).abs() * 1.0, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sm252_sl126_2d_v055_signal(taxexp, ebt, closeadj):
    base = _mean(taxexp / ebt.replace(0, np.nan).abs() * 1.0, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sm21_sl21_2d_v056_signal(intexp, taxexp, revenue, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sm63_sl21_2d_v057_signal(intexp, taxexp, revenue, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sm63_sl63_2d_v058_signal(intexp, taxexp, revenue, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sm252_sl63_2d_v059_signal(intexp, taxexp, revenue, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sm252_sl126_2d_v060_signal(intexp, taxexp, revenue, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sm21_sl21_2d_v061_signal(intexp, taxexp, fcf, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sm63_sl21_2d_v062_signal(intexp, taxexp, fcf, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sm63_sl63_2d_v063_signal(intexp, taxexp, fcf, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sm252_sl63_2d_v064_signal(intexp, taxexp, fcf, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sm252_sl126_2d_v065_signal(intexp, taxexp, fcf, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sm21_sl21_2d_v066_signal(intexp, taxexp, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sm63_sl21_2d_v067_signal(intexp, taxexp, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sm63_sl63_2d_v068_signal(intexp, taxexp, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sm252_sl63_2d_v069_signal(intexp, taxexp, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sm252_sl126_2d_v070_signal(intexp, taxexp, closeadj):
    base = _mean((intexp.abs() + taxexp.abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_pctslope_21d_2d_v071_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_pctslope_63d_2d_v072_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_pctslope_252d_2d_v073_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_pctslope_21d_2d_v074_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_pctslope_63d_2d_v075_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_pctslope_252d_2d_v076_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_pctslope_21d_2d_v077_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_pctslope_63d_2d_v078_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_pctslope_252d_2d_v079_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_pctslope_21d_2d_v080_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_pctslope_63d_2d_v081_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_pctslope_252d_2d_v082_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_pctslope_21d_2d_v083_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_pctslope_63d_2d_v084_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_pctslope_252d_2d_v085_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_pctslope_21d_2d_v086_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_pctslope_63d_2d_v087_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_pctslope_252d_2d_v088_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_pctslope_21d_2d_v089_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_pctslope_63d_2d_v090_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_pctslope_252d_2d_v091_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sgnslope_21d_2d_v092_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sgnslope_63d_2d_v093_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_sgnslope_252d_2d_v094_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sgnslope_21d_2d_v095_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sgnslope_63d_2d_v096_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_sgnslope_252d_2d_v097_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sgnslope_21d_2d_v098_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sgnslope_63d_2d_v099_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_sgnslope_252d_2d_v100_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sgnslope_21d_2d_v101_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sgnslope_63d_2d_v102_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_sgnslope_252d_2d_v103_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sgnslope_21d_2d_v104_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sgnslope_63d_2d_v105_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_sgnslope_252d_2d_v106_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sgnslope_21d_2d_v107_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sgnslope_63d_2d_v108_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_sgnslope_252d_2d_v109_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sgnslope_21d_2d_v110_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sgnslope_63d_2d_v111_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_sgnslope_252d_2d_v112_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_logmagslope_21d_2d_v113_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_logmagslope_63d_2d_v114_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_logmagslope_252d_2d_v115_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_logmagslope_21d_2d_v116_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_logmagslope_63d_2d_v117_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_logmagslope_252d_2d_v118_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_logmagslope_21d_2d_v119_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_logmagslope_63d_2d_v120_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_logmagslope_252d_2d_v121_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_logmagslope_21d_2d_v122_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_logmagslope_63d_2d_v123_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_logmagslope_252d_2d_v124_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_logmagslope_21d_2d_v125_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_logmagslope_63d_2d_v126_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_logmagslope_252d_2d_v127_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_logmagslope_21d_2d_v128_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_logmagslope_63d_2d_v129_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_logmagslope_252d_2d_v130_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_logmagslope_21d_2d_v131_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_logmagslope_63d_2d_v132_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_logmagslope_252d_2d_v133_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|int_to_ocf|
def f015itd_f015_interest_and_tax_drag_int_to_ocf_logslope_63d_2d_v134_signal(intexp, ncfo, closeadj):
    base = np.log((_f015_int_to_ocf(intexp, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|int_to_ocf|
def f015itd_f015_interest_and_tax_drag_int_to_ocf_logslope_252d_2d_v135_signal(intexp, ncfo, closeadj):
    base = np.log((_f015_int_to_ocf(intexp, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_to_ocf|
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_logslope_63d_2d_v136_signal(taxexp, ncfo, closeadj):
    base = np.log((_f015_tax_to_ocf(taxexp, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_to_ocf|
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_logslope_252d_2d_v137_signal(taxexp, ncfo, closeadj):
    base = np.log((_f015_tax_to_ocf(taxexp, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|int_to_debt|
def f015itd_f015_interest_and_tax_drag_int_to_debt_logslope_63d_2d_v138_signal(intexp, debt, closeadj):
    base = np.log((intexp.abs() / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|int_to_debt|
def f015itd_f015_interest_and_tax_drag_int_to_debt_logslope_252d_2d_v139_signal(intexp, debt, closeadj):
    base = np.log((intexp.abs() / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_rate_local|
def f015itd_f015_interest_and_tax_drag_tax_rate_local_logslope_63d_2d_v140_signal(taxexp, ebt, closeadj):
    base = np.log((taxexp / ebt.replace(0, np.nan).abs() * 1.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_rate_local|
def f015itd_f015_interest_and_tax_drag_tax_rate_local_logslope_252d_2d_v141_signal(taxexp, ebt, closeadj):
    base = np.log((taxexp / ebt.replace(0, np.nan).abs() * 1.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drag_share_rev|
def f015itd_f015_interest_and_tax_drag_drag_share_rev_logslope_63d_2d_v142_signal(intexp, taxexp, revenue, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drag_share_rev|
def f015itd_f015_interest_and_tax_drag_drag_share_rev_logslope_252d_2d_v143_signal(intexp, taxexp, revenue, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|drag_share_fcf|
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_logslope_63d_2d_v144_signal(intexp, taxexp, fcf, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|drag_share_fcf|
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_logslope_252d_2d_v145_signal(intexp, taxexp, fcf, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|int_tax_combo|
def f015itd_f015_interest_and_tax_drag_int_tax_combo_logslope_63d_2d_v146_signal(intexp, taxexp, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs())).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|int_tax_combo|
def f015itd_f015_interest_and_tax_drag_int_tax_combo_logslope_252d_2d_v147_signal(intexp, taxexp, closeadj):
    base = np.log(((intexp.abs() + taxexp.abs())).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

