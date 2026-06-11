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
def _f054_new_high_flag(closeadj, w):
    mx = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    prox = closeadj / mx.replace(0, np.nan)
    flag = (closeadj >= mx).astype(float)
    return (flag + prox) * closeadj


def _f054_new_high_count(closeadj, w):
    mx = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    flag = (closeadj >= mx).astype(float)
    return flag.rolling(w, min_periods=max(1, w // 2)).sum() * closeadj / (closeadj.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


def _f054_new_high_frequency(closeadj, w):
    mx = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    flag = (closeadj >= mx).astype(float)
    cnt = flag.rolling(w, min_periods=max(1, w // 2)).sum()
    return cnt / w * closeadj


def f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v001_signal(closeadj):
    result = _f054_new_high_flag(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v002_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v003_signal(closeadj):
    result = np.sign(_f054_new_high_flag(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v004_signal(closeadj):
    result = _mean(_f054_new_high_flag(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v005_signal(closeadj):
    result = _std(_f054_new_high_flag(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_126d_base_v006_signal(closeadj):
    result = _z(_f054_new_high_flag(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_189d_base_v007_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 189)) * (_f054_new_high_flag(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_252d_base_v008_signal(closeadj):
    result = np.sqrt((_f054_new_high_flag(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_378d_base_v009_signal(closeadj):
    result = np.log1p((_f054_new_high_flag(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_504d_base_v010_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v011_signal(closeadj):
    result = _mean(_f054_new_high_flag(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v012_signal(closeadj):
    result = _std(_f054_new_high_flag(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v013_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v014_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v015_signal(closeadj):
    result = _z(_f054_new_high_flag(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_126d_base_v016_signal(closeadj):
    result = ((_f054_new_high_flag(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f054_new_high_flag(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_189d_base_v017_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_252d_base_v018_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_378d_base_v019_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_504d_base_v020_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v021_signal(closeadj):
    result = ((_f054_new_high_flag(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v022_signal(closeadj):
    result = ((_f054_new_high_flag(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v023_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v024_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v025_signal(closeadj):
    result = (_f054_new_high_flag(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_5d_base_v026_signal(closeadj):
    result = _f054_new_high_count(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_10d_base_v027_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_21d_base_v028_signal(closeadj):
    result = np.sign(_f054_new_high_count(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_42d_base_v029_signal(closeadj):
    result = _mean(_f054_new_high_count(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_63d_base_v030_signal(closeadj):
    result = _std(_f054_new_high_count(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_126d_base_v031_signal(closeadj):
    result = _z(_f054_new_high_count(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_189d_base_v032_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 189)) * (_f054_new_high_count(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_252d_base_v033_signal(closeadj):
    result = np.sqrt((_f054_new_high_count(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_378d_base_v034_signal(closeadj):
    result = np.log1p((_f054_new_high_count(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_504d_base_v035_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_5d_base_v036_signal(closeadj):
    result = _mean(_f054_new_high_count(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_10d_base_v037_signal(closeadj):
    result = _std(_f054_new_high_count(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_21d_base_v038_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_42d_base_v039_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_63d_base_v040_signal(closeadj):
    result = _z(_f054_new_high_count(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_126d_base_v041_signal(closeadj):
    result = ((_f054_new_high_count(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f054_new_high_count(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_189d_base_v042_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_252d_base_v043_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_378d_base_v044_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_504d_base_v045_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_5d_base_v046_signal(closeadj):
    result = ((_f054_new_high_count(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_10d_base_v047_signal(closeadj):
    result = ((_f054_new_high_count(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_21d_base_v048_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_42d_base_v049_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_count_63d_base_v050_signal(closeadj):
    result = (_f054_new_high_count(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v051_signal(closeadj):
    result = _f054_new_high_frequency(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v052_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v053_signal(closeadj):
    result = np.sign(_f054_new_high_frequency(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v054_signal(closeadj):
    result = _mean(_f054_new_high_frequency(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v055_signal(closeadj):
    result = _std(_f054_new_high_frequency(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_126d_base_v056_signal(closeadj):
    result = _z(_f054_new_high_frequency(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_189d_base_v057_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 189)) * (_f054_new_high_frequency(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_252d_base_v058_signal(closeadj):
    result = np.sqrt((_f054_new_high_frequency(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_378d_base_v059_signal(closeadj):
    result = np.log1p((_f054_new_high_frequency(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_504d_base_v060_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v061_signal(closeadj):
    result = _mean(_f054_new_high_frequency(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v062_signal(closeadj):
    result = _std(_f054_new_high_frequency(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v063_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v064_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v065_signal(closeadj):
    result = _z(_f054_new_high_frequency(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_126d_base_v066_signal(closeadj):
    result = ((_f054_new_high_frequency(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f054_new_high_frequency(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_189d_base_v067_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_252d_base_v068_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_378d_base_v069_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_504d_base_v070_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v071_signal(closeadj):
    result = ((_f054_new_high_frequency(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v072_signal(closeadj):
    result = ((_f054_new_high_frequency(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v073_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v074_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v075_signal(closeadj):
    result = (_f054_new_high_frequency(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v001_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v002_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v003_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v004_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v005_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_126d_base_v006_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_189d_base_v007_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_252d_base_v008_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_378d_base_v009_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_504d_base_v010_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v011_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v012_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v013_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v014_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v015_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_126d_base_v016_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_189d_base_v017_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_252d_base_v018_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_378d_base_v019_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_504d_base_v020_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_5d_base_v021_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_10d_base_v022_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_21d_base_v023_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_42d_base_v024_signal,
    f054nhf_f054_new_high_frequency_new_high_flag_63d_base_v025_signal,
    f054nhf_f054_new_high_frequency_new_high_count_5d_base_v026_signal,
    f054nhf_f054_new_high_frequency_new_high_count_10d_base_v027_signal,
    f054nhf_f054_new_high_frequency_new_high_count_21d_base_v028_signal,
    f054nhf_f054_new_high_frequency_new_high_count_42d_base_v029_signal,
    f054nhf_f054_new_high_frequency_new_high_count_63d_base_v030_signal,
    f054nhf_f054_new_high_frequency_new_high_count_126d_base_v031_signal,
    f054nhf_f054_new_high_frequency_new_high_count_189d_base_v032_signal,
    f054nhf_f054_new_high_frequency_new_high_count_252d_base_v033_signal,
    f054nhf_f054_new_high_frequency_new_high_count_378d_base_v034_signal,
    f054nhf_f054_new_high_frequency_new_high_count_504d_base_v035_signal,
    f054nhf_f054_new_high_frequency_new_high_count_5d_base_v036_signal,
    f054nhf_f054_new_high_frequency_new_high_count_10d_base_v037_signal,
    f054nhf_f054_new_high_frequency_new_high_count_21d_base_v038_signal,
    f054nhf_f054_new_high_frequency_new_high_count_42d_base_v039_signal,
    f054nhf_f054_new_high_frequency_new_high_count_63d_base_v040_signal,
    f054nhf_f054_new_high_frequency_new_high_count_126d_base_v041_signal,
    f054nhf_f054_new_high_frequency_new_high_count_189d_base_v042_signal,
    f054nhf_f054_new_high_frequency_new_high_count_252d_base_v043_signal,
    f054nhf_f054_new_high_frequency_new_high_count_378d_base_v044_signal,
    f054nhf_f054_new_high_frequency_new_high_count_504d_base_v045_signal,
    f054nhf_f054_new_high_frequency_new_high_count_5d_base_v046_signal,
    f054nhf_f054_new_high_frequency_new_high_count_10d_base_v047_signal,
    f054nhf_f054_new_high_frequency_new_high_count_21d_base_v048_signal,
    f054nhf_f054_new_high_frequency_new_high_count_42d_base_v049_signal,
    f054nhf_f054_new_high_frequency_new_high_count_63d_base_v050_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v051_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v052_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v053_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v054_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v055_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_126d_base_v056_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_189d_base_v057_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_252d_base_v058_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_378d_base_v059_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_504d_base_v060_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v061_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v062_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v063_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v064_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v065_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_126d_base_v066_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_189d_base_v067_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_252d_base_v068_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_378d_base_v069_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_504d_base_v070_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_5d_base_v071_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_10d_base_v072_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_21d_base_v073_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_42d_base_v074_signal,
    f054nhf_f054_new_high_frequency_new_high_frequency_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F054_NEW_HIGH_FREQUENCY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f054_new_high_flag', '_f054_new_high_count', '_f054_new_high_frequency')
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
    print(f"OK f054_new_high_frequency_base_001_075_claude: {n_features} features pass")
