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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f083_burn_rate(fcf, w):
    # cash use intensity: rolling absolute change in fcf magnitude (covers both positive and negative fcf regimes)
    return fcf.diff().abs().rolling(w, min_periods=max(1, w // 2)).mean()


def _f083_runway_months(cashneq, fcf, w):
    # months of liquidity left given current burn (absolute fcf magnitude as proxy)
    burn = fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return cashneq / burn.replace(0, np.nan)


def _f083_runway_quality(cashneq, fcf, revenue, w):
    burn = fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    rev_mean = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (cashneq / rev_mean.replace(0, np.nan)) - (burn / rev_mean.replace(0, np.nan))


def f083crw_f083_cash_runway_br_21d_slope_v001_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_slope_v002_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_slope_v003_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_slope_v004_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_slope_v005_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_slope_v006_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_slope_v007_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_slope_v008_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_slope_v009_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_slope_v010_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_slope_v011_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_slope_v012_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_slope_v013_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_slope_v014_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_slope_v015_signal(cashneq, fcf, closeadj):
    base_pre = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_slope_v016_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_slope_v017_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_slope_v018_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_slope_v019_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_slope_v020_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_slope_v021_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_slope_v022_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_slope_v023_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_slope_v024_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_slope_v025_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_slope_v026_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_slope_v027_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_slope_v028_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_slope_v029_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_slope_v030_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_slope_v031_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_slope_v032_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_slope_v033_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_slope_v034_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_slope_v035_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_slope_v036_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_slope_v037_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_slope_v038_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_slope_v039_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_slope_v040_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_slope_v041_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_slope_v042_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_slope_v043_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_slope_v044_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_slope_v045_signal(cashneq, fcf, closeadj):
    base_pre = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_slope_v046_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base_pre = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_slope_v047_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base_pre = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_slope_v048_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base_pre = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_slope_v049_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base_pre = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_slope_v050_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base_pre = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_slope_v051_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base_pre = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_slope_v052_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base_pre = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_slope_v053_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base_pre = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_slope_v054_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base_pre = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_slope_v055_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base_pre = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_slope_v056_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base_pre = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_slope_v057_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base_pre = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_slope_v058_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base_pre = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_slope_v059_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base_pre = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_slope_v060_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base_pre = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_slope_v061_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_slope_v062_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_slope_v063_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_slope_v064_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_slope_v065_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_slope_v066_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_slope_v067_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_slope_v068_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_slope_v069_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_slope_v070_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_slope_v071_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_slope_v072_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_slope_v073_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_slope_v074_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_slope_v075_signal(cashneq, fcf, closeadj):
    base_pre = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_21d_slope_v076_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 21)
    base_pre = _ema(rwm / rwm.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_21d_slope_v077_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 21)
    base_pre = _ema(rwm / rwm.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_21d_slope_v078_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 21)
    base_pre = _ema(rwm / rwm.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_21d_slope_v079_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 21)
    base_pre = _ema(rwm / rwm.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_21d_slope_v080_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 21)
    base_pre = _ema(rwm / rwm.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_63d_slope_v081_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 63)
    base_pre = _ema(rwm / rwm.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_63d_slope_v082_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 63)
    base_pre = _ema(rwm / rwm.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_63d_slope_v083_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 63)
    base_pre = _ema(rwm / rwm.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_63d_slope_v084_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 63)
    base_pre = _ema(rwm / rwm.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_63d_slope_v085_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 63)
    base_pre = _ema(rwm / rwm.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_252d_slope_v086_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 252)
    base_pre = _ema(rwm / rwm.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_252d_slope_v087_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 252)
    base_pre = _ema(rwm / rwm.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_252d_slope_v088_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 252)
    base_pre = _ema(rwm / rwm.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_252d_slope_v089_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 252)
    base_pre = _ema(rwm / rwm.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwme_252d_slope_v090_signal(cashneq, fcf, closeadj):
    rwm = _f083_runway_months(cashneq, fcf, 252)
    base_pre = _ema(rwm / rwm.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_21d_slope_v091_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_21d_slope_v092_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_21d_slope_v093_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_21d_slope_v094_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_21d_slope_v095_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_63d_slope_v096_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_63d_slope_v097_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_63d_slope_v098_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_63d_slope_v099_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_63d_slope_v100_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_252d_slope_v101_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_252d_slope_v102_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_252d_slope_v103_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_252d_slope_v104_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwq_252d_slope_v105_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _f083_runway_quality(cashneq, fcf, revenue, 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_21d_slope_v106_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_21d_slope_v107_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_21d_slope_v108_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_21d_slope_v109_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_21d_slope_v110_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 21), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_63d_slope_v111_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_63d_slope_v112_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_63d_slope_v113_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_63d_slope_v114_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_63d_slope_v115_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 63), 126)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_252d_slope_v116_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_252d_slope_v117_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_252d_slope_v118_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_252d_slope_v119_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqz_252d_slope_v120_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _z(_f083_runway_quality(cashneq, fcf, revenue, 252), 504)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_21d_slope_v121_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_21d_slope_v122_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_21d_slope_v123_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_21d_slope_v124_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_21d_slope_v125_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_63d_slope_v126_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_63d_slope_v127_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_63d_slope_v128_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_63d_slope_v129_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_63d_slope_v130_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_252d_slope_v131_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_252d_slope_v132_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_252d_slope_v133_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_252d_slope_v134_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqe_252d_slope_v135_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _ema(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_21d_slope_v136_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_21d_slope_v137_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_21d_slope_v138_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_21d_slope_v139_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_21d_slope_v140_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 21), 21)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_63d_slope_v141_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_63d_slope_v142_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_63d_slope_v143_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_63d_slope_v144_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_63d_slope_v145_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 63), 63)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_252d_slope_v146_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_252d_slope_v147_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_252d_slope_v148_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_252d_slope_v149_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwqs_252d_slope_v150_signal(cashneq, fcf, revenue, closeadj):
    base_pre = _std(_f083_runway_quality(cashneq, fcf, revenue, 252), 252)
    base = base_pre * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f083crw_f083_cash_runway_br_21d_slope_v001_signal,
    f083crw_f083_cash_runway_br_21d_slope_v002_signal,
    f083crw_f083_cash_runway_br_21d_slope_v003_signal,
    f083crw_f083_cash_runway_br_21d_slope_v004_signal,
    f083crw_f083_cash_runway_br_21d_slope_v005_signal,
    f083crw_f083_cash_runway_br_63d_slope_v006_signal,
    f083crw_f083_cash_runway_br_63d_slope_v007_signal,
    f083crw_f083_cash_runway_br_63d_slope_v008_signal,
    f083crw_f083_cash_runway_br_63d_slope_v009_signal,
    f083crw_f083_cash_runway_br_63d_slope_v010_signal,
    f083crw_f083_cash_runway_br_252d_slope_v011_signal,
    f083crw_f083_cash_runway_br_252d_slope_v012_signal,
    f083crw_f083_cash_runway_br_252d_slope_v013_signal,
    f083crw_f083_cash_runway_br_252d_slope_v014_signal,
    f083crw_f083_cash_runway_br_252d_slope_v015_signal,
    f083crw_f083_cash_runway_brz_21d_slope_v016_signal,
    f083crw_f083_cash_runway_brz_21d_slope_v017_signal,
    f083crw_f083_cash_runway_brz_21d_slope_v018_signal,
    f083crw_f083_cash_runway_brz_21d_slope_v019_signal,
    f083crw_f083_cash_runway_brz_21d_slope_v020_signal,
    f083crw_f083_cash_runway_brz_63d_slope_v021_signal,
    f083crw_f083_cash_runway_brz_63d_slope_v022_signal,
    f083crw_f083_cash_runway_brz_63d_slope_v023_signal,
    f083crw_f083_cash_runway_brz_63d_slope_v024_signal,
    f083crw_f083_cash_runway_brz_63d_slope_v025_signal,
    f083crw_f083_cash_runway_brz_252d_slope_v026_signal,
    f083crw_f083_cash_runway_brz_252d_slope_v027_signal,
    f083crw_f083_cash_runway_brz_252d_slope_v028_signal,
    f083crw_f083_cash_runway_brz_252d_slope_v029_signal,
    f083crw_f083_cash_runway_brz_252d_slope_v030_signal,
    f083crw_f083_cash_runway_bre_21d_slope_v031_signal,
    f083crw_f083_cash_runway_bre_21d_slope_v032_signal,
    f083crw_f083_cash_runway_bre_21d_slope_v033_signal,
    f083crw_f083_cash_runway_bre_21d_slope_v034_signal,
    f083crw_f083_cash_runway_bre_21d_slope_v035_signal,
    f083crw_f083_cash_runway_bre_63d_slope_v036_signal,
    f083crw_f083_cash_runway_bre_63d_slope_v037_signal,
    f083crw_f083_cash_runway_bre_63d_slope_v038_signal,
    f083crw_f083_cash_runway_bre_63d_slope_v039_signal,
    f083crw_f083_cash_runway_bre_63d_slope_v040_signal,
    f083crw_f083_cash_runway_bre_252d_slope_v041_signal,
    f083crw_f083_cash_runway_bre_252d_slope_v042_signal,
    f083crw_f083_cash_runway_bre_252d_slope_v043_signal,
    f083crw_f083_cash_runway_bre_252d_slope_v044_signal,
    f083crw_f083_cash_runway_bre_252d_slope_v045_signal,
    f083crw_f083_cash_runway_rwm_21d_slope_v046_signal,
    f083crw_f083_cash_runway_rwm_21d_slope_v047_signal,
    f083crw_f083_cash_runway_rwm_21d_slope_v048_signal,
    f083crw_f083_cash_runway_rwm_21d_slope_v049_signal,
    f083crw_f083_cash_runway_rwm_21d_slope_v050_signal,
    f083crw_f083_cash_runway_rwm_63d_slope_v051_signal,
    f083crw_f083_cash_runway_rwm_63d_slope_v052_signal,
    f083crw_f083_cash_runway_rwm_63d_slope_v053_signal,
    f083crw_f083_cash_runway_rwm_63d_slope_v054_signal,
    f083crw_f083_cash_runway_rwm_63d_slope_v055_signal,
    f083crw_f083_cash_runway_rwm_252d_slope_v056_signal,
    f083crw_f083_cash_runway_rwm_252d_slope_v057_signal,
    f083crw_f083_cash_runway_rwm_252d_slope_v058_signal,
    f083crw_f083_cash_runway_rwm_252d_slope_v059_signal,
    f083crw_f083_cash_runway_rwm_252d_slope_v060_signal,
    f083crw_f083_cash_runway_rwmz_21d_slope_v061_signal,
    f083crw_f083_cash_runway_rwmz_21d_slope_v062_signal,
    f083crw_f083_cash_runway_rwmz_21d_slope_v063_signal,
    f083crw_f083_cash_runway_rwmz_21d_slope_v064_signal,
    f083crw_f083_cash_runway_rwmz_21d_slope_v065_signal,
    f083crw_f083_cash_runway_rwmz_63d_slope_v066_signal,
    f083crw_f083_cash_runway_rwmz_63d_slope_v067_signal,
    f083crw_f083_cash_runway_rwmz_63d_slope_v068_signal,
    f083crw_f083_cash_runway_rwmz_63d_slope_v069_signal,
    f083crw_f083_cash_runway_rwmz_63d_slope_v070_signal,
    f083crw_f083_cash_runway_rwmz_252d_slope_v071_signal,
    f083crw_f083_cash_runway_rwmz_252d_slope_v072_signal,
    f083crw_f083_cash_runway_rwmz_252d_slope_v073_signal,
    f083crw_f083_cash_runway_rwmz_252d_slope_v074_signal,
    f083crw_f083_cash_runway_rwmz_252d_slope_v075_signal,
    f083crw_f083_cash_runway_rwme_21d_slope_v076_signal,
    f083crw_f083_cash_runway_rwme_21d_slope_v077_signal,
    f083crw_f083_cash_runway_rwme_21d_slope_v078_signal,
    f083crw_f083_cash_runway_rwme_21d_slope_v079_signal,
    f083crw_f083_cash_runway_rwme_21d_slope_v080_signal,
    f083crw_f083_cash_runway_rwme_63d_slope_v081_signal,
    f083crw_f083_cash_runway_rwme_63d_slope_v082_signal,
    f083crw_f083_cash_runway_rwme_63d_slope_v083_signal,
    f083crw_f083_cash_runway_rwme_63d_slope_v084_signal,
    f083crw_f083_cash_runway_rwme_63d_slope_v085_signal,
    f083crw_f083_cash_runway_rwme_252d_slope_v086_signal,
    f083crw_f083_cash_runway_rwme_252d_slope_v087_signal,
    f083crw_f083_cash_runway_rwme_252d_slope_v088_signal,
    f083crw_f083_cash_runway_rwme_252d_slope_v089_signal,
    f083crw_f083_cash_runway_rwme_252d_slope_v090_signal,
    f083crw_f083_cash_runway_rwq_21d_slope_v091_signal,
    f083crw_f083_cash_runway_rwq_21d_slope_v092_signal,
    f083crw_f083_cash_runway_rwq_21d_slope_v093_signal,
    f083crw_f083_cash_runway_rwq_21d_slope_v094_signal,
    f083crw_f083_cash_runway_rwq_21d_slope_v095_signal,
    f083crw_f083_cash_runway_rwq_63d_slope_v096_signal,
    f083crw_f083_cash_runway_rwq_63d_slope_v097_signal,
    f083crw_f083_cash_runway_rwq_63d_slope_v098_signal,
    f083crw_f083_cash_runway_rwq_63d_slope_v099_signal,
    f083crw_f083_cash_runway_rwq_63d_slope_v100_signal,
    f083crw_f083_cash_runway_rwq_252d_slope_v101_signal,
    f083crw_f083_cash_runway_rwq_252d_slope_v102_signal,
    f083crw_f083_cash_runway_rwq_252d_slope_v103_signal,
    f083crw_f083_cash_runway_rwq_252d_slope_v104_signal,
    f083crw_f083_cash_runway_rwq_252d_slope_v105_signal,
    f083crw_f083_cash_runway_rwqz_21d_slope_v106_signal,
    f083crw_f083_cash_runway_rwqz_21d_slope_v107_signal,
    f083crw_f083_cash_runway_rwqz_21d_slope_v108_signal,
    f083crw_f083_cash_runway_rwqz_21d_slope_v109_signal,
    f083crw_f083_cash_runway_rwqz_21d_slope_v110_signal,
    f083crw_f083_cash_runway_rwqz_63d_slope_v111_signal,
    f083crw_f083_cash_runway_rwqz_63d_slope_v112_signal,
    f083crw_f083_cash_runway_rwqz_63d_slope_v113_signal,
    f083crw_f083_cash_runway_rwqz_63d_slope_v114_signal,
    f083crw_f083_cash_runway_rwqz_63d_slope_v115_signal,
    f083crw_f083_cash_runway_rwqz_252d_slope_v116_signal,
    f083crw_f083_cash_runway_rwqz_252d_slope_v117_signal,
    f083crw_f083_cash_runway_rwqz_252d_slope_v118_signal,
    f083crw_f083_cash_runway_rwqz_252d_slope_v119_signal,
    f083crw_f083_cash_runway_rwqz_252d_slope_v120_signal,
    f083crw_f083_cash_runway_rwqe_21d_slope_v121_signal,
    f083crw_f083_cash_runway_rwqe_21d_slope_v122_signal,
    f083crw_f083_cash_runway_rwqe_21d_slope_v123_signal,
    f083crw_f083_cash_runway_rwqe_21d_slope_v124_signal,
    f083crw_f083_cash_runway_rwqe_21d_slope_v125_signal,
    f083crw_f083_cash_runway_rwqe_63d_slope_v126_signal,
    f083crw_f083_cash_runway_rwqe_63d_slope_v127_signal,
    f083crw_f083_cash_runway_rwqe_63d_slope_v128_signal,
    f083crw_f083_cash_runway_rwqe_63d_slope_v129_signal,
    f083crw_f083_cash_runway_rwqe_63d_slope_v130_signal,
    f083crw_f083_cash_runway_rwqe_252d_slope_v131_signal,
    f083crw_f083_cash_runway_rwqe_252d_slope_v132_signal,
    f083crw_f083_cash_runway_rwqe_252d_slope_v133_signal,
    f083crw_f083_cash_runway_rwqe_252d_slope_v134_signal,
    f083crw_f083_cash_runway_rwqe_252d_slope_v135_signal,
    f083crw_f083_cash_runway_rwqs_21d_slope_v136_signal,
    f083crw_f083_cash_runway_rwqs_21d_slope_v137_signal,
    f083crw_f083_cash_runway_rwqs_21d_slope_v138_signal,
    f083crw_f083_cash_runway_rwqs_21d_slope_v139_signal,
    f083crw_f083_cash_runway_rwqs_21d_slope_v140_signal,
    f083crw_f083_cash_runway_rwqs_63d_slope_v141_signal,
    f083crw_f083_cash_runway_rwqs_63d_slope_v142_signal,
    f083crw_f083_cash_runway_rwqs_63d_slope_v143_signal,
    f083crw_f083_cash_runway_rwqs_63d_slope_v144_signal,
    f083crw_f083_cash_runway_rwqs_63d_slope_v145_signal,
    f083crw_f083_cash_runway_rwqs_252d_slope_v146_signal,
    f083crw_f083_cash_runway_rwqs_252d_slope_v147_signal,
    f083crw_f083_cash_runway_rwqs_252d_slope_v148_signal,
    f083crw_f083_cash_runway_rwqs_252d_slope_v149_signal,
    f083crw_f083_cash_runway_rwqs_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F083_CASH_RUNWAY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
        "fcf": fcf, "ncfo": ncfo, "cashneq": cashneq, "debt": debt, "equity": equity,
        "sharesbas": sharesbas, "shareswa": shareswa, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f083_burn_rate", "_f083_runway_months", "_f083_runway_quality")
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
    print(f"OK f083_cash_runway_2nd_derivatives_001_150_claude: {n_features} features pass")
