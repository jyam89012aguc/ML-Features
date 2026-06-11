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

# ===== folder domain primitives =====
def _f44_accrual_to_cash(netinc, ncfo, w):
    acc = (netinc - ncfo) / ncfo.replace(0, np.nan).abs()
    return acc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_earnings_quality(netinc, ncfo, w):
    q = ncfo / netinc.replace(0, np.nan).abs()
    return q.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_cash_earnings_proxy(ncfo, ebitda, w):
    proxy = ncfo / ebitda.replace(0, np.nan).abs()
    return proxy.rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====
def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v001_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v002_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v003_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v004_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v005_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v006_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v007_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v008_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v009_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v010_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v011_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v012_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v013_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v014_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v015_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v016_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v017_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v018_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v019_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v020_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v021_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v022_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v023_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v024_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v025_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v026_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v027_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v028_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v029_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v030_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v031_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v032_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v033_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v034_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v035_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v036_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v037_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v038_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v039_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v040_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v041_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v042_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v043_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v044_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v045_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v046_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v047_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v048_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v049_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v050_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v051_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v052_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v053_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v054_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v055_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v056_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v057_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v058_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v059_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v060_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v061_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v062_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v063_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v064_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v065_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v066_signal(netinc, ncfo, closeadj):
    base = _z((_f44_accrual_to_cash(netinc, ncfo, 5)), 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v067_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v068_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v069_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v070_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v071_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v072_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v073_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v074_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v075_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v076_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v077_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v078_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5))**2) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v079_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v080_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v081_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v082_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v083_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v084_signal(netinc, ncfo, closeadj):
    base = _ema(_mean((_f44_accrual_to_cash(netinc, ncfo, 5)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v085_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v086_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v087_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v088_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v089_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v090_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 5)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v091_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v092_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v093_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v094_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v095_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v096_signal(netinc, ncfo, closeadj):
    base = ((_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).max() - (_f44_accrual_to_cash(netinc, ncfo, 5)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v097_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v098_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v099_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v100_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v101_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v102_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v103_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v104_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v105_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v106_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v107_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v108_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v109_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v110_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v111_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v112_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v113_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v114_signal(netinc, ncfo, closeadj):
    base = (_f44_accrual_to_cash(netinc, ncfo, 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v115_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v116_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v117_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v118_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v119_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v120_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v121_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v122_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v123_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v124_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v125_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v126_signal(netinc, ncfo, closeadj):
    base = _mean((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v127_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v128_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v129_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v130_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v131_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v132_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v133_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v134_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v135_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v136_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v137_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v138_signal(netinc, ncfo, closeadj):
    base = _ema((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v139_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v140_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v141_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v142_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v143_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v144_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v145_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v146_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v147_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v148_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v149_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v150_signal(netinc, ncfo, closeadj):
    base = _std((_f44_accrual_to_cash(netinc, ncfo, 10)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v001_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v002_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v003_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v004_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v005_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_raw_slope_v006_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v007_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v008_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v009_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v010_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v011_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc_slope_v012_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v013_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v014_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v015_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v016_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v017_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_xc2_slope_v018_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v019_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v020_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v021_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v022_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v023_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean21_slope_v024_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v025_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v026_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v027_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v028_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v029_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_mean63_slope_v030_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v031_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v032_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v033_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v034_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v035_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema21_slope_v036_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v037_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v038_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v039_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v040_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v041_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_ema63_slope_v042_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v043_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v044_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v045_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v046_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v047_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std21_slope_v048_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v049_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v050_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v051_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v052_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v053_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_std63_slope_v054_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v055_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v056_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v057_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v058_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v059_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z63_slope_v060_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v061_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v062_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v063_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v064_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v065_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_z126_slope_v066_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v067_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v068_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v069_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v070_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v071_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_abs_xc_slope_v072_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v073_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v074_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v075_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v076_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v077_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_sq_xc_slope_v078_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v079_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v080_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v081_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v082_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v083_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_emamean21_slope_v084_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v085_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v086_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v087_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v088_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v089_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_logc_slope_v090_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v091_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v092_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v093_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v094_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v095_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_5d_rngxc_slope_v096_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v097_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v098_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v099_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v100_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v101_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_raw_slope_v102_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v103_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v104_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v105_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v106_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v107_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc_slope_v108_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v109_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v110_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v111_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v112_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v113_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_xc2_slope_v114_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v115_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v116_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v117_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v118_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v119_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean21_slope_v120_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v121_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v122_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v123_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v124_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v125_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_mean63_slope_v126_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v127_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v128_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v129_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v130_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v131_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema21_slope_v132_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v133_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v134_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v135_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v136_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v137_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_ema63_slope_v138_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v139_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v140_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v141_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v142_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v143_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std21_slope_v144_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v145_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v146_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v147_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v148_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v149_signal,
    f44eeq_f44_energy_earnings_quality_accrual_to_cash_10d_std63_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_ENERGY_EARNINGS_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f44_accrual_to_cash", "_f44_earnings_quality", "_f44_cash_earnings_proxy")
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
    print(f"OK f44_energy_earnings_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
