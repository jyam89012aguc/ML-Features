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


# 63d z-score of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_z_63d_base_v076_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_z_126d_base_v077_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_z_252d_base_v078_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_z_504d_base_v079_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_z_63d_base_v080_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_z_126d_base_v081_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_z_252d_base_v082_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_z_504d_base_v083_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_z_63d_base_v084_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_z_126d_base_v085_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_z_252d_base_v086_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_z_504d_base_v087_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_z_63d_base_v088_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_z_126d_base_v089_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_z_252d_base_v090_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_z_504d_base_v091_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_z_63d_base_v092_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_z_126d_base_v093_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_z_252d_base_v094_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_z_504d_base_v095_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_z_63d_base_v096_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_z_126d_base_v097_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_z_252d_base_v098_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_z_504d_base_v099_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_z_63d_base_v100_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_z_126d_base_v101_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_z_252d_base_v102_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_z_504d_base_v103_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_distmax_252d_base_v104_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_distmax_504d_base_v105_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_distmax_252d_base_v106_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_distmax_504d_base_v107_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_distmax_252d_base_v108_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_distmax_504d_base_v109_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_distmax_252d_base_v110_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_distmax_504d_base_v111_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_distmax_252d_base_v112_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_distmax_504d_base_v113_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_distmax_252d_base_v114_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_distmax_504d_base_v115_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_distmax_252d_base_v116_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_distmax_504d_base_v117_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_distmed_126d_base_v118_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_distmed_252d_base_v119_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_distmed_504d_base_v120_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_distmed_126d_base_v121_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_distmed_252d_base_v122_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_distmed_504d_base_v123_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_distmed_126d_base_v124_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_distmed_252d_base_v125_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_distmed_504d_base_v126_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_distmed_126d_base_v127_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_distmed_252d_base_v128_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_distmed_504d_base_v129_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_distmed_126d_base_v130_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_distmed_252d_base_v131_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_distmed_504d_base_v132_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_distmed_126d_base_v133_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_distmed_252d_base_v134_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_distmed_504d_base_v135_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_distmed_126d_base_v136_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_distmed_252d_base_v137_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of int_tax_combo
def f015itd_f015_interest_and_tax_drag_int_tax_combo_distmed_504d_base_v138_signal(intexp, taxexp, closeadj):
    base = (intexp.abs() + taxexp.abs())
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_chg_63d_base_v139_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in int_to_ocf
def f015itd_f015_interest_and_tax_drag_int_to_ocf_chg_252d_base_v140_signal(intexp, ncfo, closeadj):
    base = _f015_int_to_ocf(intexp, ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_chg_63d_base_v141_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_to_ocf
def f015itd_f015_interest_and_tax_drag_tax_to_ocf_chg_252d_base_v142_signal(taxexp, ncfo, closeadj):
    base = _f015_tax_to_ocf(taxexp, ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_chg_63d_base_v143_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in int_to_debt
def f015itd_f015_interest_and_tax_drag_int_to_debt_chg_252d_base_v144_signal(intexp, debt, closeadj):
    base = intexp.abs() / debt.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_chg_63d_base_v145_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tax_rate_local
def f015itd_f015_interest_and_tax_drag_tax_rate_local_chg_252d_base_v146_signal(taxexp, ebt, closeadj):
    base = taxexp / ebt.replace(0, np.nan).abs() * 1.0
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_chg_63d_base_v147_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drag_share_rev
def f015itd_f015_interest_and_tax_drag_drag_share_rev_chg_252d_base_v148_signal(intexp, taxexp, revenue, closeadj):
    base = (intexp.abs() + taxexp.abs()) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_chg_63d_base_v149_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drag_share_fcf
def f015itd_f015_interest_and_tax_drag_drag_share_fcf_chg_252d_base_v150_signal(intexp, taxexp, fcf, closeadj):
    base = (intexp.abs() + taxexp.abs()) / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

