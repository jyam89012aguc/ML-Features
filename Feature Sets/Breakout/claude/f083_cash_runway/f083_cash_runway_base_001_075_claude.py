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


def f083crw_f083_cash_runway_br_21d_xclose_base_v001_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_xemac_base_v002_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_xmean_base_v003_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_xclose2_base_v004_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_21d_xmlong_base_v005_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_xclose_base_v006_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_xemac_base_v007_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_xmean_base_v008_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_xclose2_base_v009_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_63d_xmlong_base_v010_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_xclose_base_v011_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_xemac_base_v012_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_xmean_base_v013_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_xclose2_base_v014_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_br_252d_xmlong_base_v015_signal(cashneq, fcf, closeadj):
    base = _f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_xclose_base_v016_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_xemac_base_v017_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_xmean_base_v018_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_xclose2_base_v019_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_21d_xmlong_base_v020_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_xclose_base_v021_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_xemac_base_v022_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_xmean_base_v023_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_xclose2_base_v024_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_63d_xmlong_base_v025_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_xclose_base_v026_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_xemac_base_v027_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_xmean_base_v028_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_xclose2_base_v029_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_brz_252d_xmlong_base_v030_signal(cashneq, fcf, closeadj):
    base = _z(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 504)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_xclose_base_v031_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_xemac_base_v032_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_xmean_base_v033_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_xclose2_base_v034_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_21d_xmlong_base_v035_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 21) / cashneq.abs().replace(0, np.nan), 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_xclose_base_v036_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_xemac_base_v037_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_xmean_base_v038_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_xclose2_base_v039_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_63d_xmlong_base_v040_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 63) / cashneq.abs().replace(0, np.nan), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_xclose_base_v041_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_xemac_base_v042_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_xmean_base_v043_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_xclose2_base_v044_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_bre_252d_xmlong_base_v045_signal(cashneq, fcf, closeadj):
    base = _ema(_f083_burn_rate(fcf, 252) / cashneq.abs().replace(0, np.nan), 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_xclose_base_v046_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_xemac_base_v047_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_xmean_base_v048_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_xclose2_base_v049_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_21d_xmlong_base_v050_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 21)
    base = raw / raw.rolling(63, min_periods=max(1,21//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_xclose_base_v051_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_xemac_base_v052_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_xmean_base_v053_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_xclose2_base_v054_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_63d_xmlong_base_v055_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 63)
    base = raw / raw.rolling(126, min_periods=max(1,63//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_xclose_base_v056_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_xemac_base_v057_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_xmean_base_v058_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_xclose2_base_v059_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwm_252d_xmlong_base_v060_signal(cashneq, fcf, closeadj):
    raw = _f083_runway_months(cashneq, fcf, 252)
    base = raw / raw.rolling(504, min_periods=max(1,252//2)).mean().replace(0, np.nan)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_xclose_base_v061_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_xemac_base_v062_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_xmean_base_v063_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_xclose2_base_v064_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_21d_xmlong_base_v065_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 21), 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_xclose_base_v066_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_xemac_base_v067_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_xmean_base_v068_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_xclose2_base_v069_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_63d_xmlong_base_v070_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 63), 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_xclose_base_v071_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_xemac_base_v072_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_xmean_base_v073_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_xclose2_base_v074_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f083crw_f083_cash_runway_rwmz_252d_xmlong_base_v075_signal(cashneq, fcf, closeadj):
    base = _z(_f083_runway_months(cashneq, fcf, 252), 504)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f083crw_f083_cash_runway_br_21d_xclose_base_v001_signal,
    f083crw_f083_cash_runway_br_21d_xemac_base_v002_signal,
    f083crw_f083_cash_runway_br_21d_xmean_base_v003_signal,
    f083crw_f083_cash_runway_br_21d_xclose2_base_v004_signal,
    f083crw_f083_cash_runway_br_21d_xmlong_base_v005_signal,
    f083crw_f083_cash_runway_br_63d_xclose_base_v006_signal,
    f083crw_f083_cash_runway_br_63d_xemac_base_v007_signal,
    f083crw_f083_cash_runway_br_63d_xmean_base_v008_signal,
    f083crw_f083_cash_runway_br_63d_xclose2_base_v009_signal,
    f083crw_f083_cash_runway_br_63d_xmlong_base_v010_signal,
    f083crw_f083_cash_runway_br_252d_xclose_base_v011_signal,
    f083crw_f083_cash_runway_br_252d_xemac_base_v012_signal,
    f083crw_f083_cash_runway_br_252d_xmean_base_v013_signal,
    f083crw_f083_cash_runway_br_252d_xclose2_base_v014_signal,
    f083crw_f083_cash_runway_br_252d_xmlong_base_v015_signal,
    f083crw_f083_cash_runway_brz_21d_xclose_base_v016_signal,
    f083crw_f083_cash_runway_brz_21d_xemac_base_v017_signal,
    f083crw_f083_cash_runway_brz_21d_xmean_base_v018_signal,
    f083crw_f083_cash_runway_brz_21d_xclose2_base_v019_signal,
    f083crw_f083_cash_runway_brz_21d_xmlong_base_v020_signal,
    f083crw_f083_cash_runway_brz_63d_xclose_base_v021_signal,
    f083crw_f083_cash_runway_brz_63d_xemac_base_v022_signal,
    f083crw_f083_cash_runway_brz_63d_xmean_base_v023_signal,
    f083crw_f083_cash_runway_brz_63d_xclose2_base_v024_signal,
    f083crw_f083_cash_runway_brz_63d_xmlong_base_v025_signal,
    f083crw_f083_cash_runway_brz_252d_xclose_base_v026_signal,
    f083crw_f083_cash_runway_brz_252d_xemac_base_v027_signal,
    f083crw_f083_cash_runway_brz_252d_xmean_base_v028_signal,
    f083crw_f083_cash_runway_brz_252d_xclose2_base_v029_signal,
    f083crw_f083_cash_runway_brz_252d_xmlong_base_v030_signal,
    f083crw_f083_cash_runway_bre_21d_xclose_base_v031_signal,
    f083crw_f083_cash_runway_bre_21d_xemac_base_v032_signal,
    f083crw_f083_cash_runway_bre_21d_xmean_base_v033_signal,
    f083crw_f083_cash_runway_bre_21d_xclose2_base_v034_signal,
    f083crw_f083_cash_runway_bre_21d_xmlong_base_v035_signal,
    f083crw_f083_cash_runway_bre_63d_xclose_base_v036_signal,
    f083crw_f083_cash_runway_bre_63d_xemac_base_v037_signal,
    f083crw_f083_cash_runway_bre_63d_xmean_base_v038_signal,
    f083crw_f083_cash_runway_bre_63d_xclose2_base_v039_signal,
    f083crw_f083_cash_runway_bre_63d_xmlong_base_v040_signal,
    f083crw_f083_cash_runway_bre_252d_xclose_base_v041_signal,
    f083crw_f083_cash_runway_bre_252d_xemac_base_v042_signal,
    f083crw_f083_cash_runway_bre_252d_xmean_base_v043_signal,
    f083crw_f083_cash_runway_bre_252d_xclose2_base_v044_signal,
    f083crw_f083_cash_runway_bre_252d_xmlong_base_v045_signal,
    f083crw_f083_cash_runway_rwm_21d_xclose_base_v046_signal,
    f083crw_f083_cash_runway_rwm_21d_xemac_base_v047_signal,
    f083crw_f083_cash_runway_rwm_21d_xmean_base_v048_signal,
    f083crw_f083_cash_runway_rwm_21d_xclose2_base_v049_signal,
    f083crw_f083_cash_runway_rwm_21d_xmlong_base_v050_signal,
    f083crw_f083_cash_runway_rwm_63d_xclose_base_v051_signal,
    f083crw_f083_cash_runway_rwm_63d_xemac_base_v052_signal,
    f083crw_f083_cash_runway_rwm_63d_xmean_base_v053_signal,
    f083crw_f083_cash_runway_rwm_63d_xclose2_base_v054_signal,
    f083crw_f083_cash_runway_rwm_63d_xmlong_base_v055_signal,
    f083crw_f083_cash_runway_rwm_252d_xclose_base_v056_signal,
    f083crw_f083_cash_runway_rwm_252d_xemac_base_v057_signal,
    f083crw_f083_cash_runway_rwm_252d_xmean_base_v058_signal,
    f083crw_f083_cash_runway_rwm_252d_xclose2_base_v059_signal,
    f083crw_f083_cash_runway_rwm_252d_xmlong_base_v060_signal,
    f083crw_f083_cash_runway_rwmz_21d_xclose_base_v061_signal,
    f083crw_f083_cash_runway_rwmz_21d_xemac_base_v062_signal,
    f083crw_f083_cash_runway_rwmz_21d_xmean_base_v063_signal,
    f083crw_f083_cash_runway_rwmz_21d_xclose2_base_v064_signal,
    f083crw_f083_cash_runway_rwmz_21d_xmlong_base_v065_signal,
    f083crw_f083_cash_runway_rwmz_63d_xclose_base_v066_signal,
    f083crw_f083_cash_runway_rwmz_63d_xemac_base_v067_signal,
    f083crw_f083_cash_runway_rwmz_63d_xmean_base_v068_signal,
    f083crw_f083_cash_runway_rwmz_63d_xclose2_base_v069_signal,
    f083crw_f083_cash_runway_rwmz_63d_xmlong_base_v070_signal,
    f083crw_f083_cash_runway_rwmz_252d_xclose_base_v071_signal,
    f083crw_f083_cash_runway_rwmz_252d_xemac_base_v072_signal,
    f083crw_f083_cash_runway_rwmz_252d_xmean_base_v073_signal,
    f083crw_f083_cash_runway_rwmz_252d_xclose2_base_v074_signal,
    f083crw_f083_cash_runway_rwmz_252d_xmlong_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F083_CASH_RUNWAY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f083_cash_runway_base_001_075_claude: {n_features} features pass")
