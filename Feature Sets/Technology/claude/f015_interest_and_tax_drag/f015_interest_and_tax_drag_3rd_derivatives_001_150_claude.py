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


# 21d acceleration of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accel_21d_3d_v001_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accel_63d_3d_v002_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accel_126d_3d_v003_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accel_252d_3d_v004_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accel_21d_3d_v005_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accel_63d_3d_v006_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accel_126d_3d_v007_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accel_252d_3d_v008_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accel_21d_3d_v009_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accel_63d_3d_v010_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accel_126d_3d_v011_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accel_252d_3d_v012_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accel_21d_3d_v013_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accel_63d_3d_v014_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accel_126d_3d_v015_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accel_252d_3d_v016_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accel_21d_3d_v017_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accel_63d_3d_v018_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accel_126d_3d_v019_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accel_252d_3d_v020_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accel_21d_3d_v021_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accel_63d_3d_v022_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accel_126d_3d_v023_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accel_252d_3d_v024_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accel_21d_3d_v025_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accel_63d_3d_v026_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accel_126d_3d_v027_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accel_252d_3d_v028_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slopez_21d_z126_3d_v029_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slopez_63d_z252_3d_v030_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slopez_126d_z252_3d_v031_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_slopez_252d_z504_3d_v032_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slopez_21d_z126_3d_v033_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slopez_63d_z252_3d_v034_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slopez_126d_z252_3d_v035_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_slopez_252d_z504_3d_v036_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slopez_21d_z126_3d_v037_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slopez_63d_z252_3d_v038_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slopez_126d_z252_3d_v039_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_slopez_252d_z504_3d_v040_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slopez_21d_z126_3d_v041_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slopez_63d_z252_3d_v042_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slopez_126d_z252_3d_v043_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_slopez_252d_z504_3d_v044_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slopez_21d_z126_3d_v045_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slopez_63d_z252_3d_v046_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slopez_126d_z252_3d_v047_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_slopez_252d_z504_3d_v048_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slopez_21d_z126_3d_v049_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slopez_63d_z252_3d_v050_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slopez_126d_z252_3d_v051_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_slopez_252d_z504_3d_v052_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slopez_21d_z126_3d_v053_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slopez_63d_z252_3d_v054_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slopez_126d_z252_3d_v055_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_slopez_252d_z504_3d_v056_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_jerk_21d_3d_v057_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_jerk_63d_3d_v058_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_jerk_126d_3d_v059_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_jerk_21d_3d_v060_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_jerk_63d_3d_v061_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_jerk_126d_3d_v062_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_jerk_21d_3d_v063_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_jerk_63d_3d_v064_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_jerk_126d_3d_v065_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_jerk_21d_3d_v066_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_jerk_63d_3d_v067_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_jerk_126d_3d_v068_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_jerk_21d_3d_v069_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_jerk_63d_3d_v070_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_jerk_126d_3d_v071_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_jerk_21d_3d_v072_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_jerk_63d_3d_v073_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_jerk_126d_3d_v074_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_jerk_21d_3d_v075_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_jerk_63d_3d_v076_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_jerk_126d_3d_v077_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of int_to_ocf smoothed over 252d
def f015itd_f015_interest_and_tax_drag_int_to_ocf_smoothaccel_63d_sm252_3d_v078_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of int_to_ocf smoothed over 504d
def f015itd_f015_interest_and_tax_drag_int_to_ocf_smoothaccel_252d_sm504_3d_v079_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_to_ocf smoothed over 252d
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_smoothaccel_63d_sm252_3d_v080_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_to_ocf smoothed over 504d
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_smoothaccel_252d_sm504_3d_v081_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of int_to_debt smoothed over 252d
def f015itd_f015_interest_and_tax_drag_int_to_debt_smoothaccel_63d_sm252_3d_v082_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of int_to_debt smoothed over 504d
def f015itd_f015_interest_and_tax_drag_int_to_debt_smoothaccel_252d_sm504_3d_v083_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tax_rate_local smoothed over 252d
def f015itd_f015_interest_and_tax_drag_tax_rate_local_smoothaccel_63d_sm252_3d_v084_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tax_rate_local smoothed over 504d
def f015itd_f015_interest_and_tax_drag_tax_rate_local_smoothaccel_252d_sm504_3d_v085_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drag_share_rev smoothed over 252d
def f015itd_f015_interest_and_tax_drag_drag_share_rev_smoothaccel_63d_sm252_3d_v086_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drag_share_rev smoothed over 504d
def f015itd_f015_interest_and_tax_drag_drag_share_rev_smoothaccel_252d_sm504_3d_v087_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of drag_share_fcf smoothed over 252d
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_smoothaccel_63d_sm252_3d_v088_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of drag_share_fcf smoothed over 504d
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_smoothaccel_252d_sm504_3d_v089_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of int_tax_combo smoothed over 252d
def f015itd_f015_interest_and_tax_drag_int_tax_combo_smoothaccel_63d_sm252_3d_v090_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of int_tax_combo smoothed over 504d
def f015itd_f015_interest_and_tax_drag_int_tax_combo_smoothaccel_252d_sm504_3d_v091_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accelz_21d_z252_3d_v092_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_accelz_63d_z504_3d_v093_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accelz_21d_z252_3d_v094_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_accelz_63d_z504_3d_v095_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accelz_21d_z252_3d_v096_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_accelz_63d_z504_3d_v097_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accelz_21d_z252_3d_v098_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_accelz_63d_z504_3d_v099_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accelz_21d_z252_3d_v100_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_accelz_63d_z504_3d_v101_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accelz_21d_z252_3d_v102_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_accelz_63d_z504_3d_v103_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accelz_21d_z252_3d_v104_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_accelz_63d_z504_3d_v105_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in int_to_ocf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_to_ocf_signflip_63d_3d_v106_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in int_to_ocf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_to_ocf_signflip_252d_3d_v107_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_to_ocf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_signflip_63d_3d_v108_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_to_ocf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_signflip_252d_3d_v109_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in int_to_debt (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_to_debt_signflip_63d_3d_v110_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in int_to_debt (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_to_debt_signflip_252d_3d_v111_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tax_rate_local (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_tax_rate_local_signflip_63d_3d_v112_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tax_rate_local (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_tax_rate_local_signflip_252d_3d_v113_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drag_share_rev (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_drag_share_rev_signflip_63d_3d_v114_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drag_share_rev (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_drag_share_rev_signflip_252d_3d_v115_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in drag_share_fcf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_signflip_63d_3d_v116_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in drag_share_fcf (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_signflip_252d_3d_v117_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in int_tax_combo (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_tax_combo_signflip_63d_3d_v118_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in int_tax_combo (raw count, no price scaling)
def f015itd_f015_interest_and_tax_drag_int_tax_combo_signflip_252d_3d_v119_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_ocf normalized by 252d range
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rngaccel_63d_r252_3d_v120_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_ocf normalized by 504d range
def f015itd_f015_interest_and_tax_drag_int_to_ocf_rngaccel_252d_r504_3d_v121_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_to_ocf normalized by 252d range
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rngaccel_63d_r252_3d_v122_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_to_ocf normalized by 504d range
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_rngaccel_252d_r504_3d_v123_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_to_debt normalized by 252d range
def f015itd_f015_interest_and_tax_drag_int_to_debt_rngaccel_63d_r252_3d_v124_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_to_debt normalized by 504d range
def f015itd_f015_interest_and_tax_drag_int_to_debt_rngaccel_252d_r504_3d_v125_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tax_rate_local normalized by 252d range
def f015itd_f015_interest_and_tax_drag_tax_rate_local_rngaccel_63d_r252_3d_v126_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tax_rate_local normalized by 504d range
def f015itd_f015_interest_and_tax_drag_tax_rate_local_rngaccel_252d_r504_3d_v127_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drag_share_rev normalized by 252d range
def f015itd_f015_interest_and_tax_drag_drag_share_rev_rngaccel_63d_r252_3d_v128_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drag_share_rev normalized by 504d range
def f015itd_f015_interest_and_tax_drag_drag_share_rev_rngaccel_252d_r504_3d_v129_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of drag_share_fcf normalized by 252d range
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_rngaccel_63d_r252_3d_v130_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of drag_share_fcf normalized by 504d range
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_rngaccel_252d_r504_3d_v131_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of int_tax_combo normalized by 252d range
def f015itd_f015_interest_and_tax_drag_int_tax_combo_rngaccel_63d_r252_3d_v132_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of int_tax_combo normalized by 504d range
def f015itd_f015_interest_and_tax_drag_int_tax_combo_rngaccel_252d_r504_3d_v133_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_cumslope_21d_3d_v134_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_cumslope_63d_3d_v135_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_cumslope_252d_3d_v136_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_cumslope_21d_3d_v137_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_cumslope_63d_3d_v138_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_cumslope_252d_3d_v139_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_cumslope_21d_3d_v140_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_cumslope_63d_3d_v141_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_cumslope_252d_3d_v142_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_cumslope_21d_3d_v143_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_cumslope_63d_3d_v144_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_cumslope_252d_3d_v145_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_cumslope_21d_3d_v146_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_cumslope_63d_3d_v147_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_cumslope_252d_3d_v148_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_cumslope_21d_3d_v149_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_cumslope_63d_3d_v150_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

