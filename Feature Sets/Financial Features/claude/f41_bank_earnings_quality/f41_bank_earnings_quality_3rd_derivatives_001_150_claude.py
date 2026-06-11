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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f41_accrual_to_cash(netinc, ncfo, w):
    """Accrual ratio: (netinc - ncfo) / mean(|netinc|+|ncfo|). Lower = higher quality."""
    diff = netinc - ncfo
    denom = (netinc.abs() + ncfo.abs()).rolling(w, min_periods=max(1, w // 2)).mean()
    return diff / denom.replace(0, np.nan)


def _f41_earnings_quality(netinc, ncfo, w):
    """Earnings quality = ncfo / netinc smoothed over w."""
    qm = (ncfo.rolling(w, min_periods=max(1, w // 2)).mean()
          / netinc.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))
    return qm


def _f41_cash_earnings_proxy(ncfo, netinc, w):
    """Cash earnings proxy: rolling mean of ncfo, anchored against netinc level."""
    return (ncfo.rolling(w, min_periods=max(1, w // 2)).mean()
            - 0.5 * netinc.rolling(w, min_periods=max(1, w // 2)).mean())

def f41beq_f41_bank_earnings_quality_acc_x_close_5d_i5d_jerk_v001_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i5d_jerk_v002_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i5d_jerk_v003_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i5d_jerk_v004_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 21)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i5d_jerk_v005_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 63)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i5d_jerk_v006_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i5d_jerk_v007_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i5d_jerk_v008_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i5d_jerk_v009_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i5d_jerk_v010_signal(netinc, ncfo, closeadj):
    base = _z(_f41_accrual_to_cash(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i5d_jerk_v011_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_5d_i5d_jerk_v012_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i5d_jerk_v013_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * np.sqrt(closeadj.abs())
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i5d_jerk_v014_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(5)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i5d_jerk_v015_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(63)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i5d_jerk_v016_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i5d_jerk_v017_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i5d_jerk_v018_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i5d_jerk_v019_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i5d_jerk_v020_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i5d_jerk_v021_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i5d_jerk_v022_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i5d_jerk_v023_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_5d_i5d_jerk_v024_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i5d_jerk_v025_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * np.log(closeadj.abs() + 1.0) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean21_5d_i5d_jerk_v026_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean63_5d_i5d_jerk_v027_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_std21_5d_i5d_jerk_v028_signal(netinc, ncfo, closeadj):
    base = _std(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z63_5d_i5d_jerk_v029_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z252_5d_i5d_jerk_v030_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_ema21_5d_i5d_jerk_v031_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i5d_jerk_v032_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj * closeadj.pct_change(21) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i5d_jerk_v033_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i5d_jerk_v034_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * b * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i5d_jerk_v035_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * closeadj / b.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i5d_jerk_v036_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(21)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i5d_jerk_v037_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(63)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i5d_jerk_v038_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * revenue.pct_change(21) * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i5d_jerk_v039_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    rg = revenue.pct_change(5)
    base_series = (base - rg) * closeadj
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i5d_jerk_v040_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = np.sign(base) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i5d_jerk_v041_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = np.sign(base - 1.0) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_5d_i10d_jerk_v042_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i10d_jerk_v043_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i10d_jerk_v044_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i10d_jerk_v045_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 21)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i10d_jerk_v046_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 63)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i10d_jerk_v047_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i10d_jerk_v048_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i10d_jerk_v049_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i10d_jerk_v050_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i10d_jerk_v051_signal(netinc, ncfo, closeadj):
    base = _z(_f41_accrual_to_cash(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i10d_jerk_v052_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_5d_i10d_jerk_v053_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i10d_jerk_v054_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * np.sqrt(closeadj.abs())
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i10d_jerk_v055_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(5)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i10d_jerk_v056_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(63)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i10d_jerk_v057_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i10d_jerk_v058_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i10d_jerk_v059_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i10d_jerk_v060_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i10d_jerk_v061_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i10d_jerk_v062_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i10d_jerk_v063_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i10d_jerk_v064_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_5d_i10d_jerk_v065_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i10d_jerk_v066_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * np.log(closeadj.abs() + 1.0) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean21_5d_i10d_jerk_v067_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean63_5d_i10d_jerk_v068_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_std21_5d_i10d_jerk_v069_signal(netinc, ncfo, closeadj):
    base = _std(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z63_5d_i10d_jerk_v070_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z252_5d_i10d_jerk_v071_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_ema21_5d_i10d_jerk_v072_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i10d_jerk_v073_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj * closeadj.pct_change(21) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i10d_jerk_v074_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i10d_jerk_v075_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * b * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i10d_jerk_v076_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * closeadj / b.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i10d_jerk_v077_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(21)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i10d_jerk_v078_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(63)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i10d_jerk_v079_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * revenue.pct_change(21) * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i10d_jerk_v080_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    rg = revenue.pct_change(5)
    base_series = (base - rg) * closeadj
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i10d_jerk_v081_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = np.sign(base) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i10d_jerk_v082_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = np.sign(base - 1.0) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_5d_i21d_jerk_v083_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i21d_jerk_v084_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i21d_jerk_v085_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i21d_jerk_v086_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 21)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i21d_jerk_v087_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 63)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i21d_jerk_v088_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i21d_jerk_v089_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i21d_jerk_v090_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i21d_jerk_v091_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i21d_jerk_v092_signal(netinc, ncfo, closeadj):
    base = _z(_f41_accrual_to_cash(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i21d_jerk_v093_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_5d_i21d_jerk_v094_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i21d_jerk_v095_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * np.sqrt(closeadj.abs())
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i21d_jerk_v096_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(5)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i21d_jerk_v097_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(63)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i21d_jerk_v098_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i21d_jerk_v099_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i21d_jerk_v100_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i21d_jerk_v101_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i21d_jerk_v102_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i21d_jerk_v103_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i21d_jerk_v104_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i21d_jerk_v105_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_5d_i21d_jerk_v106_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i21d_jerk_v107_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * np.log(closeadj.abs() + 1.0) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean21_5d_i21d_jerk_v108_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean63_5d_i21d_jerk_v109_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_std21_5d_i21d_jerk_v110_signal(netinc, ncfo, closeadj):
    base = _std(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z63_5d_i21d_jerk_v111_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_z252_5d_i21d_jerk_v112_signal(netinc, ncfo, closeadj):
    base = _z(_f41_cash_earnings_proxy(ncfo, netinc, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_ema21_5d_i21d_jerk_v113_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i21d_jerk_v114_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj * closeadj.pct_change(21) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i21d_jerk_v115_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i21d_jerk_v116_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * b * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i21d_jerk_v117_signal(netinc, ncfo, closeadj):
    a = _f41_accrual_to_cash(netinc, ncfo, 5)
    b = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = a * closeadj / b.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i21d_jerk_v118_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(21)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i21d_jerk_v119_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * revenue.pct_change(63)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i21d_jerk_v120_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * revenue.pct_change(21) * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i21d_jerk_v121_signal(netinc, ncfo, revenue, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    rg = revenue.pct_change(5)
    base_series = (base - rg) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i21d_jerk_v122_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = np.sign(base) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i21d_jerk_v123_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = np.sign(base - 1.0) * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_5d_i42d_jerk_v124_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i42d_jerk_v125_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i42d_jerk_v126_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(21)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i42d_jerk_v127_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 21)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i42d_jerk_v128_signal(netinc, ncfo, closeadj):
    base = _f41_accrual_to_cash(netinc, ncfo, 5)
    base_series = base * closeadj * _z(closeadj, 63)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i42d_jerk_v129_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i42d_jerk_v130_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i42d_jerk_v131_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i42d_jerk_v132_signal(netinc, ncfo, closeadj):
    base = _std(_f41_accrual_to_cash(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i42d_jerk_v133_signal(netinc, ncfo, closeadj):
    base = _z(_f41_accrual_to_cash(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i42d_jerk_v134_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_accrual_to_cash(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_5d_i42d_jerk_v135_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i42d_jerk_v136_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * np.sqrt(closeadj.abs())
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i42d_jerk_v137_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(5)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i42d_jerk_v138_signal(netinc, ncfo, closeadj):
    base = _f41_earnings_quality(netinc, ncfo, 5)
    base_series = base * closeadj * closeadj.pct_change(63)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i42d_jerk_v139_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i42d_jerk_v140_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i42d_jerk_v141_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i42d_jerk_v142_signal(netinc, ncfo, closeadj):
    base = _std(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i42d_jerk_v143_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i42d_jerk_v144_signal(netinc, ncfo, closeadj):
    base = _z(_f41_earnings_quality(netinc, ncfo, 5), 252)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i42d_jerk_v145_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 21)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i42d_jerk_v146_signal(netinc, ncfo, closeadj):
    base = _ema(_f41_earnings_quality(netinc, ncfo, 5), 63)
    base_series = base * closeadj
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_5d_i42d_jerk_v147_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i42d_jerk_v148_signal(netinc, ncfo, closeadj):
    base = _f41_cash_earnings_proxy(ncfo, netinc, 5)
    base_series = base * np.log(closeadj.abs() + 1.0) / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean21_5d_i42d_jerk_v149_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 21)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41beq_f41_bank_earnings_quality_cep_mean63_5d_i42d_jerk_v150_signal(netinc, ncfo, closeadj):
    base = _mean(_f41_cash_earnings_proxy(ncfo, netinc, 5), 63)
    base_series = base * closeadj / netinc.abs().replace(0, np.nan)
    result = _jerk(base_series, 42)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f41beq_f41_bank_earnings_quality_acc_x_close_5d_i5d_jerk_v001_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i5d_jerk_v002_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i5d_jerk_v003_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i5d_jerk_v004_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i5d_jerk_v005_signal,
    f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i5d_jerk_v006_signal,
    f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i5d_jerk_v007_signal,
    f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i5d_jerk_v008_signal,
    f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i5d_jerk_v009_signal,
    f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i5d_jerk_v010_signal,
    f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i5d_jerk_v011_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_5d_i5d_jerk_v012_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i5d_jerk_v013_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i5d_jerk_v014_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i5d_jerk_v015_signal,
    f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i5d_jerk_v016_signal,
    f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i5d_jerk_v017_signal,
    f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i5d_jerk_v018_signal,
    f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i5d_jerk_v019_signal,
    f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i5d_jerk_v020_signal,
    f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i5d_jerk_v021_signal,
    f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i5d_jerk_v022_signal,
    f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i5d_jerk_v023_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_5d_i5d_jerk_v024_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i5d_jerk_v025_signal,
    f41beq_f41_bank_earnings_quality_cep_mean21_5d_i5d_jerk_v026_signal,
    f41beq_f41_bank_earnings_quality_cep_mean63_5d_i5d_jerk_v027_signal,
    f41beq_f41_bank_earnings_quality_cep_std21_5d_i5d_jerk_v028_signal,
    f41beq_f41_bank_earnings_quality_cep_z63_5d_i5d_jerk_v029_signal,
    f41beq_f41_bank_earnings_quality_cep_z252_5d_i5d_jerk_v030_signal,
    f41beq_f41_bank_earnings_quality_cep_ema21_5d_i5d_jerk_v031_signal,
    f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i5d_jerk_v032_signal,
    f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i5d_jerk_v033_signal,
    f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i5d_jerk_v034_signal,
    f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i5d_jerk_v035_signal,
    f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i5d_jerk_v036_signal,
    f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i5d_jerk_v037_signal,
    f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i5d_jerk_v038_signal,
    f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i5d_jerk_v039_signal,
    f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i5d_jerk_v040_signal,
    f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i5d_jerk_v041_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_5d_i10d_jerk_v042_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i10d_jerk_v043_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i10d_jerk_v044_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i10d_jerk_v045_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i10d_jerk_v046_signal,
    f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i10d_jerk_v047_signal,
    f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i10d_jerk_v048_signal,
    f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i10d_jerk_v049_signal,
    f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i10d_jerk_v050_signal,
    f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i10d_jerk_v051_signal,
    f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i10d_jerk_v052_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_5d_i10d_jerk_v053_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i10d_jerk_v054_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i10d_jerk_v055_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i10d_jerk_v056_signal,
    f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i10d_jerk_v057_signal,
    f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i10d_jerk_v058_signal,
    f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i10d_jerk_v059_signal,
    f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i10d_jerk_v060_signal,
    f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i10d_jerk_v061_signal,
    f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i10d_jerk_v062_signal,
    f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i10d_jerk_v063_signal,
    f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i10d_jerk_v064_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_5d_i10d_jerk_v065_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i10d_jerk_v066_signal,
    f41beq_f41_bank_earnings_quality_cep_mean21_5d_i10d_jerk_v067_signal,
    f41beq_f41_bank_earnings_quality_cep_mean63_5d_i10d_jerk_v068_signal,
    f41beq_f41_bank_earnings_quality_cep_std21_5d_i10d_jerk_v069_signal,
    f41beq_f41_bank_earnings_quality_cep_z63_5d_i10d_jerk_v070_signal,
    f41beq_f41_bank_earnings_quality_cep_z252_5d_i10d_jerk_v071_signal,
    f41beq_f41_bank_earnings_quality_cep_ema21_5d_i10d_jerk_v072_signal,
    f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i10d_jerk_v073_signal,
    f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i10d_jerk_v074_signal,
    f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i10d_jerk_v075_signal,
    f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i10d_jerk_v076_signal,
    f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i10d_jerk_v077_signal,
    f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i10d_jerk_v078_signal,
    f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i10d_jerk_v079_signal,
    f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i10d_jerk_v080_signal,
    f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i10d_jerk_v081_signal,
    f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i10d_jerk_v082_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_5d_i21d_jerk_v083_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i21d_jerk_v084_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i21d_jerk_v085_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i21d_jerk_v086_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i21d_jerk_v087_signal,
    f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i21d_jerk_v088_signal,
    f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i21d_jerk_v089_signal,
    f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i21d_jerk_v090_signal,
    f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i21d_jerk_v091_signal,
    f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i21d_jerk_v092_signal,
    f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i21d_jerk_v093_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_5d_i21d_jerk_v094_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i21d_jerk_v095_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i21d_jerk_v096_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i21d_jerk_v097_signal,
    f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i21d_jerk_v098_signal,
    f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i21d_jerk_v099_signal,
    f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i21d_jerk_v100_signal,
    f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i21d_jerk_v101_signal,
    f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i21d_jerk_v102_signal,
    f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i21d_jerk_v103_signal,
    f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i21d_jerk_v104_signal,
    f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i21d_jerk_v105_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_5d_i21d_jerk_v106_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i21d_jerk_v107_signal,
    f41beq_f41_bank_earnings_quality_cep_mean21_5d_i21d_jerk_v108_signal,
    f41beq_f41_bank_earnings_quality_cep_mean63_5d_i21d_jerk_v109_signal,
    f41beq_f41_bank_earnings_quality_cep_std21_5d_i21d_jerk_v110_signal,
    f41beq_f41_bank_earnings_quality_cep_z63_5d_i21d_jerk_v111_signal,
    f41beq_f41_bank_earnings_quality_cep_z252_5d_i21d_jerk_v112_signal,
    f41beq_f41_bank_earnings_quality_cep_ema21_5d_i21d_jerk_v113_signal,
    f41beq_f41_bank_earnings_quality_cep_pct21_close_5d_i21d_jerk_v114_signal,
    f41beq_f41_bank_earnings_quality_acc_minus_eq_5d_i21d_jerk_v115_signal,
    f41beq_f41_bank_earnings_quality_acc_times_eq_5d_i21d_jerk_v116_signal,
    f41beq_f41_bank_earnings_quality_acc_over_eq_5d_i21d_jerk_v117_signal,
    f41beq_f41_bank_earnings_quality_eq_x_revenue_5d_i21d_jerk_v118_signal,
    f41beq_f41_bank_earnings_quality_acc_x_revenue_5d_i21d_jerk_v119_signal,
    f41beq_f41_bank_earnings_quality_cep_x_revenue_5d_i21d_jerk_v120_signal,
    f41beq_f41_bank_earnings_quality_eq_minus_revgrowth_5d_i21d_jerk_v121_signal,
    f41beq_f41_bank_earnings_quality_acc_sign_close_5d_i21d_jerk_v122_signal,
    f41beq_f41_bank_earnings_quality_eq_sign_close_5d_i21d_jerk_v123_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_5d_i42d_jerk_v124_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_sq_5d_i42d_jerk_v125_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_pct21_5d_i42d_jerk_v126_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z21_5d_i42d_jerk_v127_signal,
    f41beq_f41_bank_earnings_quality_acc_x_close_z63_5d_i42d_jerk_v128_signal,
    f41beq_f41_bank_earnings_quality_acc_mean21_close_5d_i42d_jerk_v129_signal,
    f41beq_f41_bank_earnings_quality_acc_mean63_close_5d_i42d_jerk_v130_signal,
    f41beq_f41_bank_earnings_quality_acc_std21_close_5d_i42d_jerk_v131_signal,
    f41beq_f41_bank_earnings_quality_acc_std63_close_5d_i42d_jerk_v132_signal,
    f41beq_f41_bank_earnings_quality_acc_z252_close_5d_i42d_jerk_v133_signal,
    f41beq_f41_bank_earnings_quality_acc_ema21_close_5d_i42d_jerk_v134_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_5d_i42d_jerk_v135_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_sqrt_5d_i42d_jerk_v136_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct5_5d_i42d_jerk_v137_signal,
    f41beq_f41_bank_earnings_quality_eq_x_close_pct63_5d_i42d_jerk_v138_signal,
    f41beq_f41_bank_earnings_quality_eq_mean21_close_5d_i42d_jerk_v139_signal,
    f41beq_f41_bank_earnings_quality_eq_mean63_close_5d_i42d_jerk_v140_signal,
    f41beq_f41_bank_earnings_quality_eq_std21_close_5d_i42d_jerk_v141_signal,
    f41beq_f41_bank_earnings_quality_eq_std63_close_5d_i42d_jerk_v142_signal,
    f41beq_f41_bank_earnings_quality_eq_z63_close_5d_i42d_jerk_v143_signal,
    f41beq_f41_bank_earnings_quality_eq_z252_close_5d_i42d_jerk_v144_signal,
    f41beq_f41_bank_earnings_quality_eq_ema21_close_5d_i42d_jerk_v145_signal,
    f41beq_f41_bank_earnings_quality_eq_ema63_close_5d_i42d_jerk_v146_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_5d_i42d_jerk_v147_signal,
    f41beq_f41_bank_earnings_quality_cep_x_close_log_5d_i42d_jerk_v148_signal,
    f41beq_f41_bank_earnings_quality_cep_mean21_5d_i42d_jerk_v149_signal,
    f41beq_f41_bank_earnings_quality_cep_mean63_5d_i42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_BANK_EARNINGS_QUALITY_REGISTRY_JERK_001_150 = REGISTRY

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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f41_accrual_to_cash', '_f41_earnings_quality', '_f41_cash_earnings_proxy')
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
    print(f"OK f41_bank_earnings_quality_3rd_derivatives_001_150_claude: {n_features} features pass")
