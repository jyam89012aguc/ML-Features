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
def _f24_return_durability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f24_return_stability(roe, roic, w):
    diff = (roe - roic)
    sd = diff.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / sd.replace(0, np.nan)


def _f24_quality_compound(roic, roe, w):
    avg = (roic + roe) / 2.0
    return avg.rolling(w, min_periods=max(1, w // 2)).mean()

def f24sfq_f24_specialty_finance_quality_durab_5d_xclose_base_v001_signal(roic, closeadj):
    base = _f24_return_durability(roic, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_10d_xclose_base_v002_signal(roic, closeadj):
    base = _f24_return_durability(roic, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_21d_xclose_base_v003_signal(roic, closeadj):
    base = _f24_return_durability(roic, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_42d_xclose_base_v004_signal(roic, closeadj):
    base = _f24_return_durability(roic, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_63d_xclose_base_v005_signal(roic, closeadj):
    base = _f24_return_durability(roic, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_126d_xclose_base_v006_signal(roic, closeadj):
    base = _f24_return_durability(roic, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_189d_xclose_base_v007_signal(roic, closeadj):
    base = _f24_return_durability(roic, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_252d_xclose_base_v008_signal(roic, closeadj):
    base = _f24_return_durability(roic, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_378d_xclose_base_v009_signal(roic, closeadj):
    base = _f24_return_durability(roic, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durab_504d_xclose_base_v010_signal(roic, closeadj):
    base = _f24_return_durability(roic, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_5d_xclose_base_v011_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_10d_xclose_base_v012_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_21d_xclose_base_v013_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_42d_xclose_base_v014_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_63d_xclose_base_v015_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_126d_xclose_base_v016_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_189d_xclose_base_v017_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_252d_xclose_base_v018_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_378d_xclose_base_v019_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabil_504d_xclose_base_v020_signal(roic, roe, closeadj):
    base = _f24_return_stability(roe, roic, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_5d_xclose_base_v021_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_10d_xclose_base_v022_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_21d_xclose_base_v023_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_42d_xclose_base_v024_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_63d_xclose_base_v025_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_126d_xclose_base_v026_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_189d_xclose_base_v027_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_252d_xclose_base_v028_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_378d_xclose_base_v029_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcomp_504d_xclose_base_v030_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_5d_xclose_base_v031_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 5), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_10d_xclose_base_v032_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 10), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_21d_xclose_base_v033_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_42d_xclose_base_v034_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 42), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_63d_xclose_base_v035_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_126d_xclose_base_v036_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_189d_xclose_base_v037_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 189), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_252d_xclose_base_v038_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_378d_xclose_base_v039_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 378), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabz_504d_xclose_base_v040_signal(roic, closeadj):
    base = _z(_f24_return_durability(roic, 504), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_5d_xclose_base_v041_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 5), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_10d_xclose_base_v042_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 10), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_21d_xclose_base_v043_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_42d_xclose_base_v044_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 42), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_63d_xclose_base_v045_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_126d_xclose_base_v046_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_189d_xclose_base_v047_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 189), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_252d_xclose_base_v048_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_378d_xclose_base_v049_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 378), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompmean_504d_xclose_base_v050_signal(roic, roe, closeadj):
    base = _mean(_f24_quality_compound(roic, roe, 504), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_5d_xclose_base_v051_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 5), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_10d_xclose_base_v052_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 10), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_21d_xclose_base_v053_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_42d_xclose_base_v054_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 42), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_63d_xclose_base_v055_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_126d_xclose_base_v056_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_189d_xclose_base_v057_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 189), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_252d_xclose_base_v058_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_378d_xclose_base_v059_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 378), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_durabstd_504d_xclose_base_v060_signal(roic, closeadj):
    base = _std(_f24_return_durability(roic, 504), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_5d_xclose_base_v061_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 5), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_10d_xclose_base_v062_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 10), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_21d_xclose_base_v063_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_42d_xclose_base_v064_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 42), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_63d_xclose_base_v065_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_126d_xclose_base_v066_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_189d_xclose_base_v067_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 189), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_252d_xclose_base_v068_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_378d_xclose_base_v069_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 378), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_stabilmean_504d_xclose_base_v070_signal(roic, roe, closeadj):
    base = _mean(_f24_return_stability(roe, roic, 504), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompema_5d_xclose_base_v071_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 5).ewm(span=5, min_periods=max(1,5//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompema_10d_xclose_base_v072_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 10).ewm(span=10, min_periods=max(1,10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompema_21d_xclose_base_v073_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 21).ewm(span=21, min_periods=max(1,21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompema_42d_xclose_base_v074_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 42).ewm(span=42, min_periods=max(1,42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24sfq_f24_specialty_finance_quality_qcompema_63d_xclose_base_v075_signal(roic, roe, closeadj):
    base = _f24_quality_compound(roic, roe, 63).ewm(span=63, min_periods=max(1,63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f24sfq_f24_specialty_finance_quality_durab_5d_xclose_base_v001_signal,
    f24sfq_f24_specialty_finance_quality_durab_10d_xclose_base_v002_signal,
    f24sfq_f24_specialty_finance_quality_durab_21d_xclose_base_v003_signal,
    f24sfq_f24_specialty_finance_quality_durab_42d_xclose_base_v004_signal,
    f24sfq_f24_specialty_finance_quality_durab_63d_xclose_base_v005_signal,
    f24sfq_f24_specialty_finance_quality_durab_126d_xclose_base_v006_signal,
    f24sfq_f24_specialty_finance_quality_durab_189d_xclose_base_v007_signal,
    f24sfq_f24_specialty_finance_quality_durab_252d_xclose_base_v008_signal,
    f24sfq_f24_specialty_finance_quality_durab_378d_xclose_base_v009_signal,
    f24sfq_f24_specialty_finance_quality_durab_504d_xclose_base_v010_signal,
    f24sfq_f24_specialty_finance_quality_stabil_5d_xclose_base_v011_signal,
    f24sfq_f24_specialty_finance_quality_stabil_10d_xclose_base_v012_signal,
    f24sfq_f24_specialty_finance_quality_stabil_21d_xclose_base_v013_signal,
    f24sfq_f24_specialty_finance_quality_stabil_42d_xclose_base_v014_signal,
    f24sfq_f24_specialty_finance_quality_stabil_63d_xclose_base_v015_signal,
    f24sfq_f24_specialty_finance_quality_stabil_126d_xclose_base_v016_signal,
    f24sfq_f24_specialty_finance_quality_stabil_189d_xclose_base_v017_signal,
    f24sfq_f24_specialty_finance_quality_stabil_252d_xclose_base_v018_signal,
    f24sfq_f24_specialty_finance_quality_stabil_378d_xclose_base_v019_signal,
    f24sfq_f24_specialty_finance_quality_stabil_504d_xclose_base_v020_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_5d_xclose_base_v021_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_10d_xclose_base_v022_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_21d_xclose_base_v023_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_42d_xclose_base_v024_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_63d_xclose_base_v025_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_126d_xclose_base_v026_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_189d_xclose_base_v027_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_252d_xclose_base_v028_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_378d_xclose_base_v029_signal,
    f24sfq_f24_specialty_finance_quality_qcomp_504d_xclose_base_v030_signal,
    f24sfq_f24_specialty_finance_quality_durabz_5d_xclose_base_v031_signal,
    f24sfq_f24_specialty_finance_quality_durabz_10d_xclose_base_v032_signal,
    f24sfq_f24_specialty_finance_quality_durabz_21d_xclose_base_v033_signal,
    f24sfq_f24_specialty_finance_quality_durabz_42d_xclose_base_v034_signal,
    f24sfq_f24_specialty_finance_quality_durabz_63d_xclose_base_v035_signal,
    f24sfq_f24_specialty_finance_quality_durabz_126d_xclose_base_v036_signal,
    f24sfq_f24_specialty_finance_quality_durabz_189d_xclose_base_v037_signal,
    f24sfq_f24_specialty_finance_quality_durabz_252d_xclose_base_v038_signal,
    f24sfq_f24_specialty_finance_quality_durabz_378d_xclose_base_v039_signal,
    f24sfq_f24_specialty_finance_quality_durabz_504d_xclose_base_v040_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_5d_xclose_base_v041_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_10d_xclose_base_v042_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_21d_xclose_base_v043_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_42d_xclose_base_v044_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_63d_xclose_base_v045_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_126d_xclose_base_v046_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_189d_xclose_base_v047_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_252d_xclose_base_v048_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_378d_xclose_base_v049_signal,
    f24sfq_f24_specialty_finance_quality_qcompmean_504d_xclose_base_v050_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_5d_xclose_base_v051_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_10d_xclose_base_v052_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_21d_xclose_base_v053_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_42d_xclose_base_v054_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_63d_xclose_base_v055_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_126d_xclose_base_v056_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_189d_xclose_base_v057_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_252d_xclose_base_v058_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_378d_xclose_base_v059_signal,
    f24sfq_f24_specialty_finance_quality_durabstd_504d_xclose_base_v060_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_5d_xclose_base_v061_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_10d_xclose_base_v062_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_21d_xclose_base_v063_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_42d_xclose_base_v064_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_63d_xclose_base_v065_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_126d_xclose_base_v066_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_189d_xclose_base_v067_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_252d_xclose_base_v068_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_378d_xclose_base_v069_signal,
    f24sfq_f24_specialty_finance_quality_stabilmean_504d_xclose_base_v070_signal,
    f24sfq_f24_specialty_finance_quality_qcompema_5d_xclose_base_v071_signal,
    f24sfq_f24_specialty_finance_quality_qcompema_10d_xclose_base_v072_signal,
    f24sfq_f24_specialty_finance_quality_qcompema_21d_xclose_base_v073_signal,
    f24sfq_f24_specialty_finance_quality_qcompema_42d_xclose_base_v074_signal,
    f24sfq_f24_specialty_finance_quality_qcompema_63d_xclose_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_SPECIALTY_FINANCE_QUALITY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f24_return_durability", "_f24_return_stability", "_f24_quality_compound")
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
    print(f"OK f24_specialty_finance_quality: {n_features} features pass")
