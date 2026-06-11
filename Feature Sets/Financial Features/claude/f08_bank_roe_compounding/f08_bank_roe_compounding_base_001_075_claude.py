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


def _f08_roe_trajectory(roe, w):
    return roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f08_roe_persistence(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f08_roe_quality(roe, roa, w):
    spread = roe - roa
    return spread.rolling(w, min_periods=max(1, w // 2)).mean()


def f08roc_f08_bank_roe_compounding_roetraj_5d_base_v001_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_10d_base_v002_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_21d_base_v003_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_42d_base_v004_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_63d_base_v005_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_126d_base_v006_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_189d_base_v007_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_252d_base_v008_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_378d_base_v009_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_504d_base_v010_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_21d_base_v011_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_63d_base_v012_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_126d_base_v013_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_252d_base_v014_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_504d_base_v015_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_5d_base_v016_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_10d_base_v017_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_21d_base_v018_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_42d_base_v019_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_63d_base_v020_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_126d_base_v021_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_189d_base_v022_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_252d_base_v023_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_378d_base_v024_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_504d_base_v025_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_21d_base_v026_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    result = _z(tr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_63d_base_v027_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = _z(tr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_126d_base_v028_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = _z(tr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_252d_base_v029_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = _z(tr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_21d_base_v030_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    result = _z(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_63d_base_v031_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    result = _z(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_126d_base_v032_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    result = _z(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_252d_base_v033_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    result = _z(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_21d_base_v034_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    result = _std(tr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_63d_base_v035_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = _std(tr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_126d_base_v036_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = _std(tr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_252d_base_v037_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = _std(tr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_63d_base_v038_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    result = _std(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_126d_base_v039_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    result = _std(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_252d_base_v040_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    result = _std(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_10d_base_v041_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 10)
    result = _ema(tr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_21d_base_v042_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    result = _ema(tr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_63d_base_v043_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = _ema(tr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_126d_base_v044_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = _ema(tr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_252d_base_v045_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = _ema(tr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_10d_base_v046_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 10)
    result = _ema(q, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_21d_base_v047_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    result = _ema(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_63d_base_v048_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    result = _ema(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_126d_base_v049_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    result = _ema(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_252d_base_v050_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    result = _ema(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_5d_base_v051_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 5)
    result = tr.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_21d_base_v052_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    result = tr.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_63d_base_v053_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = tr.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_126d_base_v054_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = tr.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_252d_base_v055_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = tr.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_5d_base_v056_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 5)
    result = q.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_21d_base_v057_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    result = q.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_63d_base_v058_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    result = q.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_126d_base_v059_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    result = q.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_252d_base_v060_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    result = q.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_63d_base_v061_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    rnk = p.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_126d_base_v062_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    rnk = p.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_252d_base_v063_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    rnk = p.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_63d_base_v064_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    rnk = tr.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_126d_base_v065_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    rnk = tr.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_252d_base_v066_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    rnk = tr.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_63d_base_v067_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    rnk = q.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_126d_base_v068_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    rnk = q.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_252d_base_v069_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    rnk = q.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_21d_base_v070_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    p = _f08_roe_persistence(roe, 21)
    result = tr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_63d_base_v071_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    p = _f08_roe_persistence(roe, 63)
    result = tr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_126d_base_v072_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    p = _f08_roe_persistence(roe, 126)
    result = tr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_252d_base_v073_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    p = _f08_roe_persistence(roe, 252)
    result = tr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_21d_base_v074_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    p = _f08_roe_persistence(roe, 21)
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_63d_base_v075_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    p = _f08_roe_persistence(roe, 63)
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08roc_f08_bank_roe_compounding_roetraj_5d_base_v001_signal,
    f08roc_f08_bank_roe_compounding_roetraj_10d_base_v002_signal,
    f08roc_f08_bank_roe_compounding_roetraj_21d_base_v003_signal,
    f08roc_f08_bank_roe_compounding_roetraj_42d_base_v004_signal,
    f08roc_f08_bank_roe_compounding_roetraj_63d_base_v005_signal,
    f08roc_f08_bank_roe_compounding_roetraj_126d_base_v006_signal,
    f08roc_f08_bank_roe_compounding_roetraj_189d_base_v007_signal,
    f08roc_f08_bank_roe_compounding_roetraj_252d_base_v008_signal,
    f08roc_f08_bank_roe_compounding_roetraj_378d_base_v009_signal,
    f08roc_f08_bank_roe_compounding_roetraj_504d_base_v010_signal,
    f08roc_f08_bank_roe_compounding_roepers_21d_base_v011_signal,
    f08roc_f08_bank_roe_compounding_roepers_63d_base_v012_signal,
    f08roc_f08_bank_roe_compounding_roepers_126d_base_v013_signal,
    f08roc_f08_bank_roe_compounding_roepers_252d_base_v014_signal,
    f08roc_f08_bank_roe_compounding_roepers_504d_base_v015_signal,
    f08roc_f08_bank_roe_compounding_roequal_5d_base_v016_signal,
    f08roc_f08_bank_roe_compounding_roequal_10d_base_v017_signal,
    f08roc_f08_bank_roe_compounding_roequal_21d_base_v018_signal,
    f08roc_f08_bank_roe_compounding_roequal_42d_base_v019_signal,
    f08roc_f08_bank_roe_compounding_roequal_63d_base_v020_signal,
    f08roc_f08_bank_roe_compounding_roequal_126d_base_v021_signal,
    f08roc_f08_bank_roe_compounding_roequal_189d_base_v022_signal,
    f08roc_f08_bank_roe_compounding_roequal_252d_base_v023_signal,
    f08roc_f08_bank_roe_compounding_roequal_378d_base_v024_signal,
    f08roc_f08_bank_roe_compounding_roequal_504d_base_v025_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_21d_base_v026_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_63d_base_v027_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_126d_base_v028_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_252d_base_v029_signal,
    f08roc_f08_bank_roe_compounding_roequalz_21d_base_v030_signal,
    f08roc_f08_bank_roe_compounding_roequalz_63d_base_v031_signal,
    f08roc_f08_bank_roe_compounding_roequalz_126d_base_v032_signal,
    f08roc_f08_bank_roe_compounding_roequalz_252d_base_v033_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_21d_base_v034_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_63d_base_v035_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_126d_base_v036_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_252d_base_v037_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_63d_base_v038_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_126d_base_v039_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_252d_base_v040_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_10d_base_v041_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_21d_base_v042_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_63d_base_v043_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_126d_base_v044_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_252d_base_v045_signal,
    f08roc_f08_bank_roe_compounding_roequalema_10d_base_v046_signal,
    f08roc_f08_bank_roe_compounding_roequalema_21d_base_v047_signal,
    f08roc_f08_bank_roe_compounding_roequalema_63d_base_v048_signal,
    f08roc_f08_bank_roe_compounding_roequalema_126d_base_v049_signal,
    f08roc_f08_bank_roe_compounding_roequalema_252d_base_v050_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_5d_base_v051_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_21d_base_v052_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_63d_base_v053_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_126d_base_v054_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_252d_base_v055_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_5d_base_v056_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_21d_base_v057_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_63d_base_v058_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_126d_base_v059_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_252d_base_v060_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_63d_base_v061_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_126d_base_v062_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_252d_base_v063_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_63d_base_v064_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_126d_base_v065_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_252d_base_v066_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_63d_base_v067_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_126d_base_v068_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_252d_base_v069_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_21d_base_v070_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_63d_base_v071_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_126d_base_v072_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_252d_base_v073_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_21d_base_v074_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_BANK_ROE_COMPOUNDING_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f08_roe_trajectory', '_f08_roe_persistence', '_f08_roe_quality')
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
    print(f"OK f08_bank_roe_compounding_base_001_075_claude: {n_features} features pass")
