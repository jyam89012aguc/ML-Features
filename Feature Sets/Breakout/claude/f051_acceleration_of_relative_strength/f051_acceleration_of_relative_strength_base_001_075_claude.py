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
def _f051_rs_rank_proxy(closeadj, w):
    r = closeadj.pct_change(w)
    return r.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _f051_rs_acceleration(closeadj, w):
    r = closeadj.pct_change(w)
    rk = r.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)
    return rk.diff(max(1, w // 3))


def _f051_emerging_leader(closeadj, w):
    r = closeadj.pct_change(w)
    rk = r.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)
    acc = rk.diff(max(1, w // 3))
    return rk * acc.abs() * closeadj


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v001_signal(closeadj):
    result = _f051_rs_rank_proxy(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v002_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v003_signal(closeadj):
    result = np.sign(_f051_rs_rank_proxy(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v004_signal(closeadj):
    result = _mean(_f051_rs_rank_proxy(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v005_signal(closeadj):
    result = _std(_f051_rs_rank_proxy(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_126d_base_v006_signal(closeadj):
    result = _z(_f051_rs_rank_proxy(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_189d_base_v007_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 189)) * (_f051_rs_rank_proxy(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_252d_base_v008_signal(closeadj):
    result = np.sqrt((_f051_rs_rank_proxy(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_378d_base_v009_signal(closeadj):
    result = np.log1p((_f051_rs_rank_proxy(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_504d_base_v010_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v011_signal(closeadj):
    result = _mean(_f051_rs_rank_proxy(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v012_signal(closeadj):
    result = _std(_f051_rs_rank_proxy(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v013_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v014_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v015_signal(closeadj):
    result = _z(_f051_rs_rank_proxy(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_126d_base_v016_signal(closeadj):
    result = ((_f051_rs_rank_proxy(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f051_rs_rank_proxy(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_189d_base_v017_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_252d_base_v018_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_378d_base_v019_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_504d_base_v020_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v021_signal(closeadj):
    result = ((_f051_rs_rank_proxy(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v022_signal(closeadj):
    result = ((_f051_rs_rank_proxy(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v023_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v024_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v025_signal(closeadj):
    result = (_f051_rs_rank_proxy(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v026_signal(closeadj):
    result = _f051_rs_acceleration(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v027_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v028_signal(closeadj):
    result = np.sign(_f051_rs_acceleration(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v029_signal(closeadj):
    result = _mean(_f051_rs_acceleration(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v030_signal(closeadj):
    result = _std(_f051_rs_acceleration(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_126d_base_v031_signal(closeadj):
    result = _z(_f051_rs_acceleration(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_189d_base_v032_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 189)) * (_f051_rs_acceleration(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_252d_base_v033_signal(closeadj):
    result = np.sqrt((_f051_rs_acceleration(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_378d_base_v034_signal(closeadj):
    result = np.log1p((_f051_rs_acceleration(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_504d_base_v035_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v036_signal(closeadj):
    result = _mean(_f051_rs_acceleration(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v037_signal(closeadj):
    result = _std(_f051_rs_acceleration(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v038_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v039_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v040_signal(closeadj):
    result = _z(_f051_rs_acceleration(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_126d_base_v041_signal(closeadj):
    result = ((_f051_rs_acceleration(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f051_rs_acceleration(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_189d_base_v042_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_252d_base_v043_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_378d_base_v044_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_504d_base_v045_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v046_signal(closeadj):
    result = ((_f051_rs_acceleration(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v047_signal(closeadj):
    result = ((_f051_rs_acceleration(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v048_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v049_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v050_signal(closeadj):
    result = (_f051_rs_acceleration(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v051_signal(closeadj):
    result = _f051_emerging_leader(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v052_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v053_signal(closeadj):
    result = np.sign(_f051_emerging_leader(closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v054_signal(closeadj):
    result = _mean(_f051_emerging_leader(closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v055_signal(closeadj):
    result = _std(_f051_emerging_leader(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_126d_base_v056_signal(closeadj):
    result = _z(_f051_emerging_leader(closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_189d_base_v057_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 189)) * (_f051_emerging_leader(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_252d_base_v058_signal(closeadj):
    result = np.sqrt((_f051_emerging_leader(closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_378d_base_v059_signal(closeadj):
    result = np.log1p((_f051_emerging_leader(closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_504d_base_v060_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v061_signal(closeadj):
    result = _mean(_f051_emerging_leader(closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v062_signal(closeadj):
    result = _std(_f051_emerging_leader(closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v063_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v064_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v065_signal(closeadj):
    result = _z(_f051_emerging_leader(closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_126d_base_v066_signal(closeadj):
    result = ((_f051_emerging_leader(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f051_emerging_leader(closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_189d_base_v067_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_252d_base_v068_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_378d_base_v069_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_504d_base_v070_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v071_signal(closeadj):
    result = ((_f051_emerging_leader(closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v072_signal(closeadj):
    result = ((_f051_emerging_leader(closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v073_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v074_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v075_signal(closeadj):
    result = (_f051_emerging_leader(closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v001_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v002_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v003_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v004_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v005_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_126d_base_v006_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_189d_base_v007_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_252d_base_v008_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_378d_base_v009_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_504d_base_v010_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v011_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v012_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v013_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v014_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v015_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_126d_base_v016_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_189d_base_v017_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_252d_base_v018_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_378d_base_v019_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_504d_base_v020_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_5d_base_v021_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_10d_base_v022_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_21d_base_v023_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_42d_base_v024_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_rank_proxy_63d_base_v025_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v026_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v027_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v028_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v029_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v030_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_126d_base_v031_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_189d_base_v032_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_252d_base_v033_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_378d_base_v034_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_504d_base_v035_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v036_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v037_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v038_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v039_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v040_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_126d_base_v041_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_189d_base_v042_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_252d_base_v043_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_378d_base_v044_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_504d_base_v045_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_5d_base_v046_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_10d_base_v047_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_21d_base_v048_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_42d_base_v049_signal,
    f051ars_f051_acceleration_of_relative_strength_rs_acceleration_63d_base_v050_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v051_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v052_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v053_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v054_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v055_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_126d_base_v056_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_189d_base_v057_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_252d_base_v058_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_378d_base_v059_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_504d_base_v060_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v061_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v062_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v063_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v064_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v065_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_126d_base_v066_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_189d_base_v067_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_252d_base_v068_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_378d_base_v069_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_504d_base_v070_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_5d_base_v071_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_10d_base_v072_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_21d_base_v073_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_42d_base_v074_signal,
    f051ars_f051_acceleration_of_relative_strength_emerging_leader_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F051_ACCELERATION_OF_RELATIVE_STRENGTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f051_rs_rank_proxy', '_f051_rs_acceleration', '_f051_emerging_leader')
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
    print(f"OK f051_acceleration_of_relative_strength_base_001_075_claude: {n_features} features pass")
