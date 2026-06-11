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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f45_net_debt(debt, cashneq):
    return debt - cashneq


def _f45_bs_strength(equity, debt, w):
    return _mean(equity, w) / _mean(debt, w).replace(0, np.nan)


def _f45_solvency_proxy(equity, liabilities, w):
    return _mean(equity, w) / _mean(liabilities, w).replace(0, np.nan)

# v001: _slope_pct window 5 of netdebt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v001_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: _slope_diff_norm window 21 of netdebt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v002_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: _diff window 63 of netdebt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v003_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: _slope_pct window 5 of netdebt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v004_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: _slope_diff_norm window 21 of netdebt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v005_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: _diff window 63 of netdebt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v006_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: _slope_pct window 5 of netdebt_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v007_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: _slope_diff_norm window 21 of netdebt_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v008_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: _diff window 63 of netdebt_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v009_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: _slope_pct window 5 of netdebt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v010_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: _slope_diff_norm window 21 of netdebt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v011_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: _diff window 63 of netdebt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v012_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: _slope_pct window 5 of netdebt_504d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v013_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: _slope_diff_norm window 21 of netdebt_504d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v014_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: _diff window 63 of netdebt_504d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v015_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: _slope_pct window 5 of bsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v016_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: _slope_diff_norm window 21 of bsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v017_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: _diff window 63 of bsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v018_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: _slope_pct window 5 of bsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v019_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: _slope_diff_norm window 21 of bsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v020_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: _diff window 63 of bsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v021_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: _slope_pct window 5 of bsstr_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v022_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: _slope_diff_norm window 21 of bsstr_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v023_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: _diff window 63 of bsstr_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v024_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: _slope_pct window 5 of bsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v025_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: _slope_diff_norm window 21 of bsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v026_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: _diff window 63 of bsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v027_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: _slope_pct window 5 of bsstr_504d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v028_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: _slope_diff_norm window 21 of bsstr_504d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v029_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: _diff window 63 of bsstr_504d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v030_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: _slope_pct window 5 of solv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v031_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: _slope_diff_norm window 21 of solv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v032_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: _diff window 63 of solv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v033_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: _slope_pct window 5 of solv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v034_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: _slope_diff_norm window 21 of solv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v035_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: _diff window 63 of solv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v036_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: _slope_pct window 5 of solv_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v037_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: _slope_diff_norm window 21 of solv_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v038_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: _diff window 63 of solv_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v039_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: _slope_pct window 5 of solv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v040_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: _slope_diff_norm window 21 of solv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v041_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: _diff window 63 of solv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v042_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: _slope_pct window 5 of solv_504d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v043_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: _slope_diff_norm window 21 of solv_504d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v044_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: _diff window 63 of solv_504d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v045_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: _slope_pct window 5 of ndxbsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v046_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_bs_strength(equity, debt, 21) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: _slope_diff_norm window 21 of ndxbsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v047_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_bs_strength(equity, debt, 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: _diff window 63 of ndxbsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v048_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_bs_strength(equity, debt, 21) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: _slope_pct window 5 of ndxbsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v049_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_bs_strength(equity, debt, 63) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: _slope_diff_norm window 21 of ndxbsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v050_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_bs_strength(equity, debt, 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: _diff window 63 of ndxbsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v051_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_bs_strength(equity, debt, 63) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: _slope_pct window 5 of ndxbsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v052_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_bs_strength(equity, debt, 252) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: _slope_diff_norm window 21 of ndxbsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v053_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_bs_strength(equity, debt, 252) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: _diff window 63 of ndxbsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v054_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_bs_strength(equity, debt, 252) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: _slope_pct window 5 of ndxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v055_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: _slope_diff_norm window 21 of ndxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v056_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: _diff window 63 of ndxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v057_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: _slope_pct window 5 of ndxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v058_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: _slope_diff_norm window 21 of ndxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v059_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: _diff window 63 of ndxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v060_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: _slope_pct window 5 of ndxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v061_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: _slope_diff_norm window 21 of ndxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v062_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: _diff window 63 of ndxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v063_signal(debt, cashneq, equity, liabilities, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: _slope_pct window 5 of bsstrxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v064_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: _slope_diff_norm window 21 of bsstrxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v065_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: _diff window 63 of bsstrxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v066_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: _slope_pct window 5 of bsstrxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v067_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: _slope_diff_norm window 21 of bsstrxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v068_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: _diff window 63 of bsstrxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v069_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: _slope_pct window 5 of bsstrxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v070_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: _slope_diff_norm window 21 of bsstrxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v071_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: _diff window 63 of bsstrxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v072_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: _slope_pct window 5 of netdebtema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v073_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 5).ewm(span=21, adjust=False).mean() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: _slope_diff_norm window 21 of netdebtema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v074_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 5).ewm(span=21, adjust=False).mean() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: _diff window 63 of netdebtema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v075_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 5).ewm(span=21, adjust=False).mean() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: _slope_pct window 5 of netdebtema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v076_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 15).ewm(span=63, adjust=False).mean() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: _slope_diff_norm window 21 of netdebtema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v077_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 15).ewm(span=63, adjust=False).mean() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: _diff window 63 of netdebtema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v078_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 15).ewm(span=63, adjust=False).mean() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: _slope_pct window 5 of netdebtema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v079_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).ewm(span=252, adjust=False).mean() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: _slope_diff_norm window 21 of netdebtema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v080_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).ewm(span=252, adjust=False).mean() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: _diff window 63 of netdebtema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v081_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).ewm(span=252, adjust=False).mean() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: _slope_pct window 5 of bsstrema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v082_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: _slope_diff_norm window 21 of bsstrema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v083_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: _diff window 63 of bsstrema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v084_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: _slope_pct window 5 of bsstrema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v085_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: _slope_diff_norm window 21 of bsstrema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v086_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: _diff window 63 of bsstrema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v087_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: _slope_pct window 5 of bsstrema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v088_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: _slope_diff_norm window 21 of bsstrema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v089_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: _diff window 63 of bsstrema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v090_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: _slope_pct window 5 of solvema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v091_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: _slope_diff_norm window 21 of solvema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v092_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: _diff window 63 of solvema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v093_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: _slope_pct window 5 of solvema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v094_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: _slope_diff_norm window 21 of solvema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v095_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: _diff window 63 of solvema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v096_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: _slope_pct window 5 of solvema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v097_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: _slope_diff_norm window 21 of solvema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v098_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: _diff window 63 of solvema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v099_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: _slope_pct window 5 of netdebtcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v100_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21).rolling(63, min_periods=21).sum() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: _slope_diff_norm window 21 of netdebtcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v101_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21).rolling(63, min_periods=21).sum() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: _diff window 63 of netdebtcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v102_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21).rolling(63, min_periods=21).sum() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: _slope_pct window 5 of netdebtcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v103_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: _slope_diff_norm window 21 of netdebtcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v104_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: _diff window 63 of netdebtcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v105_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: _slope_pct window 5 of netdebtcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v106_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: _slope_diff_norm window 21 of netdebtcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v107_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: _diff window 63 of netdebtcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v108_signal(debt, cashneq, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 126).rolling(252, min_periods=84).sum() * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: _slope_pct window 5 of bsstrcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v109_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: _slope_diff_norm window 21 of bsstrcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v110_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: _diff window 63 of bsstrcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v111_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: _slope_pct window 5 of bsstrcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v112_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: _slope_diff_norm window 21 of bsstrcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v113_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: _diff window 63 of bsstrcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v114_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: _slope_pct window 5 of bsstrcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v115_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: _slope_diff_norm window 21 of bsstrcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v116_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: _diff window 63 of bsstrcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v117_signal(equity, debt, closeadj):
    base = _f45_bs_strength(equity, debt, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: _slope_pct window 5 of solvcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v118_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: _slope_diff_norm window 21 of solvcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v119_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: _diff window 63 of solvcum_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v120_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: _slope_pct window 5 of solvcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v121_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: _slope_diff_norm window 21 of solvcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v122_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: _diff window 63 of solvcum_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v123_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: _slope_pct window 5 of solvcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v124_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: _slope_diff_norm window 21 of solvcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v125_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: _diff window 63 of solvcum_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v126_signal(equity, liabilities, closeadj):
    base = _f45_solvency_proxy(equity, liabilities, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: _slope_pct window 5 of composite_63d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v127_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 63), 252) + _z(_f45_bs_strength(equity, debt, 63), 252) + _z(_f45_solvency_proxy(equity, liabilities, 63), 252)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: _slope_diff_norm window 21 of composite_63d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v128_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 63), 252) + _z(_f45_bs_strength(equity, debt, 63), 252) + _z(_f45_solvency_proxy(equity, liabilities, 63), 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: _diff window 63 of composite_63d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v129_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 63), 252) + _z(_f45_bs_strength(equity, debt, 63), 252) + _z(_f45_solvency_proxy(equity, liabilities, 63), 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: _slope_pct window 5 of composite_252d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v130_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 252), 504) + _z(_f45_bs_strength(equity, debt, 252), 504) + _z(_f45_solvency_proxy(equity, liabilities, 252), 504)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: _slope_diff_norm window 21 of composite_252d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v131_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 252), 504) + _z(_f45_bs_strength(equity, debt, 252), 504) + _z(_f45_solvency_proxy(equity, liabilities, 252), 504)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: _diff window 63 of composite_252d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v132_signal(debt, cashneq, equity, liabilities, closeadj):
    base = (_z(_mean(_f45_net_debt(debt, cashneq), 252), 504) + _z(_f45_bs_strength(equity, debt, 252), 504) + _z(_f45_solvency_proxy(equity, liabilities, 252), 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: _slope_pct window 5 of netdebtxeq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v133_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) / _mean(equity, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: _slope_diff_norm window 21 of netdebtxeq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v134_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) / _mean(equity, 21).replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: _diff window 63 of netdebtxeq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v135_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 21) / _mean(equity, 21).replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: _slope_pct window 5 of netdebtxeq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v136_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) / _mean(equity, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: _slope_diff_norm window 21 of netdebtxeq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v137_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) / _mean(equity, 63).replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: _diff window 63 of netdebtxeq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v138_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 63) / _mean(equity, 63).replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: _slope_pct window 5 of netdebtxeq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v139_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) / _mean(equity, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: _slope_diff_norm window 21 of netdebtxeq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v140_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) / _mean(equity, 252).replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: _diff window 63 of netdebtxeq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v141_signal(debt, cashneq, equity, closeadj):
    base = _mean(_f45_net_debt(debt, cashneq), 252) / _mean(equity, 252).replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: _slope_pct window 5 of bsstrxsolv_alt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v142_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) + _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: _slope_diff_norm window 21 of bsstrxsolv_alt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v143_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) + _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: _diff window 63 of bsstrxsolv_alt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v144_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 21) + _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: _slope_pct window 5 of bsstrxsolv_alt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v145_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) + _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: _slope_diff_norm window 21 of bsstrxsolv_alt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v146_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) + _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: _diff window 63 of bsstrxsolv_alt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v147_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 63) + _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: _slope_pct window 5 of bsstrxsolv_alt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v148_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) + _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: _slope_diff_norm window 21 of bsstrxsolv_alt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v149_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) + _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: _diff window 63 of bsstrxsolv_alt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v150_signal(equity, debt, liabilities, closeadj):
    base = _f45_bs_strength(equity, debt, 252) + _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v001_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v002_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_slope_v003_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v004_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v005_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_slope_v006_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v007_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v008_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_slope_v009_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v010_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v011_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_slope_v012_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v013_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v014_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_slope_v015_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v016_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v017_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_slope_v018_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v019_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v020_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_slope_v021_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v022_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v023_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_slope_v024_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v025_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v026_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_slope_v027_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v028_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v029_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_slope_v030_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v031_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v032_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_slope_v033_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v034_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v035_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_slope_v036_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v037_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v038_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_slope_v039_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v040_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v041_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_slope_v042_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v043_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v044_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_slope_v045_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v046_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v047_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_slope_v048_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v049_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v050_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_slope_v051_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v052_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v053_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_slope_v054_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v055_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v056_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_slope_v057_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v058_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v059_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_slope_v060_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v061_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v062_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_slope_v063_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v064_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v065_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_slope_v066_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v067_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v068_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_slope_v069_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v070_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v071_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_slope_v072_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v073_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v074_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_slope_v075_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v076_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v077_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_slope_v078_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v079_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v080_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_slope_v081_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v082_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v083_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_slope_v084_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v085_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v086_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_slope_v087_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v088_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v089_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_slope_v090_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v091_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v092_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_slope_v093_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v094_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v095_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_slope_v096_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v097_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v098_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_slope_v099_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v100_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v101_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_21d_slope_v102_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v103_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v104_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_63d_slope_v105_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v106_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v107_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtcum_126d_slope_v108_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v109_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v110_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_21d_slope_v111_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v112_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v113_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_63d_slope_v114_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v115_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v116_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrcum_126d_slope_v117_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v118_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v119_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_21d_slope_v120_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v121_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v122_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_63d_slope_v123_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v124_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v125_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvcum_126d_slope_v126_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v127_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v128_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_slope_v129_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v130_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v131_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_slope_v132_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v133_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v134_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_21d_slope_v135_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v136_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v137_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_63d_slope_v138_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v139_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v140_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxeq_252d_slope_v141_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v142_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v143_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_21d_slope_v144_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v145_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v146_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_63d_slope_v147_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v148_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v149_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_alt_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_HEALTHCARE_BALANCE_SHEET_STRENGTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    liabilities = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")

    cols = {
        "cashneq": cashneq,
        "closeadj": closeadj,
        "debt": debt,
        "equity": equity,
        "liabilities": liabilities,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f45_net_debt', '_f45_bs_strength', '_f45_solvency_proxy',)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f45_healthcare_balance_sheet_strength_2nd_derivatives_001_150_claude: {n_features} features pass")
