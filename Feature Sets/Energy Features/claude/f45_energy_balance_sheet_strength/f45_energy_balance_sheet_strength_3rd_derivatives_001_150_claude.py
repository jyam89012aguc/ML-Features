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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

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
def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v001_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v002_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v003_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v004_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v005_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v006_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v007_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v008_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v009_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v010_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v011_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v012_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v013_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v014_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v015_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v016_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v017_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v018_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v019_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v020_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v021_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v022_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v023_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v024_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v025_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v026_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v027_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v028_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v029_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v030_signal(debt, cashneq, closeadj):
    base = _mean((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v031_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v032_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v033_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v034_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v035_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v036_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v037_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v038_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v039_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v040_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v041_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v042_signal(debt, cashneq, closeadj):
    base = _ema((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v043_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v044_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v045_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v046_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v047_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v048_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v049_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v050_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v051_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v052_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v053_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v054_signal(debt, cashneq, closeadj):
    base = _std((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v055_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v056_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v057_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v058_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v059_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v060_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v061_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v062_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v063_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v064_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v065_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v066_signal(debt, cashneq, closeadj):
    base = _z((_f45_net_debt(debt, cashneq)), 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v067_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v068_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v069_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v070_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v071_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v072_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v073_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v074_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v075_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v076_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v077_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v078_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq))**2) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v079_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v080_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v081_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v082_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v083_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v084_signal(debt, cashneq, closeadj):
    base = _ema(_mean((_f45_net_debt(debt, cashneq)), 21), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v085_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v086_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v087_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v088_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v089_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v090_signal(debt, cashneq, closeadj):
    base = (_f45_net_debt(debt, cashneq)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v091_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v092_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v093_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v094_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v095_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v096_signal(debt, cashneq, closeadj):
    base = ((_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).max() - (_f45_net_debt(debt, cashneq)).rolling(21, min_periods=10).min()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v097_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v098_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v099_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v100_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v101_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v102_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v103_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v104_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v105_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v106_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v107_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v108_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v109_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v110_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v111_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v112_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v113_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v114_signal(equity, debt, closeadj):
    base = (_f45_bs_strength(equity, debt, 5)) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v115_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v116_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v117_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v118_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v119_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v120_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v121_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v122_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v123_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v124_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v125_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v126_signal(equity, debt, closeadj):
    base = _mean((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v127_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v128_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v129_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v130_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v131_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v132_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v133_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v134_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v135_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v136_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v137_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v138_signal(equity, debt, closeadj):
    base = _ema((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v139_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v140_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v141_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v142_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v143_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v144_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v145_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v146_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v147_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v148_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v149_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v150_signal(equity, debt, closeadj):
    base = _std((_f45_bs_strength(equity, debt, 5)), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v001_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v002_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v003_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v004_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v005_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_raw_jerk_v006_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v007_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v008_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v009_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v010_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v011_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc_jerk_v012_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v013_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v014_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v015_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v016_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v017_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_xc2_jerk_v018_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v019_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v020_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v021_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v022_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v023_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean21_jerk_v024_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v025_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v026_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v027_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v028_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v029_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_mean63_jerk_v030_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v031_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v032_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v033_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v034_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v035_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema21_jerk_v036_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v037_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v038_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v039_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v040_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v041_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_ema63_jerk_v042_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v043_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v044_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v045_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v046_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v047_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std21_jerk_v048_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v049_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v050_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v051_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v052_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v053_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_std63_jerk_v054_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v055_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v056_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v057_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v058_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v059_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z63_jerk_v060_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v061_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v062_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v063_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v064_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v065_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_z126_jerk_v066_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v067_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v068_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v069_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v070_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v071_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_abs_xc_jerk_v072_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v073_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v074_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v075_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v076_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v077_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_sq_xc_jerk_v078_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v079_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v080_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v081_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v082_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v083_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_emamean21_jerk_v084_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v085_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v086_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v087_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v088_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v089_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_logc_jerk_v090_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v091_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v092_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v093_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v094_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v095_signal,
    f45ebss_f45_energy_balance_sheet_strength_net_debt_x_rngxc_jerk_v096_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v097_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v098_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v099_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v100_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v101_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_raw_jerk_v102_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v103_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v104_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v105_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v106_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v107_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc_jerk_v108_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v109_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v110_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v111_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v112_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v113_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_xc2_jerk_v114_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v115_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v116_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v117_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v118_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v119_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean21_jerk_v120_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v121_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v122_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v123_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v124_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v125_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_mean63_jerk_v126_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v127_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v128_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v129_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v130_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v131_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema21_jerk_v132_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v133_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v134_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v135_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v136_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v137_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_ema63_jerk_v138_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v139_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v140_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v141_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v142_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v143_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std21_jerk_v144_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v145_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v146_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v147_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v148_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v149_signal,
    f45ebss_f45_energy_balance_sheet_strength_bs_strength_5d_std63_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_ENERGY_BALANCE_SHEET_STRENGTH_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f45_energy_balance_sheet_strength_3rd_derivatives_001_150_claude: {n_features} features pass")
