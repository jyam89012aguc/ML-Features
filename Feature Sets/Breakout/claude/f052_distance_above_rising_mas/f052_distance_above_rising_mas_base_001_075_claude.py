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
def _f052_ma_50(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w // 2)).mean()


def _f052_ma_150(closeadj, w):
    w_long = min(max(int(w * 1.5), 21), 252)
    return closeadj.rolling(w_long, min_periods=max(1, w_long // 2)).mean()


def _f052_above_rising_mas(closeadj, w):
    ma = closeadj.rolling(w, min_periods=max(1, w // 2)).mean()
    dist = (closeadj - ma) / ma.replace(0, np.nan).abs()
    rising = ma.diff(max(2, w // 4)) / ma.abs().replace(0, np.nan)
    return dist * rising * closeadj


def f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v001_signal(closeadj):
    result = _safe_div(_f052_ma_50(closeadj, 5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v002_signal(closeadj):
    result = _safe_div(_f052_ma_50(closeadj, 10), _mean(closeadj, 252)).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v003_signal(closeadj):
    result = np.tanh(_z(_f052_ma_50(closeadj, 21), 63)) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean(), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v004_signal(closeadj):
    result = _mean(_f052_ma_50(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v005_signal(closeadj):
    result = _std(_f052_ma_50(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_126d_base_v006_signal(closeadj):
    result = _z(_f052_ma_50(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_189d_base_v007_signal(closeadj):
    result = (_f052_ma_50(closeadj, 189)) * (_f052_ma_50(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_252d_base_v008_signal(closeadj):
    result = np.sqrt((_f052_ma_50(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_378d_base_v009_signal(closeadj):
    result = np.log1p(_safe_div(_f052_ma_50(closeadj, 378), _mean(closeadj, 252)).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_504d_base_v010_signal(closeadj):
    result = (_f052_ma_50(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v011_signal(closeadj):
    result = _safe_div(_mean(_f052_ma_50(closeadj, 5), max(2, 5 // 2)), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v012_signal(closeadj):
    result = _std(_f052_ma_50(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v013_signal(closeadj):
    result = (_f052_ma_50(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v014_signal(closeadj):
    result = (_f052_ma_50(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v015_signal(closeadj):
    result = _z(_f052_ma_50(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_126d_base_v016_signal(closeadj):
    result = ((_f052_ma_50(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f052_ma_50(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_189d_base_v017_signal(closeadj):
    result = (_f052_ma_50(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_252d_base_v018_signal(closeadj):
    result = (_f052_ma_50(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_378d_base_v019_signal(closeadj):
    result = (_f052_ma_50(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_504d_base_v020_signal(closeadj):
    result = (_f052_ma_50(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v021_signal(closeadj):
    result = _safe_div((_f052_ma_50(closeadj, 5)).fillna(0).cumsum().diff(5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252)) / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v022_signal(closeadj):
    result = _safe_div((_f052_ma_50(closeadj, 10)).expanding(min_periods=5).mean(), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v023_signal(closeadj):
    result = (_f052_ma_50(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v024_signal(closeadj):
    result = (_f052_ma_50(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v025_signal(closeadj):
    result = (_f052_ma_50(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v026_signal(closeadj):
    result = _safe_div(_f052_ma_150(closeadj, 5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v027_signal(closeadj):
    result = _safe_div(_f052_ma_150(closeadj, 10), _mean(closeadj, 252)).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v028_signal(closeadj):
    result = np.tanh(_z(_f052_ma_150(closeadj, 21), 63)) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean(), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v029_signal(closeadj):
    result = _mean(_f052_ma_150(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v030_signal(closeadj):
    result = _std(_f052_ma_150(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_126d_base_v031_signal(closeadj):
    result = _z(_f052_ma_150(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_189d_base_v032_signal(closeadj):
    result = (_f052_ma_150(closeadj, 189)) * (_f052_ma_150(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_252d_base_v033_signal(closeadj):
    result = np.sqrt((_f052_ma_150(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_378d_base_v034_signal(closeadj):
    result = np.log1p(_safe_div(_f052_ma_150(closeadj, 378), _mean(closeadj, 252)).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_504d_base_v035_signal(closeadj):
    result = (_f052_ma_150(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v036_signal(closeadj):
    result = _safe_div(_mean(_f052_ma_150(closeadj, 5), max(2, 5 // 2)), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v037_signal(closeadj):
    result = _std(_f052_ma_150(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v038_signal(closeadj):
    result = (_f052_ma_150(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v039_signal(closeadj):
    result = (_f052_ma_150(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v040_signal(closeadj):
    result = _z(_f052_ma_150(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_126d_base_v041_signal(closeadj):
    result = ((_f052_ma_150(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f052_ma_150(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_189d_base_v042_signal(closeadj):
    result = (_f052_ma_150(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_252d_base_v043_signal(closeadj):
    result = (_f052_ma_150(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_378d_base_v044_signal(closeadj):
    result = (_f052_ma_150(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_504d_base_v045_signal(closeadj):
    result = (_f052_ma_150(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v046_signal(closeadj):
    result = _safe_div((_f052_ma_150(closeadj, 5)).fillna(0).cumsum().diff(5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252)) / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v047_signal(closeadj):
    result = _safe_div((_f052_ma_150(closeadj, 10)).expanding(min_periods=5).mean(), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v048_signal(closeadj):
    result = (_f052_ma_150(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v049_signal(closeadj):
    result = (_f052_ma_150(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v050_signal(closeadj):
    result = (_f052_ma_150(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v051_signal(closeadj):
    result = _f052_above_rising_mas(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v052_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v053_signal(closeadj):
    result = np.sign(_f052_above_rising_mas(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v054_signal(closeadj):
    result = _mean(_f052_above_rising_mas(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v055_signal(closeadj):
    result = _std(_f052_above_rising_mas(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_126d_base_v056_signal(closeadj):
    result = _z(_f052_above_rising_mas(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_189d_base_v057_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 189)) * (_f052_above_rising_mas(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_252d_base_v058_signal(closeadj):
    result = np.sqrt((_f052_above_rising_mas(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_378d_base_v059_signal(closeadj):
    result = np.log1p((_f052_above_rising_mas(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_504d_base_v060_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v061_signal(closeadj):
    result = _mean(_f052_above_rising_mas(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v062_signal(closeadj):
    result = _std(_f052_above_rising_mas(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v063_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v064_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v065_signal(closeadj):
    result = _z(_f052_above_rising_mas(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_126d_base_v066_signal(closeadj):
    result = ((_f052_above_rising_mas(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f052_above_rising_mas(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_189d_base_v067_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_252d_base_v068_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_378d_base_v069_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_504d_base_v070_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v071_signal(closeadj):
    result = ((_f052_above_rising_mas(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v072_signal(closeadj):
    result = ((_f052_above_rising_mas(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v073_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v074_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v075_signal(closeadj):
    result = (_f052_above_rising_mas(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v001_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v002_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v003_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v004_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v005_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_126d_base_v006_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_189d_base_v007_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_252d_base_v008_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_378d_base_v009_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_504d_base_v010_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v011_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v012_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v013_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v014_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v015_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_126d_base_v016_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_189d_base_v017_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_252d_base_v018_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_378d_base_v019_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_504d_base_v020_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_5d_base_v021_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_10d_base_v022_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_21d_base_v023_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_42d_base_v024_signal,
    f052dam_f052_distance_above_rising_mas_ma_50_63d_base_v025_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v026_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v027_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v028_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v029_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v030_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_126d_base_v031_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_189d_base_v032_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_252d_base_v033_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_378d_base_v034_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_504d_base_v035_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v036_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v037_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v038_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v039_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v040_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_126d_base_v041_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_189d_base_v042_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_252d_base_v043_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_378d_base_v044_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_504d_base_v045_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_5d_base_v046_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_10d_base_v047_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_21d_base_v048_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_42d_base_v049_signal,
    f052dam_f052_distance_above_rising_mas_ma_150_63d_base_v050_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v051_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v052_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v053_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v054_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v055_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_126d_base_v056_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_189d_base_v057_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_252d_base_v058_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_378d_base_v059_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_504d_base_v060_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v061_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v062_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v063_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v064_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v065_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_126d_base_v066_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_189d_base_v067_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_252d_base_v068_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_378d_base_v069_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_504d_base_v070_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_5d_base_v071_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_10d_base_v072_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_21d_base_v073_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_42d_base_v074_signal,
    f052dam_f052_distance_above_rising_mas_above_rising_mas_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F052_DISTANCE_ABOVE_RISING_MAS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f052_ma_50', '_f052_ma_150', '_f052_above_rising_mas')
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
    print(f"OK f052_distance_above_rising_mas_base_001_075_claude: {n_features} features pass")
