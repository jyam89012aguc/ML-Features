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
def _f060_noncash(depamor, sbcomp):
    return depamor.fillna(0) + sbcomp.fillna(0)


# 63d z-score of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_z_63d_base_v076_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_z_126d_base_v077_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_z_252d_base_v078_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_z_504d_base_v079_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_z_63d_base_v080_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_z_126d_base_v081_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_z_252d_base_v082_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_z_504d_base_v083_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_z_63d_base_v084_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_z_126d_base_v085_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_z_252d_base_v086_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_z_504d_base_v087_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_z_63d_base_v088_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_z_126d_base_v089_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_z_252d_base_v090_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_z_504d_base_v091_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_z_63d_base_v092_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_z_126d_base_v093_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_z_252d_base_v094_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_z_504d_base_v095_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_z_63d_base_v096_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_z_126d_base_v097_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_z_252d_base_v098_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_z_504d_base_v099_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_z_63d_base_v100_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_z_126d_base_v101_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_z_252d_base_v102_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_z_504d_base_v103_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_distmax_252d_base_v104_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_distmax_504d_base_v105_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_distmax_252d_base_v106_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_distmax_504d_base_v107_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_distmax_252d_base_v108_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_distmax_504d_base_v109_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_distmax_252d_base_v110_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_distmax_504d_base_v111_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_distmax_252d_base_v112_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_distmax_504d_base_v113_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_distmax_252d_base_v114_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_distmax_504d_base_v115_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_distmax_252d_base_v116_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_distmax_504d_base_v117_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_distmed_126d_base_v118_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_distmed_252d_base_v119_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_distmed_504d_base_v120_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_distmed_126d_base_v121_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_distmed_252d_base_v122_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_distmed_504d_base_v123_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_distmed_126d_base_v124_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_distmed_252d_base_v125_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_distmed_504d_base_v126_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_distmed_126d_base_v127_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_distmed_252d_base_v128_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_distmed_504d_base_v129_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_distmed_126d_base_v130_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_distmed_252d_base_v131_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_distmed_504d_base_v132_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_distmed_126d_base_v133_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_distmed_252d_base_v134_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_distmed_504d_base_v135_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_distmed_126d_base_v136_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_distmed_252d_base_v137_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_distmed_504d_base_v138_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_chg_63d_base_v139_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_chg_252d_base_v140_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_chg_63d_base_v141_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_chg_252d_base_v142_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_chg_63d_base_v143_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_chg_252d_base_v144_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_chg_63d_base_v145_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_chg_252d_base_v146_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_chg_63d_base_v147_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_chg_252d_base_v148_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_chg_63d_base_v149_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_chg_252d_base_v150_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

