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
def _f055_dm_plus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    return dmp.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_dm_minus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    return dmn.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_adx(high, low, closeadj, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    dip = dmp.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    din = dmn.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    dx = (dip - din).abs() / (dip + din).replace(0, np.nan)
    return dx.rolling(w, min_periods=max(1, w // 2)).mean() * closeadj


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v001_signal(high, low, closeadj):
    result = _f055_dm_plus(high, low, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v002_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v003_signal(high, low, closeadj):
    result = np.sign(_f055_dm_plus(high, low, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v004_signal(high, low, closeadj):
    result = _mean(_f055_dm_plus(high, low, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v005_signal(high, low, closeadj):
    result = _std(_f055_dm_plus(high, low, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_base_v006_signal(high, low, closeadj):
    result = _z(_f055_dm_plus(high, low, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_189d_base_v007_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 189)) * (_f055_dm_plus(high, low, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_base_v008_signal(high, low, closeadj):
    result = np.sqrt((_f055_dm_plus(high, low, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_378d_base_v009_signal(high, low, closeadj):
    result = np.log1p((_f055_dm_plus(high, low, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_504d_base_v010_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v011_signal(high, low, closeadj):
    result = _mean(_f055_dm_plus(high, low, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v012_signal(high, low, closeadj):
    result = _std(_f055_dm_plus(high, low, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v013_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v014_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v015_signal(high, low, closeadj):
    result = _z(_f055_dm_plus(high, low, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_base_v016_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f055_dm_plus(high, low, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_189d_base_v017_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_base_v018_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_378d_base_v019_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_504d_base_v020_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v021_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v022_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v023_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v024_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v025_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v026_signal(high, low, closeadj):
    result = _f055_dm_minus(high, low, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v027_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v028_signal(high, low, closeadj):
    result = np.sign(_f055_dm_minus(high, low, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v029_signal(high, low, closeadj):
    result = _mean(_f055_dm_minus(high, low, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v030_signal(high, low, closeadj):
    result = _std(_f055_dm_minus(high, low, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_base_v031_signal(high, low, closeadj):
    result = _z(_f055_dm_minus(high, low, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_189d_base_v032_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 189)) * (_f055_dm_minus(high, low, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_base_v033_signal(high, low, closeadj):
    result = np.sqrt((_f055_dm_minus(high, low, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_378d_base_v034_signal(high, low, closeadj):
    result = np.log1p((_f055_dm_minus(high, low, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_504d_base_v035_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v036_signal(high, low, closeadj):
    result = _mean(_f055_dm_minus(high, low, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v037_signal(high, low, closeadj):
    result = _std(_f055_dm_minus(high, low, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v038_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v039_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v040_signal(high, low, closeadj):
    result = _z(_f055_dm_minus(high, low, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_base_v041_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f055_dm_minus(high, low, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_189d_base_v042_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_base_v043_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_378d_base_v044_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_504d_base_v045_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v046_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v047_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v048_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v049_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v050_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v051_signal(high, low, closeadj):
    result = _f055_adx(high, low, closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v052_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v053_signal(high, low, closeadj):
    result = np.sign(_f055_adx(high, low, closeadj, 21)) * closeadj * closeadj.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v054_signal(high, low, closeadj):
    result = _mean(_f055_adx(high, low, closeadj, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v055_signal(high, low, closeadj):
    result = _std(_f055_adx(high, low, closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_base_v056_signal(high, low, closeadj):
    result = _z(_f055_adx(high, low, closeadj, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_189d_base_v057_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 189)) * (_f055_adx(high, low, closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_base_v058_signal(high, low, closeadj):
    result = np.sqrt((_f055_adx(high, low, closeadj, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_378d_base_v059_signal(high, low, closeadj):
    result = np.log1p((_f055_adx(high, low, closeadj, 378)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_504d_base_v060_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 504)).diff(max(2, 504 // 4)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v061_signal(high, low, closeadj):
    result = _mean(_f055_adx(high, low, closeadj, 5), max(2, 5 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v062_signal(high, low, closeadj):
    result = _std(_f055_adx(high, low, closeadj, 10), max(2, 10 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v063_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v064_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 42)).ewm(span=42, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v065_signal(high, low, closeadj):
    result = _z(_f055_adx(high, low, closeadj, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_base_v066_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() - (_f055_adx(high, low, closeadj, 126)).rolling(126, min_periods=max(1, 126 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_189d_base_v067_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 189)).rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_base_v068_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 252)).rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_378d_base_v069_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_504d_base_v070_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v071_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 5)).fillna(0).cumsum().diff(5)) * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v072_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 10)).expanding(min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v073_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 21)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v074_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 42)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v075_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v001_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v002_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v003_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v004_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v005_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_base_v006_signal,
    f055ats_f055_adx_trend_strength_dm_plus_189d_base_v007_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_base_v008_signal,
    f055ats_f055_adx_trend_strength_dm_plus_378d_base_v009_signal,
    f055ats_f055_adx_trend_strength_dm_plus_504d_base_v010_signal,
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v011_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v012_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v013_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v014_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v015_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_base_v016_signal,
    f055ats_f055_adx_trend_strength_dm_plus_189d_base_v017_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_base_v018_signal,
    f055ats_f055_adx_trend_strength_dm_plus_378d_base_v019_signal,
    f055ats_f055_adx_trend_strength_dm_plus_504d_base_v020_signal,
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v021_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v022_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v023_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v024_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v025_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v026_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v027_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v028_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v029_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v030_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_base_v031_signal,
    f055ats_f055_adx_trend_strength_dm_minus_189d_base_v032_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_base_v033_signal,
    f055ats_f055_adx_trend_strength_dm_minus_378d_base_v034_signal,
    f055ats_f055_adx_trend_strength_dm_minus_504d_base_v035_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v036_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v037_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v038_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v039_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v040_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_base_v041_signal,
    f055ats_f055_adx_trend_strength_dm_minus_189d_base_v042_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_base_v043_signal,
    f055ats_f055_adx_trend_strength_dm_minus_378d_base_v044_signal,
    f055ats_f055_adx_trend_strength_dm_minus_504d_base_v045_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v046_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v047_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v048_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v049_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v050_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v051_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v052_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v053_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v054_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v055_signal,
    f055ats_f055_adx_trend_strength_adx_126d_base_v056_signal,
    f055ats_f055_adx_trend_strength_adx_189d_base_v057_signal,
    f055ats_f055_adx_trend_strength_adx_252d_base_v058_signal,
    f055ats_f055_adx_trend_strength_adx_378d_base_v059_signal,
    f055ats_f055_adx_trend_strength_adx_504d_base_v060_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v061_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v062_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v063_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v064_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v065_signal,
    f055ats_f055_adx_trend_strength_adx_126d_base_v066_signal,
    f055ats_f055_adx_trend_strength_adx_189d_base_v067_signal,
    f055ats_f055_adx_trend_strength_adx_252d_base_v068_signal,
    f055ats_f055_adx_trend_strength_adx_378d_base_v069_signal,
    f055ats_f055_adx_trend_strength_adx_504d_base_v070_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v071_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v072_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v073_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v074_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F055_ADX_TREND_STRENGTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    cols = {"closeadj": closeadj, "high": high, "low": low}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f055_dm_plus', '_f055_dm_minus', '_f055_adx')
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
    print(f"OK f055_adx_trend_strength_base_001_075_claude: {n_features} features pass")
