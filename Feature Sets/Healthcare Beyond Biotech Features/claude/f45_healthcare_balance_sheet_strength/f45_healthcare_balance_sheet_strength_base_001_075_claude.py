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


# ===== folder domain primitives =====
def _f45_net_debt(debt, cashneq):
    return debt - cashneq


def _f45_bs_strength(equity, debt, w):
    return _mean(equity, w) / _mean(debt, w).replace(0, np.nan)


def _f45_solvency_proxy(equity, liabilities, w):
    return _mean(equity, w) / _mean(liabilities, w).replace(0, np.nan)

# v001: netdebt_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_base_v001_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v002: netdebt_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_base_v002_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v003: netdebt_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_base_v003_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 126) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v004: netdebt_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_base_v004_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v005: netdebt_504d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_base_v005_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v006: bsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_base_v006_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: bsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_base_v007_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: bsstr_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_base_v008_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: bsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_base_v009_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: bsstr_504d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_base_v010_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: solv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_base_v011_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: solv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_base_v012_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: solv_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_base_v013_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: solv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_base_v014_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: solv_504d
def f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_base_v015_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: ndtoeq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_21d_base_v016_signal(debt, cashneq, equity, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 21) / _mean(equity, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: ndtoeq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_63d_base_v017_signal(debt, cashneq, equity, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 63) / _mean(equity, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: ndtoeq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_252d_base_v018_signal(debt, cashneq, equity, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 252) / _mean(equity, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: netdebtsq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_21d_base_v019_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 21) ** 2) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v020: netdebtsq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_63d_base_v020_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 63) ** 2) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v021: netdebtsq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_252d_base_v021_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 252) ** 2) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v022: bsstrsq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_21d_base_v022_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 21) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: bsstrsq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_63d_base_v023_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 63) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: bsstrsq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_252d_base_v024_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 252) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: solvsq_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvsq_21d_base_v025_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 21) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: solvsq_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvsq_63d_base_v026_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 63) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: solvsq_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvsq_252d_base_v027_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 252) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: netdebtz_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_21d_base_v028_signal(debt, cashneq, closeadj):
    result = _z(_mean(_f45_net_debt(debt, cashneq), 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: netdebtz_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_63d_base_v029_signal(debt, cashneq, closeadj):
    result = _z(_mean(_f45_net_debt(debt, cashneq), 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: netdebtz_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_252d_base_v030_signal(debt, cashneq, closeadj):
    result = _z(_mean(_f45_net_debt(debt, cashneq), 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: bsstrz_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_21d_base_v031_signal(equity, debt, closeadj):
    result = _z(_f45_bs_strength(equity, debt, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: bsstrz_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_63d_base_v032_signal(equity, debt, closeadj):
    result = _z(_f45_bs_strength(equity, debt, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: bsstrz_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_252d_base_v033_signal(equity, debt, closeadj):
    result = _z(_f45_bs_strength(equity, debt, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: solvz_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvz_21d_base_v034_signal(equity, liabilities, closeadj):
    result = _z(_f45_solvency_proxy(equity, liabilities, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: solvz_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvz_63d_base_v035_signal(equity, liabilities, closeadj):
    result = _z(_f45_solvency_proxy(equity, liabilities, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: solvz_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvz_252d_base_v036_signal(equity, liabilities, closeadj):
    result = _z(_f45_solvency_proxy(equity, liabilities, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: ndxbsstr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_base_v037_signal(debt, cashneq, equity, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_bs_strength(equity, debt, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v038: ndxbsstr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_base_v038_signal(debt, cashneq, equity, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_bs_strength(equity, debt, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v039: ndxbsstr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_base_v039_signal(debt, cashneq, equity, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_bs_strength(equity, debt, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v040: ndxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_base_v040_signal(debt, cashneq, equity, liabilities, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v041: ndxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_base_v041_signal(debt, cashneq, equity, liabilities, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v042: ndxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_base_v042_signal(debt, cashneq, equity, liabilities, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v043: bsstrxsolv_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_base_v043_signal(equity, debt, liabilities, closeadj):
    result = _f45_bs_strength(equity, debt, 21) * _f45_solvency_proxy(equity, liabilities, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: bsstrxsolv_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_base_v044_signal(equity, debt, liabilities, closeadj):
    result = _f45_bs_strength(equity, debt, 63) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: bsstrxsolv_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_base_v045_signal(equity, debt, liabilities, closeadj):
    result = _f45_bs_strength(equity, debt, 252) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: netdebtmean_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_21d_base_v046_signal(debt, cashneq, closeadj):
    result = _mean(_mean(_f45_net_debt(debt, cashneq), 21), 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v047: netdebtmean_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_63d_base_v047_signal(debt, cashneq, closeadj):
    result = _mean(_mean(_f45_net_debt(debt, cashneq), 63), 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v048: netdebtmean_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_126d_base_v048_signal(debt, cashneq, closeadj):
    result = _mean(_mean(_f45_net_debt(debt, cashneq), 126), 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v049: bsstrmean_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_21d_base_v049_signal(equity, debt, closeadj):
    result = _mean(_f45_bs_strength(equity, debt, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: bsstrmean_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_63d_base_v050_signal(equity, debt, closeadj):
    result = _mean(_f45_bs_strength(equity, debt, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: bsstrmean_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_126d_base_v051_signal(equity, debt, closeadj):
    result = _mean(_f45_bs_strength(equity, debt, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: solvmean_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvmean_21d_base_v052_signal(equity, liabilities, closeadj):
    result = _mean(_f45_solvency_proxy(equity, liabilities, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: solvmean_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvmean_63d_base_v053_signal(equity, liabilities, closeadj):
    result = _mean(_f45_solvency_proxy(equity, liabilities, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: solvmean_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvmean_126d_base_v054_signal(equity, liabilities, closeadj):
    result = _mean(_f45_solvency_proxy(equity, liabilities, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: netdebtstd_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_21d_base_v055_signal(debt, cashneq, closeadj):
    result = _std(_mean(_f45_net_debt(debt, cashneq), 21), 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v056: netdebtstd_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_63d_base_v056_signal(debt, cashneq, closeadj):
    result = _std(_mean(_f45_net_debt(debt, cashneq), 63), 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v057: netdebtstd_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_126d_base_v057_signal(debt, cashneq, closeadj):
    result = _std(_mean(_f45_net_debt(debt, cashneq), 126), 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v058: bsstrstd_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_21d_base_v058_signal(equity, debt, closeadj):
    result = _std(_f45_bs_strength(equity, debt, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: bsstrstd_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_63d_base_v059_signal(equity, debt, closeadj):
    result = _std(_f45_bs_strength(equity, debt, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: bsstrstd_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_126d_base_v060_signal(equity, debt, closeadj):
    result = _std(_f45_bs_strength(equity, debt, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: solvstd_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvstd_21d_base_v061_signal(equity, liabilities, closeadj):
    result = _std(_f45_solvency_proxy(equity, liabilities, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: solvstd_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvstd_63d_base_v062_signal(equity, liabilities, closeadj):
    result = _std(_f45_solvency_proxy(equity, liabilities, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: solvstd_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvstd_126d_base_v063_signal(equity, liabilities, closeadj):
    result = _std(_f45_solvency_proxy(equity, liabilities, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: netdebtema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_base_v064_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 11).ewm(span=21, adjust=False).mean() * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v065: netdebtema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_base_v065_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 32).ewm(span=63, adjust=False).mean() * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v066: netdebtema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_base_v066_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 127).ewm(span=252, adjust=False).mean() * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v067: bsstrema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_base_v067_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: bsstrema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_base_v068_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: bsstrema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_base_v069_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: solvema_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_base_v070_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: solvema_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_base_v071_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: solvema_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_base_v072_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: netdebtqr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_21d_base_v073_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: netdebtqr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_63d_base_v074_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: netdebtqr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_252d_base_v075_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_21d_base_v001_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_63d_base_v002_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_126d_base_v003_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_252d_base_v004_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_504d_base_v005_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_21d_base_v006_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_63d_base_v007_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_126d_base_v008_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_252d_base_v009_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_504d_base_v010_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_21d_base_v011_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_63d_base_v012_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_126d_base_v013_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_252d_base_v014_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_504d_base_v015_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_21d_base_v016_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_63d_base_v017_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndtoeq_252d_base_v018_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_21d_base_v019_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_63d_base_v020_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtsq_252d_base_v021_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_21d_base_v022_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_63d_base_v023_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrsq_252d_base_v024_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvsq_21d_base_v025_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvsq_63d_base_v026_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvsq_252d_base_v027_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_21d_base_v028_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_63d_base_v029_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtz_252d_base_v030_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_21d_base_v031_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_63d_base_v032_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrz_252d_base_v033_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvz_21d_base_v034_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvz_63d_base_v035_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvz_252d_base_v036_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_21d_base_v037_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_63d_base_v038_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxbsstr_252d_base_v039_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_21d_base_v040_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_63d_base_v041_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_ndxsolv_252d_base_v042_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_21d_base_v043_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_63d_base_v044_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxsolv_252d_base_v045_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_21d_base_v046_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_63d_base_v047_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtmean_126d_base_v048_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_21d_base_v049_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_63d_base_v050_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrmean_126d_base_v051_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvmean_21d_base_v052_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvmean_63d_base_v053_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvmean_126d_base_v054_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_21d_base_v055_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_63d_base_v056_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtstd_126d_base_v057_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_21d_base_v058_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_63d_base_v059_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrstd_126d_base_v060_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvstd_21d_base_v061_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvstd_63d_base_v062_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvstd_126d_base_v063_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_21d_base_v064_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_63d_base_v065_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtema_252d_base_v066_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_21d_base_v067_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_63d_base_v068_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrema_252d_base_v069_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_21d_base_v070_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_63d_base_v071_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvema_252d_base_v072_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_21d_base_v073_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_63d_base_v074_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtqr_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_HEALTHCARE_BALANCE_SHEET_STRENGTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f45_healthcare_balance_sheet_strength_base_001_075_claude: {n_features} features pass")
