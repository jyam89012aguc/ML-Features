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
def _f021_bandwidth_rank(close, w):
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    bw = (2.0 * sd) / m.replace(0, np.nan).abs()
    return bw.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _f021_squeeze_extreme(close, w):
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    bw = (2.0 * sd) / m.replace(0, np.nan).abs()
    rk = bw.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)
    return (1.0 - rk) * close


def _f021_percentile_score(close, w):
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    bw = (2.0 * sd) / m.replace(0, np.nan).abs()
    rk = bw.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)
    return (0.5 - rk).abs() * close


def f021bwp_f021_bandwidth_percentile_p1_5d_raw_base_v001_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_5d_m21_base_v002_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_5d_z252_base_v003_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_5d_d21_base_v004_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 5).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_5d_rk252_base_v005_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 5)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_10d_raw_base_v006_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_10d_m21_base_v007_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_10d_z252_base_v008_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_10d_d21_base_v009_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 10).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_10d_rk252_base_v010_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 10)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_21d_raw_base_v011_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_21d_m21_base_v012_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_21d_z252_base_v013_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_21d_d21_base_v014_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 21).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_21d_rk252_base_v015_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 21)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_42d_raw_base_v016_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_42d_m21_base_v017_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_42d_z252_base_v018_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_42d_d21_base_v019_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 42).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_42d_rk252_base_v020_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 42)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_63d_raw_base_v021_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_63d_m21_base_v022_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_63d_z252_base_v023_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_63d_d21_base_v024_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 63).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_63d_rk252_base_v025_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 63)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_126d_raw_base_v026_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_126d_m21_base_v027_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_126d_z252_base_v028_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_126d_d21_base_v029_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 126).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_126d_rk252_base_v030_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 126)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_189d_raw_base_v031_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_189d_m21_base_v032_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 189), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_189d_z252_base_v033_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 189), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_189d_d21_base_v034_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 189).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_189d_rk252_base_v035_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 189)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_252d_raw_base_v036_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_252d_m21_base_v037_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_252d_z252_base_v038_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_252d_d21_base_v039_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 252).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_252d_rk252_base_v040_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 252)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_378d_raw_base_v041_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_378d_m21_base_v042_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 378), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_378d_z252_base_v043_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 378), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_378d_d21_base_v044_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 378).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_378d_rk252_base_v045_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 378)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_504d_raw_base_v046_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_504d_m21_base_v047_signal(closeadj):
    result = _mean(_f021_bandwidth_rank(closeadj, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_504d_z252_base_v048_signal(closeadj):
    result = _z(_f021_bandwidth_rank(closeadj, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_504d_d21_base_v049_signal(closeadj):
    result = _f021_bandwidth_rank(closeadj, 504).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p1_504d_rk252_base_v050_signal(closeadj):
    result = (_f021_bandwidth_rank(closeadj, 504)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_5d_m63_base_v051_signal(closeadj):
    result = _mean(_f021_squeeze_extreme(closeadj, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_5d_s63_base_v052_signal(closeadj):
    result = _std(_f021_squeeze_extreme(closeadj, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_5d_z126_base_v053_signal(closeadj):
    result = _z(_f021_squeeze_extreme(closeadj, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_5d_d63_base_v054_signal(closeadj):
    result = _f021_squeeze_extreme(closeadj, 5).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_5d_ed_base_v055_signal(closeadj):
    result = ((_f021_squeeze_extreme(closeadj, 5)).ewm(span=21, adjust=False).mean() - (_f021_squeeze_extreme(closeadj, 5)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_10d_m63_base_v056_signal(closeadj):
    result = _mean(_f021_squeeze_extreme(closeadj, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_10d_s63_base_v057_signal(closeadj):
    result = _std(_f021_squeeze_extreme(closeadj, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_10d_z126_base_v058_signal(closeadj):
    result = _z(_f021_squeeze_extreme(closeadj, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_10d_d63_base_v059_signal(closeadj):
    result = _f021_squeeze_extreme(closeadj, 10).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_10d_ed_base_v060_signal(closeadj):
    result = ((_f021_squeeze_extreme(closeadj, 10)).ewm(span=21, adjust=False).mean() - (_f021_squeeze_extreme(closeadj, 10)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_21d_m63_base_v061_signal(closeadj):
    result = _mean(_f021_squeeze_extreme(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_21d_s63_base_v062_signal(closeadj):
    result = _std(_f021_squeeze_extreme(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_21d_z126_base_v063_signal(closeadj):
    result = _z(_f021_squeeze_extreme(closeadj, 21), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_21d_d63_base_v064_signal(closeadj):
    result = _f021_squeeze_extreme(closeadj, 21).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_21d_ed_base_v065_signal(closeadj):
    result = ((_f021_squeeze_extreme(closeadj, 21)).ewm(span=21, adjust=False).mean() - (_f021_squeeze_extreme(closeadj, 21)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_42d_m63_base_v066_signal(closeadj):
    result = _mean(_f021_squeeze_extreme(closeadj, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_42d_s63_base_v067_signal(closeadj):
    result = _std(_f021_squeeze_extreme(closeadj, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_42d_z126_base_v068_signal(closeadj):
    result = _z(_f021_squeeze_extreme(closeadj, 42), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_42d_d63_base_v069_signal(closeadj):
    result = _f021_squeeze_extreme(closeadj, 42).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_42d_ed_base_v070_signal(closeadj):
    result = ((_f021_squeeze_extreme(closeadj, 42)).ewm(span=21, adjust=False).mean() - (_f021_squeeze_extreme(closeadj, 42)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_63d_m63_base_v071_signal(closeadj):
    result = _mean(_f021_squeeze_extreme(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_63d_s63_base_v072_signal(closeadj):
    result = _std(_f021_squeeze_extreme(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_63d_z126_base_v073_signal(closeadj):
    result = _z(_f021_squeeze_extreme(closeadj, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_63d_d63_base_v074_signal(closeadj):
    result = _f021_squeeze_extreme(closeadj, 63).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f021bwp_f021_bandwidth_percentile_p2_63d_ed_base_v075_signal(closeadj):
    result = ((_f021_squeeze_extreme(closeadj, 63)).ewm(span=21, adjust=False).mean() - (_f021_squeeze_extreme(closeadj, 63)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f021bwp_f021_bandwidth_percentile_p1_5d_raw_base_v001_signal,
    f021bwp_f021_bandwidth_percentile_p1_5d_m21_base_v002_signal,
    f021bwp_f021_bandwidth_percentile_p1_5d_z252_base_v003_signal,
    f021bwp_f021_bandwidth_percentile_p1_5d_d21_base_v004_signal,
    f021bwp_f021_bandwidth_percentile_p1_5d_rk252_base_v005_signal,
    f021bwp_f021_bandwidth_percentile_p1_10d_raw_base_v006_signal,
    f021bwp_f021_bandwidth_percentile_p1_10d_m21_base_v007_signal,
    f021bwp_f021_bandwidth_percentile_p1_10d_z252_base_v008_signal,
    f021bwp_f021_bandwidth_percentile_p1_10d_d21_base_v009_signal,
    f021bwp_f021_bandwidth_percentile_p1_10d_rk252_base_v010_signal,
    f021bwp_f021_bandwidth_percentile_p1_21d_raw_base_v011_signal,
    f021bwp_f021_bandwidth_percentile_p1_21d_m21_base_v012_signal,
    f021bwp_f021_bandwidth_percentile_p1_21d_z252_base_v013_signal,
    f021bwp_f021_bandwidth_percentile_p1_21d_d21_base_v014_signal,
    f021bwp_f021_bandwidth_percentile_p1_21d_rk252_base_v015_signal,
    f021bwp_f021_bandwidth_percentile_p1_42d_raw_base_v016_signal,
    f021bwp_f021_bandwidth_percentile_p1_42d_m21_base_v017_signal,
    f021bwp_f021_bandwidth_percentile_p1_42d_z252_base_v018_signal,
    f021bwp_f021_bandwidth_percentile_p1_42d_d21_base_v019_signal,
    f021bwp_f021_bandwidth_percentile_p1_42d_rk252_base_v020_signal,
    f021bwp_f021_bandwidth_percentile_p1_63d_raw_base_v021_signal,
    f021bwp_f021_bandwidth_percentile_p1_63d_m21_base_v022_signal,
    f021bwp_f021_bandwidth_percentile_p1_63d_z252_base_v023_signal,
    f021bwp_f021_bandwidth_percentile_p1_63d_d21_base_v024_signal,
    f021bwp_f021_bandwidth_percentile_p1_63d_rk252_base_v025_signal,
    f021bwp_f021_bandwidth_percentile_p1_126d_raw_base_v026_signal,
    f021bwp_f021_bandwidth_percentile_p1_126d_m21_base_v027_signal,
    f021bwp_f021_bandwidth_percentile_p1_126d_z252_base_v028_signal,
    f021bwp_f021_bandwidth_percentile_p1_126d_d21_base_v029_signal,
    f021bwp_f021_bandwidth_percentile_p1_126d_rk252_base_v030_signal,
    f021bwp_f021_bandwidth_percentile_p1_189d_raw_base_v031_signal,
    f021bwp_f021_bandwidth_percentile_p1_189d_m21_base_v032_signal,
    f021bwp_f021_bandwidth_percentile_p1_189d_z252_base_v033_signal,
    f021bwp_f021_bandwidth_percentile_p1_189d_d21_base_v034_signal,
    f021bwp_f021_bandwidth_percentile_p1_189d_rk252_base_v035_signal,
    f021bwp_f021_bandwidth_percentile_p1_252d_raw_base_v036_signal,
    f021bwp_f021_bandwidth_percentile_p1_252d_m21_base_v037_signal,
    f021bwp_f021_bandwidth_percentile_p1_252d_z252_base_v038_signal,
    f021bwp_f021_bandwidth_percentile_p1_252d_d21_base_v039_signal,
    f021bwp_f021_bandwidth_percentile_p1_252d_rk252_base_v040_signal,
    f021bwp_f021_bandwidth_percentile_p1_378d_raw_base_v041_signal,
    f021bwp_f021_bandwidth_percentile_p1_378d_m21_base_v042_signal,
    f021bwp_f021_bandwidth_percentile_p1_378d_z252_base_v043_signal,
    f021bwp_f021_bandwidth_percentile_p1_378d_d21_base_v044_signal,
    f021bwp_f021_bandwidth_percentile_p1_378d_rk252_base_v045_signal,
    f021bwp_f021_bandwidth_percentile_p1_504d_raw_base_v046_signal,
    f021bwp_f021_bandwidth_percentile_p1_504d_m21_base_v047_signal,
    f021bwp_f021_bandwidth_percentile_p1_504d_z252_base_v048_signal,
    f021bwp_f021_bandwidth_percentile_p1_504d_d21_base_v049_signal,
    f021bwp_f021_bandwidth_percentile_p1_504d_rk252_base_v050_signal,
    f021bwp_f021_bandwidth_percentile_p2_5d_m63_base_v051_signal,
    f021bwp_f021_bandwidth_percentile_p2_5d_s63_base_v052_signal,
    f021bwp_f021_bandwidth_percentile_p2_5d_z126_base_v053_signal,
    f021bwp_f021_bandwidth_percentile_p2_5d_d63_base_v054_signal,
    f021bwp_f021_bandwidth_percentile_p2_5d_ed_base_v055_signal,
    f021bwp_f021_bandwidth_percentile_p2_10d_m63_base_v056_signal,
    f021bwp_f021_bandwidth_percentile_p2_10d_s63_base_v057_signal,
    f021bwp_f021_bandwidth_percentile_p2_10d_z126_base_v058_signal,
    f021bwp_f021_bandwidth_percentile_p2_10d_d63_base_v059_signal,
    f021bwp_f021_bandwidth_percentile_p2_10d_ed_base_v060_signal,
    f021bwp_f021_bandwidth_percentile_p2_21d_m63_base_v061_signal,
    f021bwp_f021_bandwidth_percentile_p2_21d_s63_base_v062_signal,
    f021bwp_f021_bandwidth_percentile_p2_21d_z126_base_v063_signal,
    f021bwp_f021_bandwidth_percentile_p2_21d_d63_base_v064_signal,
    f021bwp_f021_bandwidth_percentile_p2_21d_ed_base_v065_signal,
    f021bwp_f021_bandwidth_percentile_p2_42d_m63_base_v066_signal,
    f021bwp_f021_bandwidth_percentile_p2_42d_s63_base_v067_signal,
    f021bwp_f021_bandwidth_percentile_p2_42d_z126_base_v068_signal,
    f021bwp_f021_bandwidth_percentile_p2_42d_d63_base_v069_signal,
    f021bwp_f021_bandwidth_percentile_p2_42d_ed_base_v070_signal,
    f021bwp_f021_bandwidth_percentile_p2_63d_m63_base_v071_signal,
    f021bwp_f021_bandwidth_percentile_p2_63d_s63_base_v072_signal,
    f021bwp_f021_bandwidth_percentile_p2_63d_z126_base_v073_signal,
    f021bwp_f021_bandwidth_percentile_p2_63d_d63_base_v074_signal,
    f021bwp_f021_bandwidth_percentile_p2_63d_ed_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F021_BANDWIDTH_PERCENTILE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f021_bandwidth_rank', '_f021_squeeze_extreme', '_f021_percentile_score')
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
    print(f"OK f021_bandwidth_percentile_base_001_075_claude: {n_features} features pass")
