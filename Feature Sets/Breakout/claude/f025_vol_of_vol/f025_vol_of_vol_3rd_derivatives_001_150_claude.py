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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f025_rolling_vol(close, w):
    r = close.pct_change()
    return r.rolling(w, min_periods=max(1, w // 2)).std()


def _f025_vol_of_vol(close, w):
    r = close.pct_change()
    rv = r.rolling(max(2, w // 2), min_periods=1).std()
    return rv.rolling(w, min_periods=max(1, w // 2)).std()


def _f025_coil_stability(close, w):
    r = close.pct_change()
    rv = r.rolling(max(2, w // 2), min_periods=1).std()
    vov = rv.rolling(w, min_periods=max(1, w // 2)).std()
    mu = rv.rolling(w, min_periods=max(1, w // 2)).mean()
    return (vov / mu.replace(0, np.nan).abs()) * close


def f025vov_f025_vol_of_vol_p1_5d_raw_jerk_v001_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_5d_m21_jerk_v002_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 5), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_5d_z252_jerk_v003_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 5), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_5d_d21_jerk_v004_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 5).diff(periods=21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_5d_rk252_jerk_v005_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 5)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_10d_raw_jerk_v006_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_10d_m21_jerk_v007_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 10), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_10d_z252_jerk_v008_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 10), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_10d_d21_jerk_v009_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 10).diff(periods=21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_10d_rk252_jerk_v010_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 10)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_21d_raw_jerk_v011_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_21d_m21_jerk_v012_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_21d_z252_jerk_v013_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_21d_d21_jerk_v014_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 21).diff(periods=21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_21d_rk252_jerk_v015_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 21)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_42d_raw_jerk_v016_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_42d_m21_jerk_v017_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_42d_z252_jerk_v018_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 42), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_42d_d21_jerk_v019_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 42).diff(periods=21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_42d_rk252_jerk_v020_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 42)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_63d_raw_jerk_v021_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_63d_m21_jerk_v022_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_63d_z252_jerk_v023_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_63d_d21_jerk_v024_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 63).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_63d_rk252_jerk_v025_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 63)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_126d_raw_jerk_v026_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_126d_m21_jerk_v027_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_126d_z252_jerk_v028_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 126), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_126d_d21_jerk_v029_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 126).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_126d_rk252_jerk_v030_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 126)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_189d_raw_jerk_v031_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_189d_m21_jerk_v032_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_189d_z252_jerk_v033_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 189), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_189d_d21_jerk_v034_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 189).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_189d_rk252_jerk_v035_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 189)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_252d_raw_jerk_v036_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_252d_m21_jerk_v037_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_252d_z252_jerk_v038_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_252d_d21_jerk_v039_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 252).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_252d_rk252_jerk_v040_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 252)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_378d_raw_jerk_v041_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_378d_m21_jerk_v042_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 378), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_378d_z252_jerk_v043_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 378), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_378d_d21_jerk_v044_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 378).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_378d_rk252_jerk_v045_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 378)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_504d_raw_jerk_v046_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_504d_m21_jerk_v047_signal(closeadj):
    base = _mean(_f025_rolling_vol(closeadj, 504), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_504d_z252_jerk_v048_signal(closeadj):
    base = _z(_f025_rolling_vol(closeadj, 504), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_504d_d21_jerk_v049_signal(closeadj):
    base = _f025_rolling_vol(closeadj, 504).diff(periods=21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p1_504d_rk252_jerk_v050_signal(closeadj):
    base = (_f025_rolling_vol(closeadj, 504)).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_5d_m63_jerk_v051_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 5), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_5d_s63_jerk_v052_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 5), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_5d_z126_jerk_v053_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 5), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_5d_d63_jerk_v054_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 5).diff(periods=63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_5d_ed_jerk_v055_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 5)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 5)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_10d_m63_jerk_v056_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 10), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_10d_s63_jerk_v057_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 10), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_10d_z126_jerk_v058_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 10), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_10d_d63_jerk_v059_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 10).diff(periods=63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_10d_ed_jerk_v060_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 10)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 10)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_21d_m63_jerk_v061_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_21d_s63_jerk_v062_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_21d_z126_jerk_v063_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_21d_d63_jerk_v064_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 21).diff(periods=63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_21d_ed_jerk_v065_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 21)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 21)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_42d_m63_jerk_v066_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 42), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_42d_s63_jerk_v067_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 42), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_42d_z126_jerk_v068_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 42), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_42d_d63_jerk_v069_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 42).diff(periods=63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_42d_ed_jerk_v070_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 42)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 42)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_63d_m63_jerk_v071_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_63d_s63_jerk_v072_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_63d_z126_jerk_v073_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_63d_d63_jerk_v074_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 63).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_63d_ed_jerk_v075_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 63)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 63)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_126d_m63_jerk_v076_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_126d_s63_jerk_v077_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_126d_z126_jerk_v078_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 126), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_126d_d63_jerk_v079_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 126).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_126d_ed_jerk_v080_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 126)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 126)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_189d_m63_jerk_v081_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 189), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_189d_s63_jerk_v082_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 189), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_189d_z126_jerk_v083_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 189), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_189d_d63_jerk_v084_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 189).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_189d_ed_jerk_v085_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 189)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 189)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_252d_m63_jerk_v086_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_252d_s63_jerk_v087_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_252d_z126_jerk_v088_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 252), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_252d_d63_jerk_v089_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 252).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_252d_ed_jerk_v090_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 252)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 252)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_378d_m63_jerk_v091_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 378), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_378d_s63_jerk_v092_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 378), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_378d_z126_jerk_v093_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 378), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_378d_d63_jerk_v094_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 378).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_378d_ed_jerk_v095_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 378)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 378)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_504d_m63_jerk_v096_signal(closeadj):
    base = _mean(_f025_vol_of_vol(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_504d_s63_jerk_v097_signal(closeadj):
    base = _std(_f025_vol_of_vol(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_504d_z126_jerk_v098_signal(closeadj):
    base = _z(_f025_vol_of_vol(closeadj, 504), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_504d_d63_jerk_v099_signal(closeadj):
    base = _f025_vol_of_vol(closeadj, 504).diff(periods=63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p2_504d_ed_jerk_v100_signal(closeadj):
    base = ((_f025_vol_of_vol(closeadj, 504)).ewm(span=21, adjust=False).mean() - (_f025_vol_of_vol(closeadj, 504)).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_5d_s21_jerk_v101_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 5), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_5d_e21_jerk_v102_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_5d_smadf_jerk_v103_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 5) - _mean(_f025_coil_stability(closeadj, 5), 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_5d_smarat_jerk_v104_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 5), _mean(_f025_coil_stability(closeadj, 5), 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_5d_zsq_jerk_v105_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 5), 252) * _z(_f025_coil_stability(closeadj, 5), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_10d_s21_jerk_v106_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 10), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_10d_e21_jerk_v107_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 10)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_10d_smadf_jerk_v108_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 10) - _mean(_f025_coil_stability(closeadj, 10), 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_10d_smarat_jerk_v109_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 10), _mean(_f025_coil_stability(closeadj, 10), 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_10d_zsq_jerk_v110_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 10), 252) * _z(_f025_coil_stability(closeadj, 10), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_21d_s21_jerk_v111_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_21d_e21_jerk_v112_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_21d_smadf_jerk_v113_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 21) - _mean(_f025_coil_stability(closeadj, 21), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_21d_smarat_jerk_v114_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 21), _mean(_f025_coil_stability(closeadj, 21), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_21d_zsq_jerk_v115_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 21), 252) * _z(_f025_coil_stability(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_42d_s21_jerk_v116_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_42d_e21_jerk_v117_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 42)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_42d_smadf_jerk_v118_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 42) - _mean(_f025_coil_stability(closeadj, 42), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_42d_smarat_jerk_v119_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 42), _mean(_f025_coil_stability(closeadj, 42), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_42d_zsq_jerk_v120_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 42), 252) * _z(_f025_coil_stability(closeadj, 42), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_63d_s21_jerk_v121_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_63d_e21_jerk_v122_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_63d_smadf_jerk_v123_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 63) - _mean(_f025_coil_stability(closeadj, 63), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_63d_smarat_jerk_v124_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 63), _mean(_f025_coil_stability(closeadj, 63), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_63d_zsq_jerk_v125_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 63), 252) * _z(_f025_coil_stability(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_126d_s21_jerk_v126_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_126d_e21_jerk_v127_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 126)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_126d_smadf_jerk_v128_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 126) - _mean(_f025_coil_stability(closeadj, 126), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_126d_smarat_jerk_v129_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 126), _mean(_f025_coil_stability(closeadj, 126), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_126d_zsq_jerk_v130_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 126), 252) * _z(_f025_coil_stability(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_189d_s21_jerk_v131_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_189d_e21_jerk_v132_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 189)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_189d_smadf_jerk_v133_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 189) - _mean(_f025_coil_stability(closeadj, 189), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_189d_smarat_jerk_v134_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 189), _mean(_f025_coil_stability(closeadj, 189), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_189d_zsq_jerk_v135_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 189), 252) * _z(_f025_coil_stability(closeadj, 189), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_252d_s21_jerk_v136_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_252d_e21_jerk_v137_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 252)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_252d_smadf_jerk_v138_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 252) - _mean(_f025_coil_stability(closeadj, 252), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_252d_smarat_jerk_v139_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 252), _mean(_f025_coil_stability(closeadj, 252), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_252d_zsq_jerk_v140_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 252), 252) * _z(_f025_coil_stability(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_378d_s21_jerk_v141_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 378), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_378d_e21_jerk_v142_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 378)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_378d_smadf_jerk_v143_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 378) - _mean(_f025_coil_stability(closeadj, 378), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_378d_smarat_jerk_v144_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 378), _mean(_f025_coil_stability(closeadj, 378), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_378d_zsq_jerk_v145_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 378), 252) * _z(_f025_coil_stability(closeadj, 378), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_504d_s21_jerk_v146_signal(closeadj):
    base = _std(_f025_coil_stability(closeadj, 504), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_504d_e21_jerk_v147_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_504d_smadf_jerk_v148_signal(closeadj):
    base = (_f025_coil_stability(closeadj, 504) - _mean(_f025_coil_stability(closeadj, 504), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_504d_smarat_jerk_v149_signal(closeadj):
    base = _safe_div(_f025_coil_stability(closeadj, 504), _mean(_f025_coil_stability(closeadj, 504), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f025vov_f025_vol_of_vol_p3_504d_zsq_jerk_v150_signal(closeadj):
    base = _z(_f025_coil_stability(closeadj, 504), 252) * _z(_f025_coil_stability(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f025vov_f025_vol_of_vol_p1_5d_raw_jerk_v001_signal,
    f025vov_f025_vol_of_vol_p1_5d_m21_jerk_v002_signal,
    f025vov_f025_vol_of_vol_p1_5d_z252_jerk_v003_signal,
    f025vov_f025_vol_of_vol_p1_5d_d21_jerk_v004_signal,
    f025vov_f025_vol_of_vol_p1_5d_rk252_jerk_v005_signal,
    f025vov_f025_vol_of_vol_p1_10d_raw_jerk_v006_signal,
    f025vov_f025_vol_of_vol_p1_10d_m21_jerk_v007_signal,
    f025vov_f025_vol_of_vol_p1_10d_z252_jerk_v008_signal,
    f025vov_f025_vol_of_vol_p1_10d_d21_jerk_v009_signal,
    f025vov_f025_vol_of_vol_p1_10d_rk252_jerk_v010_signal,
    f025vov_f025_vol_of_vol_p1_21d_raw_jerk_v011_signal,
    f025vov_f025_vol_of_vol_p1_21d_m21_jerk_v012_signal,
    f025vov_f025_vol_of_vol_p1_21d_z252_jerk_v013_signal,
    f025vov_f025_vol_of_vol_p1_21d_d21_jerk_v014_signal,
    f025vov_f025_vol_of_vol_p1_21d_rk252_jerk_v015_signal,
    f025vov_f025_vol_of_vol_p1_42d_raw_jerk_v016_signal,
    f025vov_f025_vol_of_vol_p1_42d_m21_jerk_v017_signal,
    f025vov_f025_vol_of_vol_p1_42d_z252_jerk_v018_signal,
    f025vov_f025_vol_of_vol_p1_42d_d21_jerk_v019_signal,
    f025vov_f025_vol_of_vol_p1_42d_rk252_jerk_v020_signal,
    f025vov_f025_vol_of_vol_p1_63d_raw_jerk_v021_signal,
    f025vov_f025_vol_of_vol_p1_63d_m21_jerk_v022_signal,
    f025vov_f025_vol_of_vol_p1_63d_z252_jerk_v023_signal,
    f025vov_f025_vol_of_vol_p1_63d_d21_jerk_v024_signal,
    f025vov_f025_vol_of_vol_p1_63d_rk252_jerk_v025_signal,
    f025vov_f025_vol_of_vol_p1_126d_raw_jerk_v026_signal,
    f025vov_f025_vol_of_vol_p1_126d_m21_jerk_v027_signal,
    f025vov_f025_vol_of_vol_p1_126d_z252_jerk_v028_signal,
    f025vov_f025_vol_of_vol_p1_126d_d21_jerk_v029_signal,
    f025vov_f025_vol_of_vol_p1_126d_rk252_jerk_v030_signal,
    f025vov_f025_vol_of_vol_p1_189d_raw_jerk_v031_signal,
    f025vov_f025_vol_of_vol_p1_189d_m21_jerk_v032_signal,
    f025vov_f025_vol_of_vol_p1_189d_z252_jerk_v033_signal,
    f025vov_f025_vol_of_vol_p1_189d_d21_jerk_v034_signal,
    f025vov_f025_vol_of_vol_p1_189d_rk252_jerk_v035_signal,
    f025vov_f025_vol_of_vol_p1_252d_raw_jerk_v036_signal,
    f025vov_f025_vol_of_vol_p1_252d_m21_jerk_v037_signal,
    f025vov_f025_vol_of_vol_p1_252d_z252_jerk_v038_signal,
    f025vov_f025_vol_of_vol_p1_252d_d21_jerk_v039_signal,
    f025vov_f025_vol_of_vol_p1_252d_rk252_jerk_v040_signal,
    f025vov_f025_vol_of_vol_p1_378d_raw_jerk_v041_signal,
    f025vov_f025_vol_of_vol_p1_378d_m21_jerk_v042_signal,
    f025vov_f025_vol_of_vol_p1_378d_z252_jerk_v043_signal,
    f025vov_f025_vol_of_vol_p1_378d_d21_jerk_v044_signal,
    f025vov_f025_vol_of_vol_p1_378d_rk252_jerk_v045_signal,
    f025vov_f025_vol_of_vol_p1_504d_raw_jerk_v046_signal,
    f025vov_f025_vol_of_vol_p1_504d_m21_jerk_v047_signal,
    f025vov_f025_vol_of_vol_p1_504d_z252_jerk_v048_signal,
    f025vov_f025_vol_of_vol_p1_504d_d21_jerk_v049_signal,
    f025vov_f025_vol_of_vol_p1_504d_rk252_jerk_v050_signal,
    f025vov_f025_vol_of_vol_p2_5d_m63_jerk_v051_signal,
    f025vov_f025_vol_of_vol_p2_5d_s63_jerk_v052_signal,
    f025vov_f025_vol_of_vol_p2_5d_z126_jerk_v053_signal,
    f025vov_f025_vol_of_vol_p2_5d_d63_jerk_v054_signal,
    f025vov_f025_vol_of_vol_p2_5d_ed_jerk_v055_signal,
    f025vov_f025_vol_of_vol_p2_10d_m63_jerk_v056_signal,
    f025vov_f025_vol_of_vol_p2_10d_s63_jerk_v057_signal,
    f025vov_f025_vol_of_vol_p2_10d_z126_jerk_v058_signal,
    f025vov_f025_vol_of_vol_p2_10d_d63_jerk_v059_signal,
    f025vov_f025_vol_of_vol_p2_10d_ed_jerk_v060_signal,
    f025vov_f025_vol_of_vol_p2_21d_m63_jerk_v061_signal,
    f025vov_f025_vol_of_vol_p2_21d_s63_jerk_v062_signal,
    f025vov_f025_vol_of_vol_p2_21d_z126_jerk_v063_signal,
    f025vov_f025_vol_of_vol_p2_21d_d63_jerk_v064_signal,
    f025vov_f025_vol_of_vol_p2_21d_ed_jerk_v065_signal,
    f025vov_f025_vol_of_vol_p2_42d_m63_jerk_v066_signal,
    f025vov_f025_vol_of_vol_p2_42d_s63_jerk_v067_signal,
    f025vov_f025_vol_of_vol_p2_42d_z126_jerk_v068_signal,
    f025vov_f025_vol_of_vol_p2_42d_d63_jerk_v069_signal,
    f025vov_f025_vol_of_vol_p2_42d_ed_jerk_v070_signal,
    f025vov_f025_vol_of_vol_p2_63d_m63_jerk_v071_signal,
    f025vov_f025_vol_of_vol_p2_63d_s63_jerk_v072_signal,
    f025vov_f025_vol_of_vol_p2_63d_z126_jerk_v073_signal,
    f025vov_f025_vol_of_vol_p2_63d_d63_jerk_v074_signal,
    f025vov_f025_vol_of_vol_p2_63d_ed_jerk_v075_signal,
    f025vov_f025_vol_of_vol_p2_126d_m63_jerk_v076_signal,
    f025vov_f025_vol_of_vol_p2_126d_s63_jerk_v077_signal,
    f025vov_f025_vol_of_vol_p2_126d_z126_jerk_v078_signal,
    f025vov_f025_vol_of_vol_p2_126d_d63_jerk_v079_signal,
    f025vov_f025_vol_of_vol_p2_126d_ed_jerk_v080_signal,
    f025vov_f025_vol_of_vol_p2_189d_m63_jerk_v081_signal,
    f025vov_f025_vol_of_vol_p2_189d_s63_jerk_v082_signal,
    f025vov_f025_vol_of_vol_p2_189d_z126_jerk_v083_signal,
    f025vov_f025_vol_of_vol_p2_189d_d63_jerk_v084_signal,
    f025vov_f025_vol_of_vol_p2_189d_ed_jerk_v085_signal,
    f025vov_f025_vol_of_vol_p2_252d_m63_jerk_v086_signal,
    f025vov_f025_vol_of_vol_p2_252d_s63_jerk_v087_signal,
    f025vov_f025_vol_of_vol_p2_252d_z126_jerk_v088_signal,
    f025vov_f025_vol_of_vol_p2_252d_d63_jerk_v089_signal,
    f025vov_f025_vol_of_vol_p2_252d_ed_jerk_v090_signal,
    f025vov_f025_vol_of_vol_p2_378d_m63_jerk_v091_signal,
    f025vov_f025_vol_of_vol_p2_378d_s63_jerk_v092_signal,
    f025vov_f025_vol_of_vol_p2_378d_z126_jerk_v093_signal,
    f025vov_f025_vol_of_vol_p2_378d_d63_jerk_v094_signal,
    f025vov_f025_vol_of_vol_p2_378d_ed_jerk_v095_signal,
    f025vov_f025_vol_of_vol_p2_504d_m63_jerk_v096_signal,
    f025vov_f025_vol_of_vol_p2_504d_s63_jerk_v097_signal,
    f025vov_f025_vol_of_vol_p2_504d_z126_jerk_v098_signal,
    f025vov_f025_vol_of_vol_p2_504d_d63_jerk_v099_signal,
    f025vov_f025_vol_of_vol_p2_504d_ed_jerk_v100_signal,
    f025vov_f025_vol_of_vol_p3_5d_s21_jerk_v101_signal,
    f025vov_f025_vol_of_vol_p3_5d_e21_jerk_v102_signal,
    f025vov_f025_vol_of_vol_p3_5d_smadf_jerk_v103_signal,
    f025vov_f025_vol_of_vol_p3_5d_smarat_jerk_v104_signal,
    f025vov_f025_vol_of_vol_p3_5d_zsq_jerk_v105_signal,
    f025vov_f025_vol_of_vol_p3_10d_s21_jerk_v106_signal,
    f025vov_f025_vol_of_vol_p3_10d_e21_jerk_v107_signal,
    f025vov_f025_vol_of_vol_p3_10d_smadf_jerk_v108_signal,
    f025vov_f025_vol_of_vol_p3_10d_smarat_jerk_v109_signal,
    f025vov_f025_vol_of_vol_p3_10d_zsq_jerk_v110_signal,
    f025vov_f025_vol_of_vol_p3_21d_s21_jerk_v111_signal,
    f025vov_f025_vol_of_vol_p3_21d_e21_jerk_v112_signal,
    f025vov_f025_vol_of_vol_p3_21d_smadf_jerk_v113_signal,
    f025vov_f025_vol_of_vol_p3_21d_smarat_jerk_v114_signal,
    f025vov_f025_vol_of_vol_p3_21d_zsq_jerk_v115_signal,
    f025vov_f025_vol_of_vol_p3_42d_s21_jerk_v116_signal,
    f025vov_f025_vol_of_vol_p3_42d_e21_jerk_v117_signal,
    f025vov_f025_vol_of_vol_p3_42d_smadf_jerk_v118_signal,
    f025vov_f025_vol_of_vol_p3_42d_smarat_jerk_v119_signal,
    f025vov_f025_vol_of_vol_p3_42d_zsq_jerk_v120_signal,
    f025vov_f025_vol_of_vol_p3_63d_s21_jerk_v121_signal,
    f025vov_f025_vol_of_vol_p3_63d_e21_jerk_v122_signal,
    f025vov_f025_vol_of_vol_p3_63d_smadf_jerk_v123_signal,
    f025vov_f025_vol_of_vol_p3_63d_smarat_jerk_v124_signal,
    f025vov_f025_vol_of_vol_p3_63d_zsq_jerk_v125_signal,
    f025vov_f025_vol_of_vol_p3_126d_s21_jerk_v126_signal,
    f025vov_f025_vol_of_vol_p3_126d_e21_jerk_v127_signal,
    f025vov_f025_vol_of_vol_p3_126d_smadf_jerk_v128_signal,
    f025vov_f025_vol_of_vol_p3_126d_smarat_jerk_v129_signal,
    f025vov_f025_vol_of_vol_p3_126d_zsq_jerk_v130_signal,
    f025vov_f025_vol_of_vol_p3_189d_s21_jerk_v131_signal,
    f025vov_f025_vol_of_vol_p3_189d_e21_jerk_v132_signal,
    f025vov_f025_vol_of_vol_p3_189d_smadf_jerk_v133_signal,
    f025vov_f025_vol_of_vol_p3_189d_smarat_jerk_v134_signal,
    f025vov_f025_vol_of_vol_p3_189d_zsq_jerk_v135_signal,
    f025vov_f025_vol_of_vol_p3_252d_s21_jerk_v136_signal,
    f025vov_f025_vol_of_vol_p3_252d_e21_jerk_v137_signal,
    f025vov_f025_vol_of_vol_p3_252d_smadf_jerk_v138_signal,
    f025vov_f025_vol_of_vol_p3_252d_smarat_jerk_v139_signal,
    f025vov_f025_vol_of_vol_p3_252d_zsq_jerk_v140_signal,
    f025vov_f025_vol_of_vol_p3_378d_s21_jerk_v141_signal,
    f025vov_f025_vol_of_vol_p3_378d_e21_jerk_v142_signal,
    f025vov_f025_vol_of_vol_p3_378d_smadf_jerk_v143_signal,
    f025vov_f025_vol_of_vol_p3_378d_smarat_jerk_v144_signal,
    f025vov_f025_vol_of_vol_p3_378d_zsq_jerk_v145_signal,
    f025vov_f025_vol_of_vol_p3_504d_s21_jerk_v146_signal,
    f025vov_f025_vol_of_vol_p3_504d_e21_jerk_v147_signal,
    f025vov_f025_vol_of_vol_p3_504d_smadf_jerk_v148_signal,
    f025vov_f025_vol_of_vol_p3_504d_smarat_jerk_v149_signal,
    f025vov_f025_vol_of_vol_p3_504d_zsq_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F025_VOL_OF_VOL_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ('_f025_rolling_vol', '_f025_vol_of_vol', '_f025_coil_stability')
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
    print(f"OK f025_vol_of_vol_3rd_derivatives_001_150_claude: {n_features} features pass")
