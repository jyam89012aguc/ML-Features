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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()

# ===== folder domain primitives =====
def _f45_net_debt(debt, cashneq):
    return (debt - cashneq) / (debt + cashneq).replace(0, np.nan).abs()


def _f45_bs_strength(equity, debt, w):
    s = equity / (equity + debt).replace(0, np.nan).abs()
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _f45_solvency_proxy(equity, liabilities, w):
    p = equity / liabilities.replace(0, np.nan).abs()
    return p.rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====
def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc_base_v001_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc2_base_v002_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_logc_base_v003_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 5) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc_rmean_base_v004_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 5) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc_base_v005_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc2_base_v006_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_logc_base_v007_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 10) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc_rmean_base_v008_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 10) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc_base_v009_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc2_base_v010_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_logc_base_v011_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 21) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc_rmean_base_v012_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 21) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc_base_v013_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc2_base_v014_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_logc_base_v015_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 42) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc_rmean_base_v016_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 42) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc_base_v017_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc2_base_v018_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_logc_base_v019_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 63) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc_rmean_base_v020_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 63) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc_base_v021_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc2_base_v022_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_logc_base_v023_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 126) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc_rmean_base_v024_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 126) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc_base_v025_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc2_base_v026_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_logc_base_v027_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 189) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc_rmean_base_v028_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 189) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc_base_v029_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc2_base_v030_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_logc_base_v031_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 252) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc_rmean_base_v032_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 252) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc_base_v033_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc2_base_v034_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_logc_base_v035_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 378) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc_rmean_base_v036_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 378) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc_base_v037_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc2_base_v038_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_logc_base_v039_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 504) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc_rmean_base_v040_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _mean(base, 504) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc_base_v041_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc2_base_v042_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_logc_base_v043_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 5) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc_rmean_base_v044_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 5) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc_base_v045_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc2_base_v046_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_logc_base_v047_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 10) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc_rmean_base_v048_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 10) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc_base_v049_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc2_base_v050_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_logc_base_v051_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 21) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc_rmean_base_v052_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 21) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc_base_v053_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc2_base_v054_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_logc_base_v055_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 42) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc_rmean_base_v056_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 42) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc_base_v057_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc2_base_v058_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_logc_base_v059_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 63) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc_rmean_base_v060_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 63) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc_base_v061_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc2_base_v062_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_logc_base_v063_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 126) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc_rmean_base_v064_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 126) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc_base_v065_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc2_base_v066_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_logc_base_v067_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 189) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc_rmean_base_v068_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 189) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc_base_v069_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc2_base_v070_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_logc_base_v071_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 252) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc_rmean_base_v072_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 252) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_xc_base_v073_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_xc2_base_v074_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_logc_base_v075_signal(debt, cashneq, closeadj):
    base = _f45_net_debt(debt, cashneq)
    result = _std(base, 378) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc_base_v001_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc2_base_v002_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_logc_base_v003_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_mean_xc_rmean_base_v004_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc_base_v005_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc2_base_v006_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_logc_base_v007_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_mean_xc_rmean_base_v008_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc_base_v009_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc2_base_v010_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_logc_base_v011_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_mean_xc_rmean_base_v012_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc_base_v013_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc2_base_v014_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_logc_base_v015_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_mean_xc_rmean_base_v016_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc_base_v017_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc2_base_v018_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_logc_base_v019_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_mean_xc_rmean_base_v020_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc_base_v021_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc2_base_v022_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_logc_base_v023_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_mean_xc_rmean_base_v024_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc_base_v025_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc2_base_v026_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_logc_base_v027_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_mean_xc_rmean_base_v028_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc_base_v029_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc2_base_v030_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_logc_base_v031_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_mean_xc_rmean_base_v032_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc_base_v033_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc2_base_v034_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_logc_base_v035_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_mean_xc_rmean_base_v036_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc_base_v037_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc2_base_v038_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_logc_base_v039_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t504_mean_xc_rmean_base_v040_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc_base_v041_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc2_base_v042_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_logc_base_v043_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t5_std_xc_rmean_base_v044_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc_base_v045_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc2_base_v046_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_logc_base_v047_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t10_std_xc_rmean_base_v048_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc_base_v049_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc2_base_v050_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_logc_base_v051_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t21_std_xc_rmean_base_v052_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc_base_v053_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc2_base_v054_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_logc_base_v055_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t42_std_xc_rmean_base_v056_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc_base_v057_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc2_base_v058_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_logc_base_v059_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t63_std_xc_rmean_base_v060_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc_base_v061_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc2_base_v062_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_logc_base_v063_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t126_std_xc_rmean_base_v064_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc_base_v065_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc2_base_v066_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_logc_base_v067_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t189_std_xc_rmean_base_v068_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc_base_v069_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc2_base_v070_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_logc_base_v071_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t252_std_xc_rmean_base_v072_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_xc_base_v073_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_xc2_base_v074_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_t378_std_logc_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_ENERGY_BALANCE_SHEET_STRENGTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor,
        "assets": assets, "liabilities": liabilities, "equity": equity,
        "debt": debt, "cashneq": cashneq, "ppnenet": ppnenet,
        "marketcap": marketcap, "ev": ev,
        "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f45_net_debt", "_f45_bs_strength", "_f45_solvency_proxy")
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
    print(f"OK f45_energy_balance_sheet_strength_base_001_075_claude: {n_features} features pass")
