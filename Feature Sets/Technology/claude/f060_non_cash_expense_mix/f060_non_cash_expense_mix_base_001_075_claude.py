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


# 21d mean of noncash_lvl scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_lvl_mean_21d_base_v001_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of noncash_lvl scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_lvl_mean_63d_base_v002_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of noncash_lvl scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_lvl_mean_126d_base_v003_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of noncash_lvl scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_lvl_mean_252d_base_v004_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of noncash_lvl scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_lvl_mean_504d_base_v005_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of noncash_to_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_mean_21d_base_v006_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of noncash_to_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_mean_63d_base_v007_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of noncash_to_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_mean_126d_base_v008_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of noncash_to_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_mean_252d_base_v009_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of noncash_to_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_mean_504d_base_v010_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of noncash_to_netloss scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_mean_21d_base_v011_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of noncash_to_netloss scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_mean_63d_base_v012_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of noncash_to_netloss scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_mean_126d_base_v013_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of noncash_to_netloss scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_mean_252d_base_v014_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of noncash_to_netloss scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_mean_504d_base_v015_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of noncash_share_chg scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_mean_21d_base_v016_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of noncash_share_chg scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_mean_63d_base_v017_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of noncash_share_chg scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_mean_126d_base_v018_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of noncash_share_chg scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_mean_252d_base_v019_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of noncash_share_chg scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_mean_504d_base_v020_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dep_sbc_ratio scaled by closeadj
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_mean_21d_base_v021_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dep_sbc_ratio scaled by closeadj
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_mean_63d_base_v022_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dep_sbc_ratio scaled by closeadj
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_mean_126d_base_v023_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dep_sbc_ratio scaled by closeadj
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_mean_252d_base_v024_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dep_sbc_ratio scaled by closeadj
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_mean_504d_base_v025_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_share_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_mean_21d_base_v026_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_share_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_mean_63d_base_v027_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_share_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_mean_126d_base_v028_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_share_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_mean_252d_base_v029_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_share_opex scaled by closeadj
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_mean_504d_base_v030_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of noncash_to_revenue scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_mean_21d_base_v031_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of noncash_to_revenue scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_mean_63d_base_v032_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of noncash_to_revenue scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_mean_126d_base_v033_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of noncash_to_revenue scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_mean_252d_base_v034_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of noncash_to_revenue scaled by closeadj
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_mean_504d_base_v035_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_median_63d_base_v036_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_median_252d_base_v037_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_median_504d_base_v038_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_median_63d_base_v039_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_median_252d_base_v040_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_median_504d_base_v041_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_median_63d_base_v042_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_median_252d_base_v043_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_median_504d_base_v044_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_median_63d_base_v045_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_median_252d_base_v046_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_median_504d_base_v047_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_median_63d_base_v048_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_median_252d_base_v049_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_median_504d_base_v050_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_median_63d_base_v051_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_median_252d_base_v052_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_median_504d_base_v053_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_median_63d_base_v054_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_median_252d_base_v055_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_median_504d_base_v056_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rmax_252d_base_v057_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rmax_504d_base_v058_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rmax_252d_base_v059_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rmax_504d_base_v060_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_rmax_252d_base_v061_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_rmax_504d_base_v062_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_rmax_252d_base_v063_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_rmax_504d_base_v064_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_rmax_252d_base_v065_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_rmax_504d_base_v066_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_rmax_252d_base_v067_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_rmax_504d_base_v068_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_rmax_252d_base_v069_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_rmax_504d_base_v070_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rmin_252d_base_v071_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rmin_504d_base_v072_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rmin_252d_base_v073_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rmin_504d_base_v074_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_rmin_252d_base_v075_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

