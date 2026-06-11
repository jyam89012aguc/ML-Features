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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


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


def _f09_earnings_vol(netinc, w):
    return netinc.rolling(w, min_periods=max(1, w // 2)).std()


def _f09_credit_quality_score(netinc, revenue, w):
    ratio = netinc / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f09_provision_proxy(netinc, w):
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return sd / m.replace(0, np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_5d_jerk_v001_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 5)
    base_series = base / _mean(netinc.abs(), 5).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_10d_jerk_v002_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 10)
    base_series = base / _mean(netinc.abs(), 10).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_21d_jerk_v003_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 21)
    base_series = base / _mean(netinc.abs(), 21).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_42d_jerk_v004_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 42)
    base_series = base / _mean(netinc.abs(), 42).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_63d_jerk_v005_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 63)
    base_series = base / _mean(netinc.abs(), 63).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_126d_jerk_v006_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 126)
    base_series = base / _mean(netinc.abs(), 126).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_189d_jerk_v007_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 189)
    base_series = base / _mean(netinc.abs(), 189).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_252d_jerk_v008_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 252)
    base_series = base / _mean(netinc.abs(), 252).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_378d_jerk_v009_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 378)
    base_series = base / _mean(netinc.abs(), 378).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_504d_jerk_v010_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 504)
    base_series = base / _mean(netinc.abs(), 504).replace(0, np.nan) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_5d_jerk_v011_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_10d_jerk_v012_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 10)
    base_series = base * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_21d_jerk_v013_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_42d_jerk_v014_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 42)
    base_series = base * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_63d_jerk_v015_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = base * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_126d_jerk_v016_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = base * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_189d_jerk_v017_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 189)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_252d_jerk_v018_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = base * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_378d_jerk_v019_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 378)
    base_series = base * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_504d_jerk_v020_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 504)
    base_series = base * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_5d_jerk_v021_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 5)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_10d_jerk_v022_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 10)
    base_series = base * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_21d_jerk_v023_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 21)
    base_series = base * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_42d_jerk_v024_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 42)
    base_series = base * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_63d_jerk_v025_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 63)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_126d_jerk_v026_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 126)
    base_series = base * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_189d_jerk_v027_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 189)
    base_series = base * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_252d_jerk_v028_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 252)
    base_series = base * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_378d_jerk_v029_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 378)
    base_series = base * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_504d_jerk_v030_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 504)
    base_series = base * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_21d_jerk_v031_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = _z(ev, 21) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_63d_jerk_v032_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = _z(ev, 63) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_126d_jerk_v033_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = _z(ev, 126) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_252d_jerk_v034_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = _z(ev, 252) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_21d_jerk_v035_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = _z(cq, 21) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_63d_jerk_v036_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = _z(cq, 63) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_126d_jerk_v037_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = _z(cq, 126) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_252d_jerk_v038_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = _z(cq, 252) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_21d_jerk_v039_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    base_series = _z(pp, 21) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_63d_jerk_v040_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    base_series = _z(pp, 63) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_126d_jerk_v041_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    base_series = _z(pp, 126) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_252d_jerk_v042_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    base_series = _z(pp, 252) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_10d_jerk_v043_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 10) / _mean(netinc.abs(), 10).replace(0, np.nan)
    base_series = _ema(ev, 10) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_21d_jerk_v044_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = _ema(ev, 21) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_63d_jerk_v045_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = _ema(ev, 63) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_126d_jerk_v046_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = _ema(ev, 126) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_252d_jerk_v047_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = _ema(ev, 252) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_10d_jerk_v048_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 10)
    base_series = _ema(cq, 10) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_21d_jerk_v049_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = _ema(cq, 21) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_63d_jerk_v050_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = _ema(cq, 63) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_126d_jerk_v051_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = _ema(cq, 126) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_252d_jerk_v052_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = _ema(cq, 252) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_10d_jerk_v053_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 10)
    base_series = _ema(pp, 10) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_21d_jerk_v054_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    base_series = _ema(pp, 21) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_63d_jerk_v055_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    base_series = _ema(pp, 63) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_126d_jerk_v056_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    base_series = _ema(pp, 126) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_252d_jerk_v057_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    base_series = _ema(pp, 252) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_5d_jerk_v058_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 5) / _mean(netinc.abs(), 5).replace(0, np.nan)
    base_series = ev.diff(periods=5) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_21d_jerk_v059_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = ev.diff(periods=21) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_63d_jerk_v060_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = ev.diff(periods=63) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_126d_jerk_v061_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = ev.diff(periods=126) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_252d_jerk_v062_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = ev.diff(periods=252) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_5d_jerk_v063_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 5)
    base_series = cq.diff(periods=5) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_21d_jerk_v064_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = cq.diff(periods=21) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_63d_jerk_v065_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = cq.diff(periods=63) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_126d_jerk_v066_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = cq.diff(periods=126) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_252d_jerk_v067_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = cq.diff(periods=252) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_5d_jerk_v068_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 5)
    base_series = pp.diff(periods=5) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_21d_jerk_v069_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    base_series = pp.diff(periods=21) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_63d_jerk_v070_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    base_series = pp.diff(periods=63) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_126d_jerk_v071_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    base_series = pp.diff(periods=126) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_252d_jerk_v072_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    base_series = pp.diff(periods=252) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_63d_jerk_v073_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    rnk = ev.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_126d_jerk_v074_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126)
    rnk = ev.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_252d_jerk_v075_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    rnk = ev.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_63d_jerk_v076_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    rnk = cq.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_126d_jerk_v077_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    rnk = cq.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_252d_jerk_v078_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    rnk = cq.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_63d_jerk_v079_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    rnk = pp.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_126d_jerk_v080_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    rnk = pp.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_252d_jerk_v081_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    rnk = pp.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_21d_jerk_v082_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21)
    base_series = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_63d_jerk_v083_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    base_series = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_252d_jerk_v084_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    base_series = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_21d_jerk_v085_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = ev * cq * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_63d_jerk_v086_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = ev * cq * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_126d_jerk_v087_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = ev * cq * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_252d_jerk_v088_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = ev * cq * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_21d_jerk_v089_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = pp * cq * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_63d_jerk_v090_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = pp * cq * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_126d_jerk_v091_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = pp * cq * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_252d_jerk_v092_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = pp * cq * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_21v63_jerk_v093_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 21)
    b = _f09_earnings_vol(netinc, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_21v63_jerk_v094_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 21)
    b = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_63v252_jerk_v095_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 63)
    b = _f09_earnings_vol(netinc, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_63v252_jerk_v096_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 63)
    b = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_126v504_jerk_v097_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 126)
    b = _f09_earnings_vol(netinc, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_126v504_jerk_v098_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 126)
    b = _f09_credit_quality_score(netinc, revenue, 504)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_42v189_jerk_v099_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 42)
    b = _f09_earnings_vol(netinc, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_42v189_jerk_v100_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 42)
    b = _f09_credit_quality_score(netinc, revenue, 189)
    base_series = (a - b) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_21d_jerk_v101_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 21)
    rev_chg = revenue.pct_change(periods=21)
    base_series = ev / _mean(revenue.abs(), 21).replace(0, np.nan) * rev_chg * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_63d_jerk_v102_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    rev_chg = revenue.pct_change(periods=63)
    base_series = ev / _mean(revenue.abs(), 63).replace(0, np.nan) * rev_chg * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_126d_jerk_v103_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 126)
    rev_chg = revenue.pct_change(periods=126)
    base_series = ev / _mean(revenue.abs(), 126).replace(0, np.nan) * rev_chg * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_252d_jerk_v104_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    rev_chg = revenue.pct_change(periods=252)
    base_series = ev / _mean(revenue.abs(), 252).replace(0, np.nan) * rev_chg * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_63d_jerk_v105_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    rng = cq.rolling(63, min_periods=max(1, 63//2)).max() - cq.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_126d_jerk_v106_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    rng = cq.rolling(126, min_periods=max(1, 126//2)).max() - cq.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_252d_jerk_v107_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    rng = cq.rolling(252, min_periods=max(1, 252//2)).max() - cq.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_21d_jerk_v108_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    base_series = _std(pp, 21) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_63d_jerk_v109_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    base_series = _std(pp, 63) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_126d_jerk_v110_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    base_series = _std(pp, 126) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_252d_jerk_v111_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    base_series = _std(pp, 252) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_21d_jerk_v112_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    base_series = _std(cq, 21) * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_63d_jerk_v113_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    base_series = _std(cq, 63) * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_126d_jerk_v114_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    base_series = _std(cq, 126) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_252d_jerk_v115_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    base_series = _std(cq, 252) * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_21d_jerk_v116_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    base_series = ev * pv * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_63d_jerk_v117_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    base_series = ev * pv * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_126d_jerk_v118_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    base_series = ev * pv * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_252d_jerk_v119_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    base_series = ev * pv * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_5d_jerk_v120_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 5)
    rev_m = _mean(revenue.abs(), 5).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_10d_jerk_v121_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 10)
    rev_m = _mean(revenue.abs(), 10).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_21d_jerk_v122_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 21)
    rev_m = _mean(revenue.abs(), 21).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_42d_jerk_v123_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 42)
    rev_m = _mean(revenue.abs(), 42).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_63d_jerk_v124_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 63)
    rev_m = _mean(revenue.abs(), 63).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_126d_jerk_v125_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 126)
    rev_m = _mean(revenue.abs(), 126).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_189d_jerk_v126_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 189)
    rev_m = _mean(revenue.abs(), 189).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_252d_jerk_v127_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 252)
    rev_m = _mean(revenue.abs(), 252).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_378d_jerk_v128_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 378)
    rev_m = _mean(revenue.abs(), 378).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_504d_jerk_v129_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 504)
    rev_m = _mean(revenue.abs(), 504).replace(0, np.nan)
    base_series = base / rev_m * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_21d_jerk_v130_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = ev.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_42d_jerk_v131_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    base_series = ev.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_63d_jerk_v132_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = ev.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_126d_jerk_v133_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = ev.rolling(126, min_periods=max(1, 126//2)).sum() * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_189d_jerk_v134_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 189) / _mean(netinc.abs(), 189).replace(0, np.nan)
    base_series = ev.rolling(189, min_periods=max(1, 189//2)).sum() * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_252d_jerk_v135_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = ev.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_378d_jerk_v136_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 378) / _mean(netinc.abs(), 378).replace(0, np.nan)
    base_series = ev.rolling(378, min_periods=max(1, 378//2)).sum() * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_504d_jerk_v137_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 504) / _mean(netinc.abs(), 504).replace(0, np.nan)
    base_series = ev.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_21d_jerk_v138_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    cv = _std(closeadj.pct_change(), 21)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_42d_jerk_v139_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 42)
    cv = _std(closeadj.pct_change(), 42)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_63d_jerk_v140_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    cv = _std(closeadj.pct_change(), 63)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_126d_jerk_v141_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    cv = _std(closeadj.pct_change(), 126)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_189d_jerk_v142_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 189)
    cv = _std(closeadj.pct_change(), 189)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_252d_jerk_v143_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    cv = _std(closeadj.pct_change(), 252)
    base_series = cq * cv * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_21d_jerk_v144_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    rg = revenue.pct_change(periods=21)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_42d_jerk_v145_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 42)
    rg = revenue.pct_change(periods=42)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_63d_jerk_v146_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    rg = revenue.pct_change(periods=63)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_126d_jerk_v147_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    rg = revenue.pct_change(periods=126)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_189d_jerk_v148_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 189)
    rg = revenue.pct_change(periods=189)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_252d_jerk_v149_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    rg = revenue.pct_change(periods=252)
    base_series = pp * rg * closeadj
    result = _jerk(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolemapct_21d_jerk_v150_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = _ema(ev, 21).pct_change(periods=21) * closeadj
    result = _jerk(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09bcq_f09_bank_credit_quality_earnvol_5d_jerk_v001_signal,
    f09bcq_f09_bank_credit_quality_earnvol_10d_jerk_v002_signal,
    f09bcq_f09_bank_credit_quality_earnvol_21d_jerk_v003_signal,
    f09bcq_f09_bank_credit_quality_earnvol_42d_jerk_v004_signal,
    f09bcq_f09_bank_credit_quality_earnvol_63d_jerk_v005_signal,
    f09bcq_f09_bank_credit_quality_earnvol_126d_jerk_v006_signal,
    f09bcq_f09_bank_credit_quality_earnvol_189d_jerk_v007_signal,
    f09bcq_f09_bank_credit_quality_earnvol_252d_jerk_v008_signal,
    f09bcq_f09_bank_credit_quality_earnvol_378d_jerk_v009_signal,
    f09bcq_f09_bank_credit_quality_earnvol_504d_jerk_v010_signal,
    f09bcq_f09_bank_credit_quality_creditqual_5d_jerk_v011_signal,
    f09bcq_f09_bank_credit_quality_creditqual_10d_jerk_v012_signal,
    f09bcq_f09_bank_credit_quality_creditqual_21d_jerk_v013_signal,
    f09bcq_f09_bank_credit_quality_creditqual_42d_jerk_v014_signal,
    f09bcq_f09_bank_credit_quality_creditqual_63d_jerk_v015_signal,
    f09bcq_f09_bank_credit_quality_creditqual_126d_jerk_v016_signal,
    f09bcq_f09_bank_credit_quality_creditqual_189d_jerk_v017_signal,
    f09bcq_f09_bank_credit_quality_creditqual_252d_jerk_v018_signal,
    f09bcq_f09_bank_credit_quality_creditqual_378d_jerk_v019_signal,
    f09bcq_f09_bank_credit_quality_creditqual_504d_jerk_v020_signal,
    f09bcq_f09_bank_credit_quality_provprox_5d_jerk_v021_signal,
    f09bcq_f09_bank_credit_quality_provprox_10d_jerk_v022_signal,
    f09bcq_f09_bank_credit_quality_provprox_21d_jerk_v023_signal,
    f09bcq_f09_bank_credit_quality_provprox_42d_jerk_v024_signal,
    f09bcq_f09_bank_credit_quality_provprox_63d_jerk_v025_signal,
    f09bcq_f09_bank_credit_quality_provprox_126d_jerk_v026_signal,
    f09bcq_f09_bank_credit_quality_provprox_189d_jerk_v027_signal,
    f09bcq_f09_bank_credit_quality_provprox_252d_jerk_v028_signal,
    f09bcq_f09_bank_credit_quality_provprox_378d_jerk_v029_signal,
    f09bcq_f09_bank_credit_quality_provprox_504d_jerk_v030_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_21d_jerk_v031_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_63d_jerk_v032_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_126d_jerk_v033_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_252d_jerk_v034_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_21d_jerk_v035_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_63d_jerk_v036_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_126d_jerk_v037_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_252d_jerk_v038_signal,
    f09bcq_f09_bank_credit_quality_provproxz_21d_jerk_v039_signal,
    f09bcq_f09_bank_credit_quality_provproxz_63d_jerk_v040_signal,
    f09bcq_f09_bank_credit_quality_provproxz_126d_jerk_v041_signal,
    f09bcq_f09_bank_credit_quality_provproxz_252d_jerk_v042_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_10d_jerk_v043_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_21d_jerk_v044_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_63d_jerk_v045_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_126d_jerk_v046_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_252d_jerk_v047_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_10d_jerk_v048_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_21d_jerk_v049_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_63d_jerk_v050_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_126d_jerk_v051_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_252d_jerk_v052_signal,
    f09bcq_f09_bank_credit_quality_provproxema_10d_jerk_v053_signal,
    f09bcq_f09_bank_credit_quality_provproxema_21d_jerk_v054_signal,
    f09bcq_f09_bank_credit_quality_provproxema_63d_jerk_v055_signal,
    f09bcq_f09_bank_credit_quality_provproxema_126d_jerk_v056_signal,
    f09bcq_f09_bank_credit_quality_provproxema_252d_jerk_v057_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_5d_jerk_v058_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_21d_jerk_v059_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_63d_jerk_v060_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_126d_jerk_v061_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_252d_jerk_v062_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_5d_jerk_v063_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_21d_jerk_v064_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_63d_jerk_v065_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_126d_jerk_v066_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_252d_jerk_v067_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_5d_jerk_v068_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_21d_jerk_v069_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_63d_jerk_v070_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_126d_jerk_v071_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_252d_jerk_v072_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_63d_jerk_v073_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_126d_jerk_v074_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_252d_jerk_v075_signal,
    f09bcq_f09_bank_credit_quality_creditqualrank_63d_jerk_v076_signal,
    f09bcq_f09_bank_credit_quality_creditqualrank_126d_jerk_v077_signal,
    f09bcq_f09_bank_credit_quality_creditqualrank_252d_jerk_v078_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_63d_jerk_v079_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_126d_jerk_v080_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_252d_jerk_v081_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_21d_jerk_v082_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_63d_jerk_v083_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_252d_jerk_v084_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_21d_jerk_v085_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_63d_jerk_v086_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_126d_jerk_v087_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_252d_jerk_v088_signal,
    f09bcq_f09_bank_credit_quality_provxqual_21d_jerk_v089_signal,
    f09bcq_f09_bank_credit_quality_provxqual_63d_jerk_v090_signal,
    f09bcq_f09_bank_credit_quality_provxqual_126d_jerk_v091_signal,
    f09bcq_f09_bank_credit_quality_provxqual_252d_jerk_v092_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_21v63_jerk_v093_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_21v63_jerk_v094_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_63v252_jerk_v095_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_63v252_jerk_v096_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_126v504_jerk_v097_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_126v504_jerk_v098_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_42v189_jerk_v099_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_42v189_jerk_v100_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_21d_jerk_v101_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_63d_jerk_v102_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_126d_jerk_v103_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_252d_jerk_v104_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_63d_jerk_v105_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_126d_jerk_v106_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_252d_jerk_v107_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_21d_jerk_v108_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_63d_jerk_v109_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_126d_jerk_v110_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_252d_jerk_v111_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_21d_jerk_v112_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_63d_jerk_v113_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_126d_jerk_v114_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_252d_jerk_v115_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_21d_jerk_v116_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_63d_jerk_v117_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_126d_jerk_v118_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_252d_jerk_v119_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_5d_jerk_v120_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_10d_jerk_v121_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_21d_jerk_v122_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_42d_jerk_v123_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_63d_jerk_v124_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_126d_jerk_v125_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_189d_jerk_v126_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_252d_jerk_v127_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_378d_jerk_v128_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_504d_jerk_v129_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_21d_jerk_v130_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_42d_jerk_v131_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_63d_jerk_v132_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_126d_jerk_v133_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_189d_jerk_v134_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_252d_jerk_v135_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_378d_jerk_v136_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_504d_jerk_v137_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_21d_jerk_v138_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_42d_jerk_v139_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_63d_jerk_v140_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_126d_jerk_v141_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_189d_jerk_v142_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_252d_jerk_v143_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_21d_jerk_v144_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_42d_jerk_v145_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_63d_jerk_v146_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_126d_jerk_v147_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_189d_jerk_v148_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_252d_jerk_v149_signal,
    f09bcq_f09_bank_credit_quality_earnvolemapct_21d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_BANK_CREDIT_QUALITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f09_earnings_vol', '_f09_credit_quality_score', '_f09_provision_proxy')
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
    print(f"OK f09_bank_credit_quality_3rd_derivatives_001_150_claude: {n_features} features pass")
