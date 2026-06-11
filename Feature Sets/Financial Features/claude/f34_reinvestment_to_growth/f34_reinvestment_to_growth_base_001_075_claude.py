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


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f34_retained_growth(retearn, w):
    return retearn.pct_change(periods=w)


def _f34_reinvestment_intensity(retearn, equity):
    return retearn / equity.replace(0, np.nan).abs()


def _f34_reinvestment_quality(retearn, equity, w):
    intens = retearn / equity.replace(0, np.nan).abs()
    return intens.pct_change(periods=w)


# ===== features =====
def f34rtg_f34_reinvestment_to_growth_retgrowth_5d_base_v001_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_10d_base_v002_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_21d_base_v003_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_42d_base_v004_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_63d_base_v005_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_126d_base_v006_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_189d_base_v007_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_252d_base_v008_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_378d_base_v009_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowth_504d_base_v010_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthabs_21d_base_v011_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthabs_63d_base_v012_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthabs_126d_base_v013_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthabs_252d_base_v014_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthabs_504d_base_v015_signal(retearn, closeadj):
    result = _f34_retained_growth(retearn, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_5d_base_v016_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_10d_base_v017_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_21d_base_v018_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_42d_base_v019_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_63d_base_v020_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_126d_base_v021_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_189d_base_v022_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_252d_base_v023_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_378d_base_v024_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintens_504d_base_v025_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_5d_base_v026_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_10d_base_v027_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_21d_base_v028_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_42d_base_v029_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_63d_base_v030_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_126d_base_v031_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_189d_base_v032_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_252d_base_v033_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_378d_base_v034_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqual_504d_base_v035_signal(retearn, equity, closeadj):
    result = _f34_reinvestment_quality(retearn, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_63d_base_v036_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_126d_base_v037_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_252d_base_v038_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_504d_base_v039_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_21d_base_v040_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = _z(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthz_42d_base_v041_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 42)
    result = _z(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_63d_base_v042_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 63)
    result = _z(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_126d_base_v043_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 126)
    result = _z(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_252d_base_v044_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 252)
    result = _z(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_504d_base_v045_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 504)
    result = _z(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_21d_base_v046_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 21)
    result = _z(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualz_42d_base_v047_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 42)
    result = _z(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthema_21d_base_v048_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = _ema(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthema_63d_base_v049_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthema_126d_base_v050_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = _ema(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthema_252d_base_v051_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = _ema(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthema_504d_base_v052_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = _ema(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensc_21d_base_v053_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensc_63d_base_v054_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensc_126d_base_v055_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensc_252d_base_v056_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensc_504d_base_v057_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema_21d_base_v058_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 21)
    result = _ema(q, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema_63d_base_v059_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 63)
    result = _ema(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema_126d_base_v060_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 126)
    result = _ema(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema_252d_base_v061_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 252)
    result = _ema(q, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema_504d_base_v062_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 504)
    result = _ema(q, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_21d_base_v063_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_63d_base_v064_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_126d_base_v065_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_252d_base_v066_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_504d_base_v067_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxeq_42d_base_v068_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 42)
    result = g * equity / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_21d_base_v069_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 21)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_42d_base_v070_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 42)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_63d_base_v071_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 63)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_126d_base_v072_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 126)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_189d_base_v073_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 189)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_252d_base_v074_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 252)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgxintens_504d_base_v075_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 504)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _mean(ri, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34rtg_f34_reinvestment_to_growth_retgrowth_5d_base_v001_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_10d_base_v002_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_21d_base_v003_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_42d_base_v004_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_63d_base_v005_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_126d_base_v006_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_189d_base_v007_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_252d_base_v008_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_378d_base_v009_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowth_504d_base_v010_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthabs_21d_base_v011_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthabs_63d_base_v012_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthabs_126d_base_v013_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthabs_252d_base_v014_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthabs_504d_base_v015_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_5d_base_v016_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_10d_base_v017_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_21d_base_v018_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_42d_base_v019_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_63d_base_v020_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_126d_base_v021_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_189d_base_v022_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_252d_base_v023_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_378d_base_v024_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintens_504d_base_v025_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_5d_base_v026_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_10d_base_v027_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_21d_base_v028_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_42d_base_v029_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_63d_base_v030_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_126d_base_v031_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_189d_base_v032_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_252d_base_v033_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_378d_base_v034_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqual_504d_base_v035_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_63d_base_v036_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_126d_base_v037_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_252d_base_v038_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_504d_base_v039_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_21d_base_v040_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthz_42d_base_v041_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_63d_base_v042_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_126d_base_v043_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_252d_base_v044_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_504d_base_v045_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_21d_base_v046_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualz_42d_base_v047_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthema_21d_base_v048_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthema_63d_base_v049_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthema_126d_base_v050_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthema_252d_base_v051_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthema_504d_base_v052_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensc_21d_base_v053_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensc_63d_base_v054_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensc_126d_base_v055_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensc_252d_base_v056_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensc_504d_base_v057_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema_21d_base_v058_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema_63d_base_v059_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema_126d_base_v060_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema_252d_base_v061_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema_504d_base_v062_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_21d_base_v063_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_63d_base_v064_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_126d_base_v065_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_252d_base_v066_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_504d_base_v067_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxeq_42d_base_v068_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_21d_base_v069_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_42d_base_v070_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_63d_base_v071_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_126d_base_v072_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_189d_base_v073_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_252d_base_v074_signal,
    f34rtg_f34_reinvestment_to_growth_retgxintens_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_REINVESTMENT_TO_GROWTH_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f34_retained_growth", "_f34_reinvestment_intensity", "_f34_reinvestment_quality",)
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
    print(f"OK f34_reinvestment_to_growth_base_001_075_claude: {n_features} features pass")
