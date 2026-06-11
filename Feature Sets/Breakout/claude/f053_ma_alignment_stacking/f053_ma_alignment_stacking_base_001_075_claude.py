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
def _f053_ma_fast(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w // 2)).mean()


def _f053_ma_alignment(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    return (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()


def _f053_stacking_score(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    align = (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()
    return align * closeadj


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v001_signal(closeadj):
    result = _safe_div(_f053_ma_fast(closeadj, 5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v002_signal(closeadj):
    result = _safe_div(_f053_ma_fast(closeadj, 10), _mean(closeadj, 252)).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v003_signal(closeadj):
    result = np.tanh(_z(_f053_ma_fast(closeadj, 21), 63)) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean(), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v004_signal(closeadj):
    result = _mean(_f053_ma_fast(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v005_signal(closeadj):
    result = _std(_f053_ma_fast(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v006_signal(closeadj):
    result = _z(_f053_ma_fast(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v007_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 189)) * (_f053_ma_fast(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v008_signal(closeadj):
    result = np.sqrt((_f053_ma_fast(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v009_signal(closeadj):
    result = np.log1p(_safe_div(_f053_ma_fast(closeadj, 378), _mean(closeadj, 252)).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v010_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v011_signal(closeadj):
    result = _safe_div(_mean(_f053_ma_fast(closeadj, 5), max(2, 5 // 2)), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v012_signal(closeadj):
    result = _std(_f053_ma_fast(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v013_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v014_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v015_signal(closeadj):
    result = _z(_f053_ma_fast(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v016_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f053_ma_fast(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v017_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v018_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v019_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v020_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v021_signal(closeadj):
    result = _safe_div((_f053_ma_fast(closeadj, 5)).fillna(0).cumsum().diff(5), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252)) / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v022_signal(closeadj):
    result = _safe_div((_f053_ma_fast(closeadj, 10)).expanding(min_periods=5).mean(), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v023_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v024_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v025_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v026_signal(closeadj):
    result = _f053_ma_alignment(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v027_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v028_signal(closeadj):
    result = np.sign(_f053_ma_alignment(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v029_signal(closeadj):
    result = _mean(_f053_ma_alignment(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v030_signal(closeadj):
    result = _std(_f053_ma_alignment(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v031_signal(closeadj):
    result = _z(_f053_ma_alignment(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v032_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 189)) * (_f053_ma_alignment(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v033_signal(closeadj):
    result = np.sqrt((_f053_ma_alignment(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v034_signal(closeadj):
    result = np.log1p((_f053_ma_alignment(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v035_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v036_signal(closeadj):
    result = _mean(_f053_ma_alignment(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v037_signal(closeadj):
    result = _std(_f053_ma_alignment(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v038_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v039_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v040_signal(closeadj):
    result = _z(_f053_ma_alignment(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v041_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f053_ma_alignment(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v042_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v043_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v044_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v045_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v046_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v047_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v048_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v049_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v050_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v051_signal(closeadj):
    result = _f053_stacking_score(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v052_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v053_signal(closeadj):
    result = np.sign(_f053_stacking_score(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v054_signal(closeadj):
    result = _mean(_f053_stacking_score(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v055_signal(closeadj):
    result = _std(_f053_stacking_score(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v056_signal(closeadj):
    result = _z(_f053_stacking_score(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v057_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 189)) * (_f053_stacking_score(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v058_signal(closeadj):
    result = np.sqrt((_f053_stacking_score(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v059_signal(closeadj):
    result = np.log1p((_f053_stacking_score(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v060_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v061_signal(closeadj):
    result = _mean(_f053_stacking_score(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v062_signal(closeadj):
    result = _std(_f053_stacking_score(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v063_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v064_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v065_signal(closeadj):
    result = _z(_f053_stacking_score(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v066_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f053_stacking_score(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v067_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v068_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v069_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v070_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v071_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v072_signal(closeadj):
    result = _safe_div((_f053_stacking_score(closeadj, 10)).expanding(min_periods=5).mean(), _mean(closeadj, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v073_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v074_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v075_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v001_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v002_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v003_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v004_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v005_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v006_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v007_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v008_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v009_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v010_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v011_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v012_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v013_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v014_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v015_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v016_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v017_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v018_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v019_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v020_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v021_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v022_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v023_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v024_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v025_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v026_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v027_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v028_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v029_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v030_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v031_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v032_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v033_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v034_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v035_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v036_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v037_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v038_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v039_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v040_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v041_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v042_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v043_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v044_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v045_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v046_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v047_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v048_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v049_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v050_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v051_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v052_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v053_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v054_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v055_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v056_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v057_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v058_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v059_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v060_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v061_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v062_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v063_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v064_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v065_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v066_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v067_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v068_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v069_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v070_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v071_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v072_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v073_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v074_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F053_MA_ALIGNMENT_STACKING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f053_ma_fast', '_f053_ma_alignment', '_f053_stacking_score')
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
    print(f"OK f053_ma_alignment_stacking_base_001_075_claude: {n_features} features pass")
