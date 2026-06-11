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
def _f002_max_age(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    return age


def _f002_time_since_ath(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    tsa = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    return tsa / float(w)


def _f002_base_age_score(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = (close - ath) / ath.replace(0, np.nan).abs()
    return age * (1.0 + dd.abs())


def f002tsa_f002_time_since_ath_mage_5d_base_v001_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v002_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v003_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v004_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v005_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v006_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = ((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v007_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = ((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v008_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = ((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v009_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = ((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v010_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = ((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v011_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = ((base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v012_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = ((base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v013_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = ((base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v014_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = ((base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v015_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = ((base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_126d_base_v016_signal(closeadj):
    base = _f002_max_age(closeadj, 126)
    result = (np.sqrt((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_189d_base_v017_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 189)
    result = (np.sqrt((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_252d_base_v018_signal(closeadj):
    base = _f002_base_age_score(closeadj, 252)
    result = (np.sqrt((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_378d_base_v019_signal(closeadj):
    base = _f002_max_age(closeadj, 378)
    result = (np.sqrt((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_504d_base_v020_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 504)
    result = (np.sqrt((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_5d_base_v021_signal(closeadj):
    base = _f002_base_age_score(closeadj, 5)
    result = (np.log1p((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_10d_base_v022_signal(closeadj):
    base = _f002_max_age(closeadj, 10)
    result = (np.log1p((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_21d_base_v023_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 21)
    result = (np.log1p((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_42d_base_v024_signal(closeadj):
    base = _f002_base_age_score(closeadj, 42)
    result = (np.log1p((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_63d_base_v025_signal(closeadj):
    base = _f002_max_age(closeadj, 63)
    result = (np.log1p((base).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_126d_base_v026_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_189d_base_v027_signal(closeadj):
    base = _f002_base_age_score(closeadj, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_252d_base_v028_signal(closeadj):
    base = _f002_max_age(closeadj, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_378d_base_v029_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_504d_base_v030_signal(closeadj):
    base = _f002_base_age_score(closeadj, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_5d_base_v031_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v032_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v033_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v034_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v035_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v036_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v037_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v038_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v039_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v040_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v041_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = (np.tanh(_z(base, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v042_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = (np.tanh(_z(base, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v043_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = (np.tanh(_z(base, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v044_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = (np.tanh(_z(base, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v045_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = (np.tanh(_z(base, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_126d_base_v046_signal(closeadj):
    base = _f002_max_age(closeadj, 126)
    result = ((base).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_189d_base_v047_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 189)
    result = ((base).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_252d_base_v048_signal(closeadj):
    base = _f002_base_age_score(closeadj, 252)
    result = ((base).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_378d_base_v049_signal(closeadj):
    base = _f002_max_age(closeadj, 378)
    result = ((base).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_504d_base_v050_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 504)
    result = ((base).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_5d_base_v051_signal(closeadj):
    base = _f002_base_age_score(closeadj, 5)
    result = ((base).ewm(span=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_10d_base_v052_signal(closeadj):
    base = _f002_max_age(closeadj, 10)
    result = ((base).ewm(span=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_21d_base_v053_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 21)
    result = ((base).ewm(span=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_42d_base_v054_signal(closeadj):
    base = _f002_base_age_score(closeadj, 42)
    result = ((base).ewm(span=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_63d_base_v055_signal(closeadj):
    base = _f002_max_age(closeadj, 63)
    result = ((base).ewm(span=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_126d_base_v056_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 126)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_189d_base_v057_signal(closeadj):
    base = _f002_base_age_score(closeadj, 189)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_252d_base_v058_signal(closeadj):
    base = _f002_max_age(closeadj, 252)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_378d_base_v059_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 378)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_504d_base_v060_signal(closeadj):
    base = _f002_base_age_score(closeadj, 504)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_5d_base_v061_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v062_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v063_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v064_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v065_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v066_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v067_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v068_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v069_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v070_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = ((base).rolling(63, min_periods=max(1, 63 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v071_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v072_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v073_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v074_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v075_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f002tsa_f002_time_since_ath_mage_5d_base_v001_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v002_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v003_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v004_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v005_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v006_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v007_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v008_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v009_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v010_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v011_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v012_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v013_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v014_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v015_signal,
    f002tsa_f002_time_since_ath_mage_126d_base_v016_signal,
    f002tsa_f002_time_since_ath_tsa_189d_base_v017_signal,
    f002tsa_f002_time_since_ath_bas_252d_base_v018_signal,
    f002tsa_f002_time_since_ath_mage_378d_base_v019_signal,
    f002tsa_f002_time_since_ath_tsa_504d_base_v020_signal,
    f002tsa_f002_time_since_ath_bas_5d_base_v021_signal,
    f002tsa_f002_time_since_ath_mage_10d_base_v022_signal,
    f002tsa_f002_time_since_ath_tsa_21d_base_v023_signal,
    f002tsa_f002_time_since_ath_bas_42d_base_v024_signal,
    f002tsa_f002_time_since_ath_mage_63d_base_v025_signal,
    f002tsa_f002_time_since_ath_tsa_126d_base_v026_signal,
    f002tsa_f002_time_since_ath_bas_189d_base_v027_signal,
    f002tsa_f002_time_since_ath_mage_252d_base_v028_signal,
    f002tsa_f002_time_since_ath_tsa_378d_base_v029_signal,
    f002tsa_f002_time_since_ath_bas_504d_base_v030_signal,
    f002tsa_f002_time_since_ath_mage_5d_base_v031_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v032_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v033_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v034_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v035_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v036_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v037_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v038_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v039_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v040_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v041_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v042_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v043_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v044_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v045_signal,
    f002tsa_f002_time_since_ath_mage_126d_base_v046_signal,
    f002tsa_f002_time_since_ath_tsa_189d_base_v047_signal,
    f002tsa_f002_time_since_ath_bas_252d_base_v048_signal,
    f002tsa_f002_time_since_ath_mage_378d_base_v049_signal,
    f002tsa_f002_time_since_ath_tsa_504d_base_v050_signal,
    f002tsa_f002_time_since_ath_bas_5d_base_v051_signal,
    f002tsa_f002_time_since_ath_mage_10d_base_v052_signal,
    f002tsa_f002_time_since_ath_tsa_21d_base_v053_signal,
    f002tsa_f002_time_since_ath_bas_42d_base_v054_signal,
    f002tsa_f002_time_since_ath_mage_63d_base_v055_signal,
    f002tsa_f002_time_since_ath_tsa_126d_base_v056_signal,
    f002tsa_f002_time_since_ath_bas_189d_base_v057_signal,
    f002tsa_f002_time_since_ath_mage_252d_base_v058_signal,
    f002tsa_f002_time_since_ath_tsa_378d_base_v059_signal,
    f002tsa_f002_time_since_ath_bas_504d_base_v060_signal,
    f002tsa_f002_time_since_ath_mage_5d_base_v061_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v062_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v063_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v064_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v065_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v066_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v067_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v068_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v069_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v070_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v071_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v072_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v073_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v074_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F002_TIME_SINCE_ATH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f002_max_age", "_f002_time_since_ath", "_f002_base_age_score")
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
    print(f"OK f002_time_since_ath_base_001_075_claude: {n_features} features pass")
