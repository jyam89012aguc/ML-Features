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


def _f09_earnings_vol(netinc, w):
    return netinc.rolling(w, min_periods=max(1, w // 2)).std()


def _f09_credit_quality_score(netinc, revenue, w):
    ratio = netinc / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f09_provision_proxy(netinc, w):
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return sd / m.replace(0, np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_5d_base_v001_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 5)
    result = base / _mean(netinc.abs(), 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_10d_base_v002_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 10)
    result = base / _mean(netinc.abs(), 10).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_21d_base_v003_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 21)
    result = base / _mean(netinc.abs(), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_42d_base_v004_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 42)
    result = base / _mean(netinc.abs(), 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_63d_base_v005_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 63)
    result = base / _mean(netinc.abs(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_126d_base_v006_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 126)
    result = base / _mean(netinc.abs(), 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_189d_base_v007_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 189)
    result = base / _mean(netinc.abs(), 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_252d_base_v008_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 252)
    result = base / _mean(netinc.abs(), 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_378d_base_v009_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 378)
    result = base / _mean(netinc.abs(), 378).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvol_504d_base_v010_signal(netinc, closeadj):
    base = _f09_earnings_vol(netinc, 504)
    result = base / _mean(netinc.abs(), 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_5d_base_v011_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_10d_base_v012_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_21d_base_v013_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_42d_base_v014_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_63d_base_v015_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_126d_base_v016_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_189d_base_v017_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_252d_base_v018_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_378d_base_v019_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqual_504d_base_v020_signal(netinc, revenue, closeadj):
    base = _f09_credit_quality_score(netinc, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_5d_base_v021_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_10d_base_v022_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_21d_base_v023_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_42d_base_v024_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_63d_base_v025_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_126d_base_v026_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_189d_base_v027_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_252d_base_v028_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_378d_base_v029_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provprox_504d_base_v030_signal(netinc, closeadj):
    base = _f09_provision_proxy(netinc, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_21d_base_v031_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = _z(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_63d_base_v032_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = _z(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_126d_base_v033_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = _z(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolz_252d_base_v034_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = _z(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_21d_base_v035_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = _z(cq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_63d_base_v036_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = _z(cq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_126d_base_v037_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = _z(cq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualz_252d_base_v038_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = _z(cq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_21d_base_v039_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    result = _z(pp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_63d_base_v040_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    result = _z(pp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_126d_base_v041_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    result = _z(pp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxz_252d_base_v042_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    result = _z(pp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_10d_base_v043_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 10) / _mean(netinc.abs(), 10).replace(0, np.nan)
    result = _ema(ev, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_21d_base_v044_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = _ema(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_63d_base_v045_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = _ema(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_126d_base_v046_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = _ema(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolema_252d_base_v047_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = _ema(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_10d_base_v048_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 10)
    result = _ema(cq, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_21d_base_v049_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = _ema(cq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_63d_base_v050_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = _ema(cq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_126d_base_v051_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = _ema(cq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualema_252d_base_v052_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = _ema(cq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_10d_base_v053_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 10)
    result = _ema(pp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_21d_base_v054_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    result = _ema(pp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_63d_base_v055_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    result = _ema(pp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_126d_base_v056_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    result = _ema(pp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxema_252d_base_v057_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    result = _ema(pp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_5d_base_v058_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 5) / _mean(netinc.abs(), 5).replace(0, np.nan)
    result = ev.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_21d_base_v059_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = ev.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_63d_base_v060_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = ev.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_126d_base_v061_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = ev.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolchg_252d_base_v062_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = ev.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_5d_base_v063_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 5)
    result = cq.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_21d_base_v064_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = cq.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_63d_base_v065_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = cq.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_126d_base_v066_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = cq.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualchg_252d_base_v067_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = cq.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_5d_base_v068_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 5)
    result = pp.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_21d_base_v069_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    result = pp.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_63d_base_v070_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    result = pp.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_126d_base_v071_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    result = pp.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxchg_252d_base_v072_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    result = pp.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_63d_base_v073_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    rnk = ev.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_126d_base_v074_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126)
    rnk = ev.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolrank_252d_base_v075_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    rnk = ev.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09bcq_f09_bank_credit_quality_earnvol_5d_base_v001_signal,
    f09bcq_f09_bank_credit_quality_earnvol_10d_base_v002_signal,
    f09bcq_f09_bank_credit_quality_earnvol_21d_base_v003_signal,
    f09bcq_f09_bank_credit_quality_earnvol_42d_base_v004_signal,
    f09bcq_f09_bank_credit_quality_earnvol_63d_base_v005_signal,
    f09bcq_f09_bank_credit_quality_earnvol_126d_base_v006_signal,
    f09bcq_f09_bank_credit_quality_earnvol_189d_base_v007_signal,
    f09bcq_f09_bank_credit_quality_earnvol_252d_base_v008_signal,
    f09bcq_f09_bank_credit_quality_earnvol_378d_base_v009_signal,
    f09bcq_f09_bank_credit_quality_earnvol_504d_base_v010_signal,
    f09bcq_f09_bank_credit_quality_creditqual_5d_base_v011_signal,
    f09bcq_f09_bank_credit_quality_creditqual_10d_base_v012_signal,
    f09bcq_f09_bank_credit_quality_creditqual_21d_base_v013_signal,
    f09bcq_f09_bank_credit_quality_creditqual_42d_base_v014_signal,
    f09bcq_f09_bank_credit_quality_creditqual_63d_base_v015_signal,
    f09bcq_f09_bank_credit_quality_creditqual_126d_base_v016_signal,
    f09bcq_f09_bank_credit_quality_creditqual_189d_base_v017_signal,
    f09bcq_f09_bank_credit_quality_creditqual_252d_base_v018_signal,
    f09bcq_f09_bank_credit_quality_creditqual_378d_base_v019_signal,
    f09bcq_f09_bank_credit_quality_creditqual_504d_base_v020_signal,
    f09bcq_f09_bank_credit_quality_provprox_5d_base_v021_signal,
    f09bcq_f09_bank_credit_quality_provprox_10d_base_v022_signal,
    f09bcq_f09_bank_credit_quality_provprox_21d_base_v023_signal,
    f09bcq_f09_bank_credit_quality_provprox_42d_base_v024_signal,
    f09bcq_f09_bank_credit_quality_provprox_63d_base_v025_signal,
    f09bcq_f09_bank_credit_quality_provprox_126d_base_v026_signal,
    f09bcq_f09_bank_credit_quality_provprox_189d_base_v027_signal,
    f09bcq_f09_bank_credit_quality_provprox_252d_base_v028_signal,
    f09bcq_f09_bank_credit_quality_provprox_378d_base_v029_signal,
    f09bcq_f09_bank_credit_quality_provprox_504d_base_v030_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_21d_base_v031_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_63d_base_v032_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_126d_base_v033_signal,
    f09bcq_f09_bank_credit_quality_earnvolz_252d_base_v034_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_21d_base_v035_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_63d_base_v036_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_126d_base_v037_signal,
    f09bcq_f09_bank_credit_quality_creditqualz_252d_base_v038_signal,
    f09bcq_f09_bank_credit_quality_provproxz_21d_base_v039_signal,
    f09bcq_f09_bank_credit_quality_provproxz_63d_base_v040_signal,
    f09bcq_f09_bank_credit_quality_provproxz_126d_base_v041_signal,
    f09bcq_f09_bank_credit_quality_provproxz_252d_base_v042_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_10d_base_v043_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_21d_base_v044_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_63d_base_v045_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_126d_base_v046_signal,
    f09bcq_f09_bank_credit_quality_earnvolema_252d_base_v047_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_10d_base_v048_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_21d_base_v049_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_63d_base_v050_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_126d_base_v051_signal,
    f09bcq_f09_bank_credit_quality_creditqualema_252d_base_v052_signal,
    f09bcq_f09_bank_credit_quality_provproxema_10d_base_v053_signal,
    f09bcq_f09_bank_credit_quality_provproxema_21d_base_v054_signal,
    f09bcq_f09_bank_credit_quality_provproxema_63d_base_v055_signal,
    f09bcq_f09_bank_credit_quality_provproxema_126d_base_v056_signal,
    f09bcq_f09_bank_credit_quality_provproxema_252d_base_v057_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_5d_base_v058_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_21d_base_v059_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_63d_base_v060_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_126d_base_v061_signal,
    f09bcq_f09_bank_credit_quality_earnvolchg_252d_base_v062_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_5d_base_v063_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_21d_base_v064_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_63d_base_v065_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_126d_base_v066_signal,
    f09bcq_f09_bank_credit_quality_creditqualchg_252d_base_v067_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_5d_base_v068_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_21d_base_v069_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_63d_base_v070_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_126d_base_v071_signal,
    f09bcq_f09_bank_credit_quality_provproxchg_252d_base_v072_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_63d_base_v073_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_126d_base_v074_signal,
    f09bcq_f09_bank_credit_quality_earnvolrank_252d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_BANK_CREDIT_QUALITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f09_bank_credit_quality_base_001_075_claude: {n_features} features pass")
