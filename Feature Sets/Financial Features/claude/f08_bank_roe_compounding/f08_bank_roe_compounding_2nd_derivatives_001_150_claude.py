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


def _f08_roe_trajectory(roe, w):
    return roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f08_roe_persistence(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f08_roe_quality(roe, roa, w):
    spread = roe - roa
    return spread.rolling(w, min_periods=max(1, w // 2)).mean()


def f08roc_f08_bank_roe_compounding_roetraj_5d_slope_v001_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 5)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_10d_slope_v002_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 10)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_21d_slope_v003_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 21)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_42d_slope_v004_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 42)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_63d_slope_v005_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 63)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_126d_slope_v006_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 126)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_189d_slope_v007_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 189)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_252d_slope_v008_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 252)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_378d_slope_v009_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 378)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetraj_504d_slope_v010_signal(roe, closeadj):
    base = _f08_roe_trajectory(roe, 504)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_21d_slope_v011_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 21)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_63d_slope_v012_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 63)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_126d_slope_v013_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 126)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_252d_slope_v014_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 252)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepers_504d_slope_v015_signal(roe, closeadj):
    base = _f08_roe_persistence(roe, 504)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_5d_slope_v016_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 5)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_10d_slope_v017_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 10)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_21d_slope_v018_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 21)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_42d_slope_v019_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 42)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_63d_slope_v020_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 63)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_126d_slope_v021_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 126)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_189d_slope_v022_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 189)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_252d_slope_v023_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 252)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_378d_slope_v024_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 378)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequal_504d_slope_v025_signal(roe, roa, closeadj):
    base = _f08_roe_quality(roe, roa, 504)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_21d_slope_v026_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    base_series = _z(tr, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_63d_slope_v027_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = _z(tr, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_126d_slope_v028_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = _z(tr, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajz_252d_slope_v029_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = _z(tr, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_21d_slope_v030_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    base_series = _z(q, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_63d_slope_v031_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    base_series = _z(q, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_126d_slope_v032_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    base_series = _z(q, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalz_252d_slope_v033_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    base_series = _z(q, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_21d_slope_v034_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    base_series = _std(tr, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_63d_slope_v035_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = _std(tr, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_126d_slope_v036_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = _std(tr, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajstd_252d_slope_v037_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = _std(tr, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_63d_slope_v038_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    base_series = _std(p, 63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_126d_slope_v039_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    base_series = _std(p, 126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersstd_252d_slope_v040_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    base_series = _std(p, 252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_10d_slope_v041_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 10)
    base_series = _ema(tr, 10) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_21d_slope_v042_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    base_series = _ema(tr, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_63d_slope_v043_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = _ema(tr, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_126d_slope_v044_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = _ema(tr, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajema_252d_slope_v045_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = _ema(tr, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_10d_slope_v046_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 10)
    base_series = _ema(q, 10) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_21d_slope_v047_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    base_series = _ema(q, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_63d_slope_v048_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    base_series = _ema(q, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_126d_slope_v049_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    base_series = _ema(q, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalema_252d_slope_v050_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    base_series = _ema(q, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_5d_slope_v051_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 5)
    base_series = tr.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_21d_slope_v052_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    base_series = tr.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_63d_slope_v053_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = tr.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_126d_slope_v054_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = tr.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajchg_252d_slope_v055_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = tr.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_5d_slope_v056_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 5)
    base_series = q.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_21d_slope_v057_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    base_series = q.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_63d_slope_v058_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    base_series = q.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_126d_slope_v059_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    base_series = q.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalchg_252d_slope_v060_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    base_series = q.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_63d_slope_v061_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    rnk = p.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_126d_slope_v062_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    rnk = p.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersrank_252d_slope_v063_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    rnk = p.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_63d_slope_v064_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    rnk = tr.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_126d_slope_v065_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    rnk = tr.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajrank_252d_slope_v066_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    rnk = tr.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_63d_slope_v067_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    rnk = q.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_126d_slope_v068_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    rnk = q.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrank_252d_slope_v069_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    rnk = q.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_21d_slope_v070_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    p = _f08_roe_persistence(roe, 21)
    base_series = tr * p * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_63d_slope_v071_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    p = _f08_roe_persistence(roe, 63)
    base_series = tr * p * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_126d_slope_v072_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    p = _f08_roe_persistence(roe, 126)
    base_series = tr * p * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxpers_252d_slope_v073_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    p = _f08_roe_persistence(roe, 252)
    base_series = tr * p * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_21d_slope_v074_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    p = _f08_roe_persistence(roe, 21)
    base_series = q * p * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_63d_slope_v075_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    p = _f08_roe_persistence(roe, 63)
    base_series = q * p * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_126d_slope_v076_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    p = _f08_roe_persistence(roe, 126)
    base_series = q * p * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_252d_slope_v077_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    p = _f08_roe_persistence(roe, 252)
    base_series = q * p * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_21d_slope_v078_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21).abs()
    base_series = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_63d_slope_v079_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63).abs()
    base_series = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_252d_slope_v080_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252).abs()
    base_series = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_21d_slope_v081_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    rng = tr.rolling(21, min_periods=max(1, 21//2)).max() - tr.rolling(21, min_periods=max(1, 21//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_63d_slope_v082_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    rng = tr.rolling(63, min_periods=max(1, 63//2)).max() - tr.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_126d_slope_v083_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    rng = tr.rolling(126, min_periods=max(1, 126//2)).max() - tr.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_252d_slope_v084_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    rng = tr.rolling(252, min_periods=max(1, 252//2)).max() - tr.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_21v63_slope_v085_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 21)
    b = _f08_roe_trajectory(roe, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_21m63_slope_v086_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 21)
    b = _f08_roe_trajectory(roe, 63)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_63v252_slope_v087_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 63)
    b = _f08_roe_trajectory(roe, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_63m252_slope_v088_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 63)
    b = _f08_roe_trajectory(roe, 252)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_126v504_slope_v089_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 126)
    b = _f08_roe_trajectory(roe, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_126m504_slope_v090_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 126)
    b = _f08_roe_trajectory(roe, 504)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_42v189_slope_v091_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 42)
    b = _f08_roe_trajectory(roe, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_42m189_slope_v092_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 42)
    b = _f08_roe_trajectory(roe, 189)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_21d_slope_v093_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    base_series = (tr - _ema(tr, 21)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_63d_slope_v094_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = (tr - _ema(tr, 63)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_126d_slope_v095_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = (tr - _ema(tr, 126)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_252d_slope_v096_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = (tr - _ema(tr, 252)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersratio_63v252_slope_v097_signal(roe, closeadj):
    a = _f08_roe_persistence(roe, 63)
    b = _f08_roe_persistence(roe, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersratio_126v504_slope_v098_signal(roe, closeadj):
    a = _f08_roe_persistence(roe, 126)
    b = _f08_roe_persistence(roe, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_63d_slope_v099_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    rng = q.rolling(63, min_periods=max(1, 63//2)).max() - q.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_126d_slope_v100_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    rng = q.rolling(126, min_periods=max(1, 126//2)).max() - q.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_252d_slope_v101_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    rng = q.rolling(252, min_periods=max(1, 252//2)).max() - q.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_21d_slope_v102_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    e_chg = equity.pct_change(periods=21)
    base_series = tr * e_chg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_63d_slope_v103_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    e_chg = equity.pct_change(periods=63)
    base_series = tr * e_chg * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_126d_slope_v104_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    e_chg = equity.pct_change(periods=126)
    base_series = tr * e_chg * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_252d_slope_v105_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    e_chg = equity.pct_change(periods=252)
    base_series = tr * e_chg * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_504d_slope_v106_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    e_chg = equity.pct_change(periods=504)
    base_series = tr * e_chg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_21d_slope_v107_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    e_chg = equity.pct_change(periods=21)
    base_series = q * e_chg * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_63d_slope_v108_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    e_chg = equity.pct_change(periods=63)
    base_series = q * e_chg * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_126d_slope_v109_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    e_chg = equity.pct_change(periods=126)
    base_series = q * e_chg * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_252d_slope_v110_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    e_chg = equity.pct_change(periods=252)
    base_series = q * e_chg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_63d_slope_v111_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    base_series = (tr - tr.shift(63)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_126d_slope_v112_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    base_series = (tr - tr.shift(126)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_252d_slope_v113_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    base_series = (tr - tr.shift(252)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_504d_slope_v114_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    base_series = (tr - tr.shift(504)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_10d_slope_v115_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 10)
    base_series = _ema(p, 10) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_21d_slope_v116_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    base_series = _ema(p, 21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_63d_slope_v117_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    base_series = _ema(p, 63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_126d_slope_v118_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    base_series = _ema(p, 126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_252d_slope_v119_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    base_series = _ema(p, 252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_5d_slope_v120_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 5)
    base_series = p.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_21d_slope_v121_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    base_series = p.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_63d_slope_v122_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    base_series = p.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_126d_slope_v123_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    base_series = p.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_252d_slope_v124_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    base_series = p.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_21d_slope_v125_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    ra = _f08_roe_trajectory(roa, 21)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_42d_slope_v126_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 42)
    ra = _f08_roe_trajectory(roa, 42)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_63d_slope_v127_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    ra = _f08_roe_trajectory(roa, 63)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_126d_slope_v128_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    ra = _f08_roe_trajectory(roa, 126)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_189d_slope_v129_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 189)
    ra = _f08_roe_trajectory(roa, 189)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_252d_slope_v130_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    ra = _f08_roe_trajectory(roa, 252)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_378d_slope_v131_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 378)
    ra = _f08_roe_trajectory(roa, 378)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_504d_slope_v132_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    ra = _f08_roe_trajectory(roa, 504)
    base_series = (tr - ra) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_21d_slope_v133_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    ra = _f08_roe_trajectory(roa, 21)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_42d_slope_v134_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 42)
    ra = _f08_roe_trajectory(roa, 42)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_63d_slope_v135_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    ra = _f08_roe_trajectory(roa, 63)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_126d_slope_v136_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    ra = _f08_roe_trajectory(roa, 126)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_189d_slope_v137_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 189)
    ra = _f08_roe_trajectory(roa, 189)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_252d_slope_v138_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    ra = _f08_roe_trajectory(roa, 252)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_378d_slope_v139_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 378)
    ra = _f08_roe_trajectory(roa, 378)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_504d_slope_v140_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    ra = _f08_roe_trajectory(roa, 504)
    base_series = (tr / ra.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_21d_slope_v141_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    p = _f08_roe_persistence(roe, 21)
    base_series = _ema(q, 21) * p * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_42d_slope_v142_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 42)
    p = _f08_roe_persistence(roe, 42)
    base_series = _ema(q, 42) * p * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_63d_slope_v143_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    p = _f08_roe_persistence(roe, 63)
    base_series = _ema(q, 63) * p * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_126d_slope_v144_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    p = _f08_roe_persistence(roe, 126)
    base_series = _ema(q, 126) * p * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_189d_slope_v145_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 189)
    p = _f08_roe_persistence(roe, 189)
    base_series = _ema(q, 189) * p * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_252d_slope_v146_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    p = _f08_roe_persistence(roe, 252)
    base_series = _ema(q, 252) * p * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_21d_slope_v147_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    rv = _std(closeadj.pct_change(), 21)
    base_series = p * rv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_42d_slope_v148_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 42)
    rv = _std(closeadj.pct_change(), 42)
    base_series = p * rv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_63d_slope_v149_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    rv = _std(closeadj.pct_change(), 63)
    base_series = p * rv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_126d_slope_v150_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    rv = _std(closeadj.pct_change(), 126)
    base_series = p * rv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08roc_f08_bank_roe_compounding_roetraj_5d_slope_v001_signal,
    f08roc_f08_bank_roe_compounding_roetraj_10d_slope_v002_signal,
    f08roc_f08_bank_roe_compounding_roetraj_21d_slope_v003_signal,
    f08roc_f08_bank_roe_compounding_roetraj_42d_slope_v004_signal,
    f08roc_f08_bank_roe_compounding_roetraj_63d_slope_v005_signal,
    f08roc_f08_bank_roe_compounding_roetraj_126d_slope_v006_signal,
    f08roc_f08_bank_roe_compounding_roetraj_189d_slope_v007_signal,
    f08roc_f08_bank_roe_compounding_roetraj_252d_slope_v008_signal,
    f08roc_f08_bank_roe_compounding_roetraj_378d_slope_v009_signal,
    f08roc_f08_bank_roe_compounding_roetraj_504d_slope_v010_signal,
    f08roc_f08_bank_roe_compounding_roepers_21d_slope_v011_signal,
    f08roc_f08_bank_roe_compounding_roepers_63d_slope_v012_signal,
    f08roc_f08_bank_roe_compounding_roepers_126d_slope_v013_signal,
    f08roc_f08_bank_roe_compounding_roepers_252d_slope_v014_signal,
    f08roc_f08_bank_roe_compounding_roepers_504d_slope_v015_signal,
    f08roc_f08_bank_roe_compounding_roequal_5d_slope_v016_signal,
    f08roc_f08_bank_roe_compounding_roequal_10d_slope_v017_signal,
    f08roc_f08_bank_roe_compounding_roequal_21d_slope_v018_signal,
    f08roc_f08_bank_roe_compounding_roequal_42d_slope_v019_signal,
    f08roc_f08_bank_roe_compounding_roequal_63d_slope_v020_signal,
    f08roc_f08_bank_roe_compounding_roequal_126d_slope_v021_signal,
    f08roc_f08_bank_roe_compounding_roequal_189d_slope_v022_signal,
    f08roc_f08_bank_roe_compounding_roequal_252d_slope_v023_signal,
    f08roc_f08_bank_roe_compounding_roequal_378d_slope_v024_signal,
    f08roc_f08_bank_roe_compounding_roequal_504d_slope_v025_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_21d_slope_v026_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_63d_slope_v027_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_126d_slope_v028_signal,
    f08roc_f08_bank_roe_compounding_roetrajz_252d_slope_v029_signal,
    f08roc_f08_bank_roe_compounding_roequalz_21d_slope_v030_signal,
    f08roc_f08_bank_roe_compounding_roequalz_63d_slope_v031_signal,
    f08roc_f08_bank_roe_compounding_roequalz_126d_slope_v032_signal,
    f08roc_f08_bank_roe_compounding_roequalz_252d_slope_v033_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_21d_slope_v034_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_63d_slope_v035_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_126d_slope_v036_signal,
    f08roc_f08_bank_roe_compounding_roetrajstd_252d_slope_v037_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_63d_slope_v038_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_126d_slope_v039_signal,
    f08roc_f08_bank_roe_compounding_roepersstd_252d_slope_v040_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_10d_slope_v041_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_21d_slope_v042_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_63d_slope_v043_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_126d_slope_v044_signal,
    f08roc_f08_bank_roe_compounding_roetrajema_252d_slope_v045_signal,
    f08roc_f08_bank_roe_compounding_roequalema_10d_slope_v046_signal,
    f08roc_f08_bank_roe_compounding_roequalema_21d_slope_v047_signal,
    f08roc_f08_bank_roe_compounding_roequalema_63d_slope_v048_signal,
    f08roc_f08_bank_roe_compounding_roequalema_126d_slope_v049_signal,
    f08roc_f08_bank_roe_compounding_roequalema_252d_slope_v050_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_5d_slope_v051_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_21d_slope_v052_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_63d_slope_v053_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_126d_slope_v054_signal,
    f08roc_f08_bank_roe_compounding_roetrajchg_252d_slope_v055_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_5d_slope_v056_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_21d_slope_v057_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_63d_slope_v058_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_126d_slope_v059_signal,
    f08roc_f08_bank_roe_compounding_roequalchg_252d_slope_v060_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_63d_slope_v061_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_126d_slope_v062_signal,
    f08roc_f08_bank_roe_compounding_roepersrank_252d_slope_v063_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_63d_slope_v064_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_126d_slope_v065_signal,
    f08roc_f08_bank_roe_compounding_roetrajrank_252d_slope_v066_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_63d_slope_v067_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_126d_slope_v068_signal,
    f08roc_f08_bank_roe_compounding_roequalrank_252d_slope_v069_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_21d_slope_v070_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_63d_slope_v071_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_126d_slope_v072_signal,
    f08roc_f08_bank_roe_compounding_roetrajxpers_252d_slope_v073_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_21d_slope_v074_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_63d_slope_v075_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_126d_slope_v076_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_252d_slope_v077_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_21d_slope_v078_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_63d_slope_v079_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_252d_slope_v080_signal,
    f08roc_f08_bank_roe_compounding_roerange_21d_slope_v081_signal,
    f08roc_f08_bank_roe_compounding_roerange_63d_slope_v082_signal,
    f08roc_f08_bank_roe_compounding_roerange_126d_slope_v083_signal,
    f08roc_f08_bank_roe_compounding_roerange_252d_slope_v084_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_21v63_slope_v085_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_21m63_slope_v086_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_63v252_slope_v087_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_63m252_slope_v088_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_126v504_slope_v089_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_126m504_slope_v090_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_42v189_slope_v091_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_42m189_slope_v092_signal,
    f08roc_f08_bank_roe_compounding_roedev_21d_slope_v093_signal,
    f08roc_f08_bank_roe_compounding_roedev_63d_slope_v094_signal,
    f08roc_f08_bank_roe_compounding_roedev_126d_slope_v095_signal,
    f08roc_f08_bank_roe_compounding_roedev_252d_slope_v096_signal,
    f08roc_f08_bank_roe_compounding_roepersratio_63v252_slope_v097_signal,
    f08roc_f08_bank_roe_compounding_roepersratio_126v504_slope_v098_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_63d_slope_v099_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_126d_slope_v100_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_252d_slope_v101_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_21d_slope_v102_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_63d_slope_v103_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_126d_slope_v104_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_252d_slope_v105_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_504d_slope_v106_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_21d_slope_v107_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_63d_slope_v108_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_126d_slope_v109_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_252d_slope_v110_signal,
    f08roc_f08_bank_roe_compounding_roecompound_63d_slope_v111_signal,
    f08roc_f08_bank_roe_compounding_roecompound_126d_slope_v112_signal,
    f08roc_f08_bank_roe_compounding_roecompound_252d_slope_v113_signal,
    f08roc_f08_bank_roe_compounding_roecompound_504d_slope_v114_signal,
    f08roc_f08_bank_roe_compounding_roepersema_10d_slope_v115_signal,
    f08roc_f08_bank_roe_compounding_roepersema_21d_slope_v116_signal,
    f08roc_f08_bank_roe_compounding_roepersema_63d_slope_v117_signal,
    f08roc_f08_bank_roe_compounding_roepersema_126d_slope_v118_signal,
    f08roc_f08_bank_roe_compounding_roepersema_252d_slope_v119_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_5d_slope_v120_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_21d_slope_v121_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_63d_slope_v122_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_126d_slope_v123_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_252d_slope_v124_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_21d_slope_v125_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_42d_slope_v126_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_63d_slope_v127_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_126d_slope_v128_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_189d_slope_v129_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_252d_slope_v130_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_378d_slope_v131_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_504d_slope_v132_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_21d_slope_v133_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_42d_slope_v134_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_63d_slope_v135_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_126d_slope_v136_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_189d_slope_v137_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_252d_slope_v138_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_378d_slope_v139_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_504d_slope_v140_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_21d_slope_v141_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_42d_slope_v142_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_63d_slope_v143_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_126d_slope_v144_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_189d_slope_v145_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_252d_slope_v146_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_21d_slope_v147_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_42d_slope_v148_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_63d_slope_v149_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_126d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_BANK_ROE_COMPOUNDING_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f08_bank_roe_compounding_2nd_derivatives_001_150_claude: {n_features} features pass")
