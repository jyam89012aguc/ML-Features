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


def f45grr_f45_gambling_revenue_resilience_rs_5d_base_v001_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_10d_base_v002_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_21d_base_v003_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_42d_base_v004_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_63d_base_v005_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_126d_base_v006_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_189d_base_v007_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_252d_base_v008_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_378d_base_v009_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rs_504d_base_v010_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_5d_base_v011_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 5)
    result = _ema(s, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_10d_base_v012_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 10)
    result = _ema(s, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_21d_base_v013_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 21)
    result = _ema(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_42d_base_v014_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 42)
    result = _ema(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_63d_base_v015_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _ema(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_126d_base_v016_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 126)
    result = _ema(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_189d_base_v017_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 189)
    result = _ema(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_252d_base_v018_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    result = _ema(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_378d_base_v019_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 378)
    result = _ema(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsema_504d_base_v020_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    result = _ema(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_21d_base_v021_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_42d_base_v022_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_63d_base_v023_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_126d_base_v024_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_189d_base_v025_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_252d_base_v026_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_378d_base_v027_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsz_504d_base_v028_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_5d_base_v029_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_10d_base_v030_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_21d_base_v031_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_42d_base_v032_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_63d_base_v033_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_126d_base_v034_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_189d_base_v035_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_252d_base_v036_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_378d_base_v037_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_ms_504d_base_v038_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_5d_base_v039_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 5)
    result = _ema(s, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_10d_base_v040_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 10)
    result = _ema(s, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_21d_base_v041_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 21)
    result = _ema(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_42d_base_v042_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 42)
    result = _ema(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_63d_base_v043_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _ema(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_126d_base_v044_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 126)
    result = _ema(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_189d_base_v045_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 189)
    result = _ema(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_252d_base_v046_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    result = _ema(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_378d_base_v047_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 378)
    result = _ema(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msema_504d_base_v048_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    result = _ema(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_21d_base_v049_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_42d_base_v050_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_63d_base_v051_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_126d_base_v052_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_189d_base_v053_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_252d_base_v054_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_378d_base_v055_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msz_504d_base_v056_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_5d_base_v057_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 5)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_10d_base_v058_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 10)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_21d_base_v059_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 21)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_42d_base_v060_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 42)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_63d_base_v061_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_126d_base_v062_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 126)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_189d_base_v063_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 189)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_252d_base_v064_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 252)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_378d_base_v065_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 378)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gr_504d_base_v066_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 504)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_5d_base_v067_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 5)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_10d_base_v068_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 10)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_21d_base_v069_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 21)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_42d_base_v070_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 42)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_63d_base_v071_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_126d_base_v072_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 126)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_189d_base_v073_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 189)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_252d_base_v074_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 252)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grema_378d_base_v075_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 378)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45grr_f45_gambling_revenue_resilience_rs_5d_base_v001_signal,
    f45grr_f45_gambling_revenue_resilience_rs_10d_base_v002_signal,
    f45grr_f45_gambling_revenue_resilience_rs_21d_base_v003_signal,
    f45grr_f45_gambling_revenue_resilience_rs_42d_base_v004_signal,
    f45grr_f45_gambling_revenue_resilience_rs_63d_base_v005_signal,
    f45grr_f45_gambling_revenue_resilience_rs_126d_base_v006_signal,
    f45grr_f45_gambling_revenue_resilience_rs_189d_base_v007_signal,
    f45grr_f45_gambling_revenue_resilience_rs_252d_base_v008_signal,
    f45grr_f45_gambling_revenue_resilience_rs_378d_base_v009_signal,
    f45grr_f45_gambling_revenue_resilience_rs_504d_base_v010_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_5d_base_v011_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_10d_base_v012_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_21d_base_v013_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_42d_base_v014_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_63d_base_v015_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_126d_base_v016_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_189d_base_v017_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_252d_base_v018_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_378d_base_v019_signal,
    f45grr_f45_gambling_revenue_resilience_rsema_504d_base_v020_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_21d_base_v021_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_42d_base_v022_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_63d_base_v023_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_126d_base_v024_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_189d_base_v025_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_252d_base_v026_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_378d_base_v027_signal,
    f45grr_f45_gambling_revenue_resilience_rsz_504d_base_v028_signal,
    f45grr_f45_gambling_revenue_resilience_ms_5d_base_v029_signal,
    f45grr_f45_gambling_revenue_resilience_ms_10d_base_v030_signal,
    f45grr_f45_gambling_revenue_resilience_ms_21d_base_v031_signal,
    f45grr_f45_gambling_revenue_resilience_ms_42d_base_v032_signal,
    f45grr_f45_gambling_revenue_resilience_ms_63d_base_v033_signal,
    f45grr_f45_gambling_revenue_resilience_ms_126d_base_v034_signal,
    f45grr_f45_gambling_revenue_resilience_ms_189d_base_v035_signal,
    f45grr_f45_gambling_revenue_resilience_ms_252d_base_v036_signal,
    f45grr_f45_gambling_revenue_resilience_ms_378d_base_v037_signal,
    f45grr_f45_gambling_revenue_resilience_ms_504d_base_v038_signal,
    f45grr_f45_gambling_revenue_resilience_msema_5d_base_v039_signal,
    f45grr_f45_gambling_revenue_resilience_msema_10d_base_v040_signal,
    f45grr_f45_gambling_revenue_resilience_msema_21d_base_v041_signal,
    f45grr_f45_gambling_revenue_resilience_msema_42d_base_v042_signal,
    f45grr_f45_gambling_revenue_resilience_msema_63d_base_v043_signal,
    f45grr_f45_gambling_revenue_resilience_msema_126d_base_v044_signal,
    f45grr_f45_gambling_revenue_resilience_msema_189d_base_v045_signal,
    f45grr_f45_gambling_revenue_resilience_msema_252d_base_v046_signal,
    f45grr_f45_gambling_revenue_resilience_msema_378d_base_v047_signal,
    f45grr_f45_gambling_revenue_resilience_msema_504d_base_v048_signal,
    f45grr_f45_gambling_revenue_resilience_msz_21d_base_v049_signal,
    f45grr_f45_gambling_revenue_resilience_msz_42d_base_v050_signal,
    f45grr_f45_gambling_revenue_resilience_msz_63d_base_v051_signal,
    f45grr_f45_gambling_revenue_resilience_msz_126d_base_v052_signal,
    f45grr_f45_gambling_revenue_resilience_msz_189d_base_v053_signal,
    f45grr_f45_gambling_revenue_resilience_msz_252d_base_v054_signal,
    f45grr_f45_gambling_revenue_resilience_msz_378d_base_v055_signal,
    f45grr_f45_gambling_revenue_resilience_msz_504d_base_v056_signal,
    f45grr_f45_gambling_revenue_resilience_gr_5d_base_v057_signal,
    f45grr_f45_gambling_revenue_resilience_gr_10d_base_v058_signal,
    f45grr_f45_gambling_revenue_resilience_gr_21d_base_v059_signal,
    f45grr_f45_gambling_revenue_resilience_gr_42d_base_v060_signal,
    f45grr_f45_gambling_revenue_resilience_gr_63d_base_v061_signal,
    f45grr_f45_gambling_revenue_resilience_gr_126d_base_v062_signal,
    f45grr_f45_gambling_revenue_resilience_gr_189d_base_v063_signal,
    f45grr_f45_gambling_revenue_resilience_gr_252d_base_v064_signal,
    f45grr_f45_gambling_revenue_resilience_gr_378d_base_v065_signal,
    f45grr_f45_gambling_revenue_resilience_gr_504d_base_v066_signal,
    f45grr_f45_gambling_revenue_resilience_grema_5d_base_v067_signal,
    f45grr_f45_gambling_revenue_resilience_grema_10d_base_v068_signal,
    f45grr_f45_gambling_revenue_resilience_grema_21d_base_v069_signal,
    f45grr_f45_gambling_revenue_resilience_grema_42d_base_v070_signal,
    f45grr_f45_gambling_revenue_resilience_grema_63d_base_v071_signal,
    f45grr_f45_gambling_revenue_resilience_grema_126d_base_v072_signal,
    f45grr_f45_gambling_revenue_resilience_grema_189d_base_v073_signal,
    f45grr_f45_gambling_revenue_resilience_grema_252d_base_v074_signal,
    f45grr_f45_gambling_revenue_resilience_grema_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_GAMBLING_REVENUE_RESILIENCE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK gambling_revenue_resilience_base_001_075_claude: {n_features} features pass")
