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


# 21d acceleration of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accel_21d_3d_v001_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accel_63d_3d_v002_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accel_126d_3d_v003_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accel_252d_3d_v004_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accel_21d_3d_v005_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accel_63d_3d_v006_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accel_126d_3d_v007_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accel_252d_3d_v008_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accel_21d_3d_v009_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accel_63d_3d_v010_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accel_126d_3d_v011_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accel_252d_3d_v012_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accel_21d_3d_v013_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accel_63d_3d_v014_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accel_126d_3d_v015_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accel_252d_3d_v016_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accel_21d_3d_v017_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accel_63d_3d_v018_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accel_126d_3d_v019_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accel_252d_3d_v020_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accel_21d_3d_v021_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accel_63d_3d_v022_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accel_126d_3d_v023_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accel_252d_3d_v024_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accel_21d_3d_v025_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accel_63d_3d_v026_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accel_126d_3d_v027_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accel_252d_3d_v028_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slopez_21d_z126_3d_v029_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slopez_63d_z252_3d_v030_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slopez_126d_z252_3d_v031_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_slopez_252d_z504_3d_v032_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slopez_21d_z126_3d_v033_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slopez_63d_z252_3d_v034_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slopez_126d_z252_3d_v035_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_slopez_252d_z504_3d_v036_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slopez_21d_z126_3d_v037_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slopez_63d_z252_3d_v038_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slopez_126d_z252_3d_v039_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_slopez_252d_z504_3d_v040_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slopez_21d_z126_3d_v041_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slopez_63d_z252_3d_v042_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slopez_126d_z252_3d_v043_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_slopez_252d_z504_3d_v044_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slopez_21d_z126_3d_v045_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slopez_63d_z252_3d_v046_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slopez_126d_z252_3d_v047_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_slopez_252d_z504_3d_v048_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slopez_21d_z126_3d_v049_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slopez_63d_z252_3d_v050_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slopez_126d_z252_3d_v051_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_slopez_252d_z504_3d_v052_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slopez_21d_z126_3d_v053_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slopez_63d_z252_3d_v054_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slopez_126d_z252_3d_v055_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_slopez_252d_z504_3d_v056_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_jerk_21d_3d_v057_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_jerk_63d_3d_v058_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_jerk_126d_3d_v059_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_jerk_21d_3d_v060_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_jerk_63d_3d_v061_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_jerk_126d_3d_v062_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_jerk_21d_3d_v063_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_jerk_63d_3d_v064_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_jerk_126d_3d_v065_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_jerk_21d_3d_v066_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_jerk_63d_3d_v067_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_jerk_126d_3d_v068_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_jerk_21d_3d_v069_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_jerk_63d_3d_v070_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_jerk_126d_3d_v071_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_jerk_21d_3d_v072_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_jerk_63d_3d_v073_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_jerk_126d_3d_v074_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_jerk_21d_3d_v075_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_jerk_63d_3d_v076_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_jerk_126d_3d_v077_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_lvl smoothed over 252d
def f060nce_f060_non_cash_expense_mix_noncash_lvl_smoothaccel_63d_sm252_3d_v078_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_lvl smoothed over 504d
def f060nce_f060_non_cash_expense_mix_noncash_lvl_smoothaccel_252d_sm504_3d_v079_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_to_opex smoothed over 252d
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_smoothaccel_63d_sm252_3d_v080_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_to_opex smoothed over 504d
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_smoothaccel_252d_sm504_3d_v081_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_to_netloss smoothed over 252d
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_smoothaccel_63d_sm252_3d_v082_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_to_netloss smoothed over 504d
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_smoothaccel_252d_sm504_3d_v083_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_share_chg smoothed over 252d
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_smoothaccel_63d_sm252_3d_v084_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_share_chg smoothed over 504d
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_smoothaccel_252d_sm504_3d_v085_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dep_sbc_ratio smoothed over 252d
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_smoothaccel_63d_sm252_3d_v086_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dep_sbc_ratio smoothed over 504d
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_smoothaccel_252d_sm504_3d_v087_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_share_opex smoothed over 252d
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_smoothaccel_63d_sm252_3d_v088_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_share_opex smoothed over 504d
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_smoothaccel_252d_sm504_3d_v089_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_to_revenue smoothed over 252d
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_smoothaccel_63d_sm252_3d_v090_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_to_revenue smoothed over 504d
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_smoothaccel_252d_sm504_3d_v091_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accelz_21d_z252_3d_v092_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_accelz_63d_z504_3d_v093_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accelz_21d_z252_3d_v094_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_accelz_63d_z504_3d_v095_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accelz_21d_z252_3d_v096_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_accelz_63d_z504_3d_v097_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accelz_21d_z252_3d_v098_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_accelz_63d_z504_3d_v099_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accelz_21d_z252_3d_v100_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_accelz_63d_z504_3d_v101_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accelz_21d_z252_3d_v102_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_accelz_63d_z504_3d_v103_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accelz_21d_z252_3d_v104_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_to_revenue
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_accelz_63d_z504_3d_v105_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_lvl (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_lvl_signflip_63d_3d_v106_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_lvl (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_lvl_signflip_252d_3d_v107_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_to_opex (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_signflip_63d_3d_v108_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_to_opex (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_signflip_252d_3d_v109_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_to_netloss (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_signflip_63d_3d_v110_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_to_netloss (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_signflip_252d_3d_v111_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_share_chg (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_signflip_63d_3d_v112_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_share_chg (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_signflip_252d_3d_v113_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dep_sbc_ratio (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_signflip_63d_3d_v114_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dep_sbc_ratio (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_signflip_252d_3d_v115_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_share_opex (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_signflip_63d_3d_v116_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_share_opex (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_signflip_252d_3d_v117_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_to_revenue (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_signflip_63d_3d_v118_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_to_revenue (raw count, no price scaling)
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_signflip_252d_3d_v119_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_lvl normalized by 252d range
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rngaccel_63d_r252_3d_v120_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_lvl normalized by 504d range
def f060nce_f060_non_cash_expense_mix_noncash_lvl_rngaccel_252d_r504_3d_v121_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_opex normalized by 252d range
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rngaccel_63d_r252_3d_v122_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_opex normalized by 504d range
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_rngaccel_252d_r504_3d_v123_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_netloss normalized by 252d range
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_rngaccel_63d_r252_3d_v124_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_netloss normalized by 504d range
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_rngaccel_252d_r504_3d_v125_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_share_chg normalized by 252d range
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_rngaccel_63d_r252_3d_v126_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_share_chg normalized by 504d range
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_rngaccel_252d_r504_3d_v127_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dep_sbc_ratio normalized by 252d range
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_rngaccel_63d_r252_3d_v128_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dep_sbc_ratio normalized by 504d range
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_rngaccel_252d_r504_3d_v129_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_share_opex normalized by 252d range
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_rngaccel_63d_r252_3d_v130_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_share_opex normalized by 504d range
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_rngaccel_252d_r504_3d_v131_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_to_revenue normalized by 252d range
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_rngaccel_63d_r252_3d_v132_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_to_revenue normalized by 504d range
def f060nce_f060_non_cash_expense_mix_noncash_to_revenue_rngaccel_252d_r504_3d_v133_signal(depamor, sbcomp, revenue, closeadj):
    base = _f060_noncash(depamor, sbcomp) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_cumslope_21d_3d_v134_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_cumslope_63d_3d_v135_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of noncash_lvl
def f060nce_f060_non_cash_expense_mix_noncash_lvl_cumslope_252d_3d_v136_signal(depamor, sbcomp, closeadj):
    base = _f060_noncash(depamor, sbcomp)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_cumslope_21d_3d_v137_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_cumslope_63d_3d_v138_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of noncash_to_opex
def f060nce_f060_non_cash_expense_mix_noncash_to_opex_cumslope_252d_3d_v139_signal(depamor, sbcomp, opex, closeadj):
    base = _f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_cumslope_21d_3d_v140_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_cumslope_63d_3d_v141_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of noncash_to_netloss
def f060nce_f060_non_cash_expense_mix_noncash_to_netloss_cumslope_252d_3d_v142_signal(depamor, sbcomp, netinc, closeadj):
    base = _f060_noncash(depamor, sbcomp) / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_cumslope_21d_3d_v143_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_cumslope_63d_3d_v144_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of noncash_share_chg
def f060nce_f060_non_cash_expense_mix_noncash_share_chg_cumslope_252d_3d_v145_signal(depamor, sbcomp, opex, closeadj):
    base = (_f060_noncash(depamor, sbcomp) / opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_cumslope_21d_3d_v146_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_cumslope_63d_3d_v147_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dep_sbc_ratio
def f060nce_f060_non_cash_expense_mix_dep_sbc_ratio_cumslope_252d_3d_v148_signal(depamor, sbcomp, closeadj):
    base = depamor / sbcomp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_cumslope_21d_3d_v149_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_share_opex
def f060nce_f060_non_cash_expense_mix_sbc_share_opex_cumslope_63d_3d_v150_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

