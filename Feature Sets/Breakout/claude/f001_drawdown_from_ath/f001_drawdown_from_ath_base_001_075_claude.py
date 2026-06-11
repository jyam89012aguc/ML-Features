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


def _drawdown(s, w):
    path_max = s.rolling(w, min_periods=1).max()
    return (s - path_max) / path_max.replace(0, np.nan)


def _rsi(s, w):
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w, min_periods=max(1, w // 2)).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w, min_periods=max(1, w // 2)).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


# ===== folder domain primitives =====


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v001_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v002_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v003_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v004_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v005_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v006_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v007_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v008_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v009_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v010_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v011_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v012_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v013_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v014_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v015_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base) * (base)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v016_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = np.sqrt((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v017_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = np.sqrt((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v018_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = np.sqrt((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v019_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = np.sqrt((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v020_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = np.sqrt((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v021_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = np.log1p((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v022_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = np.log1p((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v023_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = np.log1p((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v024_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = np.log1p((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v025_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = np.log1p((base).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v026_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v027_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v028_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v029_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v030_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v031_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v032_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v033_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v034_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v035_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v036_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v037_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v038_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v039_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v040_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v041_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = np.tanh(_z(base, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v042_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = np.tanh(_z(base, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v043_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = np.tanh(_z(base, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v044_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = np.tanh(_z(base, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v045_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = np.tanh(_z(base, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v046_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v047_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v048_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v049_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v050_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v051_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).ewm(span=21, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v052_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).ewm(span=21, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v053_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).ewm(span=21, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v054_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).ewm(span=21, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v055_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).ewm(span=21, adjust=False).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v056_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v057_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v058_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v059_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v060_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v061_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v062_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v063_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v064_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v065_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).median()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_126d_base_v066_signal(closeadj):
    base = _drawdown(closeadj, 126)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_189d_base_v067_signal(closeadj):
    base = _drawdown(closeadj, 189)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_252d_base_v068_signal(closeadj):
    base = _drawdown(closeadj, 252)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_378d_base_v069_signal(closeadj):
    base = _drawdown(closeadj, 378)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_504d_base_v070_signal(closeadj):
    base = _drawdown(closeadj, 504)
    result = (base).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_5d_base_v071_signal(closeadj):
    base = _drawdown(closeadj, 5)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_10d_base_v072_signal(closeadj):
    base = _drawdown(closeadj, 10)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_21d_base_v073_signal(closeadj):
    base = _drawdown(closeadj, 21)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_42d_base_v074_signal(closeadj):
    base = _drawdown(closeadj, 42)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_dd_63d_base_v075_signal(closeadj):
    base = _drawdown(closeadj, 63)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v001_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v002_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v003_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v004_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v005_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v006_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v007_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v008_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v009_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v010_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v011_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v012_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v013_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v014_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v015_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v016_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v017_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v018_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v019_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v020_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v021_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v022_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v023_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v024_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v025_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v026_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v027_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v028_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v029_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v030_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v031_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v032_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v033_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v034_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v035_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v036_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v037_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v038_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v039_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v040_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v041_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v042_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v043_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v044_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v045_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v046_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v047_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v048_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v049_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v050_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v051_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v052_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v053_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v054_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v055_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v056_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v057_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v058_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v059_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v060_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v061_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v062_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v063_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v064_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v065_signal,
    f001dfa_f001_drawdown_from_ath_dd_126d_base_v066_signal,
    f001dfa_f001_drawdown_from_ath_dd_189d_base_v067_signal,
    f001dfa_f001_drawdown_from_ath_dd_252d_base_v068_signal,
    f001dfa_f001_drawdown_from_ath_dd_378d_base_v069_signal,
    f001dfa_f001_drawdown_from_ath_dd_504d_base_v070_signal,
    f001dfa_f001_drawdown_from_ath_dd_5d_base_v071_signal,
    f001dfa_f001_drawdown_from_ath_dd_10d_base_v072_signal,
    f001dfa_f001_drawdown_from_ath_dd_21d_base_v073_signal,
    f001dfa_f001_drawdown_from_ath_dd_42d_base_v074_signal,
    f001dfa_f001_drawdown_from_ath_dd_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F001_DRAWDOWN_FROM_ATH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_drawdown",)
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
    print(f"OK f001_drawdown_from_ath_base_001_075_claude: {n_features} features pass")
