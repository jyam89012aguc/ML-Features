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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f45_revenue_smoothness(revenue, w):
    g = revenue.pct_change()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    m = g.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return m / sd.replace(0, np.nan)


def _f45_margin_stability(ebitdamargin, w):
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / sd.replace(0, np.nan)


def _f45_gaming_resilience_score(revenue, ebitda, w):
    g_rev = revenue.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    g_ebt = ebitda.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (g_rev.replace(0, np.nan) + g_ebt.replace(0, np.nan))


def f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v001_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v002_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v003_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v004_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v005_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v006_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v007_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v008_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v009_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v010_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v011_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v012_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v013_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v014_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v015_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v016_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v017_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v018_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v019_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v020_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v021_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v022_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v023_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v024_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v025_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v026_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v027_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v028_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v029_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v030_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v031_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v032_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v033_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v034_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v035_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v036_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v037_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v038_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v039_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v040_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v041_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v042_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v043_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v044_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v045_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v046_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v047_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v048_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v049_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v050_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v051_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v052_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v053_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v054_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v055_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v056_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v057_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v058_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v059_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v060_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v061_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v062_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v063_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v064_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v065_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v066_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v067_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v068_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v069_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v070_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v071_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v072_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v073_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v074_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v075_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v076_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v077_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v078_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v079_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v080_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v081_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v082_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v083_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v084_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    base = _z(s, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v085_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v086_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v087_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v088_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v089_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v090_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v091_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v092_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v093_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v094_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v095_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v096_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v097_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v098_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v099_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v100_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v101_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v102_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v103_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v104_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v105_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v106_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v107_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v108_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v109_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v110_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v111_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v112_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v113_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v114_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v115_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v116_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v117_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v118_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v119_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v120_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    base = _ema(s, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v121_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v122_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v123_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    base = _ema(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v124_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v125_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v126_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v127_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v128_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v129_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _ema(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v130_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v131_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v132_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v133_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v134_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v135_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    base = _ema(s, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v136_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v137_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v138_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v139_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v140_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v141_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    base = _ema(s, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v142_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v143_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v144_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    base = _ema(s, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v145_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v146_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v147_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v148_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v149_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v150_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    base = _z(s, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v001_signal,
    f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v002_signal,
    f45grr_f45_gambling_revenue_resilience_rs_5d_jerk_v003_signal,
    f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v004_signal,
    f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v005_signal,
    f45grr_f45_gambling_revenue_resilience_rs_10d_jerk_v006_signal,
    f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v007_signal,
    f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v008_signal,
    f45grr_f45_gambling_revenue_resilience_rs_21d_jerk_v009_signal,
    f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v010_signal,
    f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v011_signal,
    f45grr_f45_gambling_revenue_resilience_rs_42d_jerk_v012_signal,
    f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v013_signal,
    f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v014_signal,
    f45grr_f45_gambling_revenue_resilience_rs_63d_jerk_v015_signal,
    f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v016_signal,
    f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v017_signal,
    f45grr_f45_gambling_revenue_resilience_rs_126d_jerk_v018_signal,
    f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v019_signal,
    f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v020_signal,
    f45grr_f45_gambling_revenue_resilience_rs_189d_jerk_v021_signal,
    f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v022_signal,
    f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v023_signal,
    f45grr_f45_gambling_revenue_resilience_rs_252d_jerk_v024_signal,
    f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v025_signal,
    f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v026_signal,
    f45grr_f45_gambling_revenue_resilience_rs_378d_jerk_v027_signal,
    f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v028_signal,
    f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v029_signal,
    f45grr_f45_gambling_revenue_resilience_rs_504d_jerk_v030_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v031_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v032_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_5d_jerk_v033_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v034_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v035_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_10d_jerk_v036_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v037_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v038_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_21d_jerk_v039_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v040_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v041_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_42d_jerk_v042_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v043_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v044_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_63d_jerk_v045_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v046_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v047_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_126d_jerk_v048_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v049_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v050_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_189d_jerk_v051_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v052_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v053_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_252d_jerk_v054_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v055_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v056_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_378d_jerk_v057_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v058_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v059_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_504d_jerk_v060_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v061_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v062_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_21d_jerk_v063_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v064_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v065_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_42d_jerk_v066_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v067_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v068_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_63d_jerk_v069_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v070_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v071_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_126d_jerk_v072_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v073_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v074_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_189d_jerk_v075_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v076_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v077_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_252d_jerk_v078_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v079_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v080_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_378d_jerk_v081_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v082_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v083_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_504d_jerk_v084_signal,
    f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v085_signal,
    f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v086_signal,
    f45grr_f45_gambling_revenue_resilience_ms_5d_jerk_v087_signal,
    f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v088_signal,
    f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v089_signal,
    f45grr_f45_gambling_revenue_resilience_ms_10d_jerk_v090_signal,
    f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v091_signal,
    f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v092_signal,
    f45grr_f45_gambling_revenue_resilience_ms_21d_jerk_v093_signal,
    f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v094_signal,
    f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v095_signal,
    f45grr_f45_gambling_revenue_resilience_ms_42d_jerk_v096_signal,
    f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v097_signal,
    f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v098_signal,
    f45grr_f45_gambling_revenue_resilience_ms_63d_jerk_v099_signal,
    f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v100_signal,
    f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v101_signal,
    f45grr_f45_gambling_revenue_resilience_ms_126d_jerk_v102_signal,
    f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v103_signal,
    f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v104_signal,
    f45grr_f45_gambling_revenue_resilience_ms_189d_jerk_v105_signal,
    f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v106_signal,
    f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v107_signal,
    f45grr_f45_gambling_revenue_resilience_ms_252d_jerk_v108_signal,
    f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v109_signal,
    f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v110_signal,
    f45grr_f45_gambling_revenue_resilience_ms_378d_jerk_v111_signal,
    f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v112_signal,
    f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v113_signal,
    f45grr_f45_gambling_revenue_resilience_ms_504d_jerk_v114_signal,
    f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v115_signal,
    f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v116_signal,
    f45grr_f45_gambling_revenue_resilience_msema_5d_jerk_v117_signal,
    f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v118_signal,
    f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v119_signal,
    f45grr_f45_gambling_revenue_resilience_msema_10d_jerk_v120_signal,
    f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v121_signal,
    f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v122_signal,
    f45grr_f45_gambling_revenue_resilience_msema_21d_jerk_v123_signal,
    f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v124_signal,
    f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v125_signal,
    f45grr_f45_gambling_revenue_resilience_msema_42d_jerk_v126_signal,
    f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v127_signal,
    f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v128_signal,
    f45grr_f45_gambling_revenue_resilience_msema_63d_jerk_v129_signal,
    f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v130_signal,
    f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v131_signal,
    f45grr_f45_gambling_revenue_resilience_msema_126d_jerk_v132_signal,
    f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v133_signal,
    f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v134_signal,
    f45grr_f45_gambling_revenue_resilience_msema_189d_jerk_v135_signal,
    f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v136_signal,
    f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v137_signal,
    f45grr_f45_gambling_revenue_resilience_msema_252d_jerk_v138_signal,
    f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v139_signal,
    f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v140_signal,
    f45grr_f45_gambling_revenue_resilience_msema_378d_jerk_v141_signal,
    f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v142_signal,
    f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v143_signal,
    f45grr_f45_gambling_revenue_resilience_msema_504d_jerk_v144_signal,
    f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v145_signal,
    f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v146_signal,
    f45grr_f45_gambling_revenue_resilience_msz_21d_jerk_v147_signal,
    f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v148_signal,
    f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v149_signal,
    f45grr_f45_gambling_revenue_resilience_msz_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_GAMBLING_REVENUE_RESILIENCE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ebitda": ebitda, "ebitdamargin": ebitdamargin }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f45_revenue_smoothness", "_f45_margin_stability", "_f45_gaming_resilience_score")
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
    print(f"OK gambling_revenue_resilience_3rd_derivatives_001_150_claude: {n_features} features pass")
