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
def _f060_noncash(depamor, sbcomp):
    return depamor.fillna(0) + sbcomp.fillna(0)


# 21d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slope_21d_2d_v001_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slope_63d_2d_v002_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slope_126d_2d_v003_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slope_252d_2d_v004_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slope_504d_2d_v005_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slope_21d_2d_v006_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slope_63d_2d_v007_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slope_126d_2d_v008_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slope_252d_2d_v009_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slope_504d_2d_v010_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slope_21d_2d_v011_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slope_63d_2d_v012_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slope_126d_2d_v013_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slope_252d_2d_v014_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slope_504d_2d_v015_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slope_21d_2d_v016_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slope_63d_2d_v017_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slope_126d_2d_v018_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slope_252d_2d_v019_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slope_504d_2d_v020_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slope_21d_2d_v021_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slope_63d_2d_v022_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slope_126d_2d_v023_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slope_252d_2d_v024_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slope_504d_2d_v025_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slope_21d_2d_v026_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slope_63d_2d_v027_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slope_126d_2d_v028_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slope_252d_2d_v029_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slope_504d_2d_v030_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slope_21d_2d_v031_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slope_63d_2d_v032_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slope_126d_2d_v033_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slope_252d_2d_v034_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slope_504d_2d_v035_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sm21_sl21_2d_v036_signal(depamor, sbcomp, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sm63_sl21_2d_v037_signal(depamor, sbcomp, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sm63_sl63_2d_v038_signal(depamor, sbcomp, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sm252_sl63_2d_v039_signal(depamor, sbcomp, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sm252_sl126_2d_v040_signal(depamor, sbcomp, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sm21_sl21_2d_v041_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sm63_sl21_2d_v042_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sm63_sl63_2d_v043_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sm252_sl63_2d_v044_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sm252_sl126_2d_v045_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sm21_sl21_2d_v046_signal(depamor, sbcomp, netinc, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sm63_sl21_2d_v047_signal(depamor, sbcomp, netinc, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sm63_sl63_2d_v048_signal(depamor, sbcomp, netinc, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sm252_sl63_2d_v049_signal(depamor, sbcomp, netinc, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sm252_sl126_2d_v050_signal(depamor, sbcomp, netinc, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sm21_sl21_2d_v051_signal(depamor, sbcomp, opex, closeadj):
    base = _mean((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sm63_sl21_2d_v052_signal(depamor, sbcomp, opex, closeadj):
    base = _mean((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sm63_sl63_2d_v053_signal(depamor, sbcomp, opex, closeadj):
    base = _mean((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sm252_sl63_2d_v054_signal(depamor, sbcomp, opex, closeadj):
    base = _mean((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sm252_sl126_2d_v055_signal(depamor, sbcomp, opex, closeadj):
    base = _mean((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sm21_sl21_2d_v056_signal(depamor, sbcomp, closeadj):
    base = _mean(depamor / sbcomp.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sm63_sl21_2d_v057_signal(depamor, sbcomp, closeadj):
    base = _mean(depamor / sbcomp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sm63_sl63_2d_v058_signal(depamor, sbcomp, closeadj):
    base = _mean(depamor / sbcomp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sm252_sl63_2d_v059_signal(depamor, sbcomp, closeadj):
    base = _mean(depamor / sbcomp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sm252_sl126_2d_v060_signal(depamor, sbcomp, closeadj):
    base = _mean(depamor / sbcomp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sm21_sl21_2d_v061_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sm63_sl21_2d_v062_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sm63_sl63_2d_v063_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sm252_sl63_2d_v064_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sm252_sl126_2d_v065_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sm21_sl21_2d_v066_signal(depamor, sbcomp, revenue, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sm63_sl21_2d_v067_signal(depamor, sbcomp, revenue, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sm63_sl63_2d_v068_signal(depamor, sbcomp, revenue, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sm252_sl63_2d_v069_signal(depamor, sbcomp, revenue, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sm252_sl126_2d_v070_signal(depamor, sbcomp, revenue, closeadj):
    base = _mean(_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_pctslope_21d_2d_v071_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_pctslope_63d_2d_v072_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_pctslope_252d_2d_v073_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_pctslope_21d_2d_v074_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_pctslope_63d_2d_v075_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_pctslope_252d_2d_v076_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_pctslope_21d_2d_v077_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_pctslope_63d_2d_v078_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_pctslope_252d_2d_v079_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_pctslope_21d_2d_v080_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_pctslope_63d_2d_v081_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_pctslope_252d_2d_v082_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_pctslope_21d_2d_v083_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_pctslope_63d_2d_v084_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_pctslope_252d_2d_v085_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_pctslope_21d_2d_v086_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_pctslope_63d_2d_v087_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_pctslope_252d_2d_v088_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_pctslope_21d_2d_v089_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_pctslope_63d_2d_v090_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_pctslope_252d_2d_v091_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sgnslope_21d_2d_v092_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sgnslope_63d_2d_v093_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_sgnslope_252d_2d_v094_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sgnslope_21d_2d_v095_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sgnslope_63d_2d_v096_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_sgnslope_252d_2d_v097_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sgnslope_21d_2d_v098_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sgnslope_63d_2d_v099_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_sgnslope_252d_2d_v100_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sgnslope_21d_2d_v101_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sgnslope_63d_2d_v102_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_sgnslope_252d_2d_v103_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sgnslope_21d_2d_v104_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sgnslope_63d_2d_v105_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_sgnslope_252d_2d_v106_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sgnslope_21d_2d_v107_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sgnslope_63d_2d_v108_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_sgnslope_252d_2d_v109_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sgnslope_21d_2d_v110_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sgnslope_63d_2d_v111_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_sgnslope_252d_2d_v112_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_logmagslope_21d_2d_v113_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_logmagslope_63d_2d_v114_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_logmagslope_252d_2d_v115_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_logmagslope_21d_2d_v116_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_logmagslope_63d_2d_v117_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_logmagslope_252d_2d_v118_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_logmagslope_21d_2d_v119_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_logmagslope_63d_2d_v120_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_logmagslope_252d_2d_v121_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_logmagslope_21d_2d_v122_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_logmagslope_63d_2d_v123_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_logmagslope_252d_2d_v124_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_logmagslope_21d_2d_v125_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_logmagslope_63d_2d_v126_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_logmagslope_252d_2d_v127_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_logmagslope_21d_2d_v128_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_logmagslope_63d_2d_v129_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_logmagslope_252d_2d_v130_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_logmagslope_21d_2d_v131_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_logmagslope_63d_2d_v132_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_logmagslope_252d_2d_v133_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_lvl|
def f060nce_f060_non_cash_expense_mix_noncash_lvl_logslope_63d_2d_v134_signal(depamor, sbcomp, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_lvl|
def f060nce_f060_non_cash_expense_mix_noncash_lvl_logslope_252d_2d_v135_signal(depamor, sbcomp, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_to_opex|
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_logslope_63d_2d_v136_signal(depamor, sbcomp, opex, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_to_opex|
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_logslope_252d_2d_v137_signal(depamor, sbcomp, opex, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_to_netloss|
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_logslope_63d_2d_v138_signal(depamor, sbcomp, netinc, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_to_netloss|
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_logslope_252d_2d_v139_signal(depamor, sbcomp, netinc, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_share_chg|
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_logslope_63d_2d_v140_signal(depamor, sbcomp, opex, closeadj):
    base = np.log(((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_share_chg|
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_logslope_252d_2d_v141_signal(depamor, sbcomp, opex, closeadj):
    base = np.log(((_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dep_sbc_ratio|
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_logslope_63d_2d_v142_signal(depamor, sbcomp, closeadj):
    base = np.log((depamor / sbcomp.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dep_sbc_ratio|
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_logslope_252d_2d_v143_signal(depamor, sbcomp, closeadj):
    base = np.log((depamor / sbcomp.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_share_opex|
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_logslope_63d_2d_v144_signal(sbcomp, opex, closeadj):
    base = np.log((sbcomp / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_share_opex|
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_logslope_252d_2d_v145_signal(sbcomp, opex, closeadj):
    base = np.log((sbcomp / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_to_revenue|
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_logslope_63d_2d_v146_signal(depamor, sbcomp, revenue, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_to_revenue|
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_logslope_252d_2d_v147_signal(depamor, sbcomp, revenue, closeadj):
    base = np.log((_f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

