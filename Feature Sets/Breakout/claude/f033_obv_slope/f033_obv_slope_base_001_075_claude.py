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
def _f033_obv(closeadj, volume):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    return (sign * volume).cumsum()


def _f033_obv_slope(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    return obv.diff(w) / obv.abs().replace(0, np.nan)


def _f033_obv_trend(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    m = obv.rolling(w, min_periods=max(1, w // 2)).mean()
    return (obv - m) / obv.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


def f033obs_f033_obv_slope_obvslope_5d_base_v001_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_10d_base_v002_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_21d_base_v003_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_42d_base_v004_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_63d_base_v005_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_126d_base_v006_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_189d_base_v007_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_252d_base_v008_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_378d_base_v009_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_504d_base_v010_signal(closeadj, volume):
    result = _f033_obv_slope(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_5d_base_v011_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_10d_base_v012_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_21d_base_v013_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_42d_base_v014_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_63d_base_v015_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_126d_base_v016_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_189d_base_v017_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_252d_base_v018_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_378d_base_v019_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_504d_base_v020_signal(closeadj, volume):
    result = _f033_obv_trend(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_5d_base_v021_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 21) * closeadj * np.log(5 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_10d_base_v022_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 21) * closeadj * np.log(10 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_21d_base_v023_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 21) * closeadj * np.log(21 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_42d_base_v024_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 63) * closeadj * np.log(42 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_63d_base_v025_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 63) * closeadj * np.log(63 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_126d_base_v026_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 126) * closeadj * np.log(126 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_189d_base_v027_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 252) * closeadj * np.log(189 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_252d_base_v028_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 252) * closeadj * np.log(252 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_378d_base_v029_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 504) * closeadj * np.log(378 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_504d_base_v030_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = _z(o, 504) * closeadj * np.log(504 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_5d_base_v031_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 5)) / o.abs().rolling(5, min_periods=1).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_10d_base_v032_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 10)) / o.abs().rolling(10, min_periods=2).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_21d_base_v033_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 21)) / o.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_42d_base_v034_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 42)) / o.abs().rolling(42, min_periods=10).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_63d_base_v035_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 63)) / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_126d_base_v036_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 126)) / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_189d_base_v037_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 189)) / o.abs().rolling(189, min_periods=47).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_252d_base_v038_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 252)) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_378d_base_v039_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 378)) / o.abs().rolling(378, min_periods=94).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_504d_base_v040_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    result = (o - _mean(o, 504)) / o.abs().rolling(504, min_periods=126).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_5d_base_v041_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_10d_base_v042_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_21d_base_v043_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    result = _mean(sl, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_42d_base_v044_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    result = _mean(sl, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_63d_base_v045_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    result = _mean(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_126d_base_v046_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    result = _mean(sl, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_189d_base_v047_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    result = _mean(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_252d_base_v048_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    result = _mean(sl, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_378d_base_v049_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    result = _mean(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_504d_base_v050_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    result = _mean(sl, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_5d_base_v051_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_10d_base_v052_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_21d_base_v053_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_42d_base_v054_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_63d_base_v055_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_126d_base_v056_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    result = _z(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_189d_base_v057_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    result = _z(sl, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_252d_base_v058_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    result = _z(sl, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_378d_base_v059_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    result = _z(sl, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_504d_base_v060_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    result = _z(sl, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_5d_base_v061_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 5)
    result = _mean(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_10d_base_v062_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 10)
    result = _mean(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_21d_base_v063_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    result = _mean(t, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_42d_base_v064_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 42)
    result = _mean(t, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_63d_base_v065_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    result = _mean(t, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_126d_base_v066_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    result = _mean(t, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_189d_base_v067_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 189)
    result = _mean(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_252d_base_v068_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    result = _mean(t, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_378d_base_v069_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 378)
    result = _mean(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_504d_base_v070_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 504)
    result = _mean(t, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_5d_base_v071_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    ret = closeadj.pct_change(1)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_10d_base_v072_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    ret = closeadj.pct_change(2)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_21d_base_v073_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_42d_base_v074_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    ret = closeadj.pct_change(10)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_63d_base_v075_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f033obs_f033_obv_slope_obvslope_5d_base_v001_signal,
    f033obs_f033_obv_slope_obvslope_10d_base_v002_signal,
    f033obs_f033_obv_slope_obvslope_21d_base_v003_signal,
    f033obs_f033_obv_slope_obvslope_42d_base_v004_signal,
    f033obs_f033_obv_slope_obvslope_63d_base_v005_signal,
    f033obs_f033_obv_slope_obvslope_126d_base_v006_signal,
    f033obs_f033_obv_slope_obvslope_189d_base_v007_signal,
    f033obs_f033_obv_slope_obvslope_252d_base_v008_signal,
    f033obs_f033_obv_slope_obvslope_378d_base_v009_signal,
    f033obs_f033_obv_slope_obvslope_504d_base_v010_signal,
    f033obs_f033_obv_slope_obvtrend_5d_base_v011_signal,
    f033obs_f033_obv_slope_obvtrend_10d_base_v012_signal,
    f033obs_f033_obv_slope_obvtrend_21d_base_v013_signal,
    f033obs_f033_obv_slope_obvtrend_42d_base_v014_signal,
    f033obs_f033_obv_slope_obvtrend_63d_base_v015_signal,
    f033obs_f033_obv_slope_obvtrend_126d_base_v016_signal,
    f033obs_f033_obv_slope_obvtrend_189d_base_v017_signal,
    f033obs_f033_obv_slope_obvtrend_252d_base_v018_signal,
    f033obs_f033_obv_slope_obvtrend_378d_base_v019_signal,
    f033obs_f033_obv_slope_obvtrend_504d_base_v020_signal,
    f033obs_f033_obv_slope_obvz_5d_base_v021_signal,
    f033obs_f033_obv_slope_obvz_10d_base_v022_signal,
    f033obs_f033_obv_slope_obvz_21d_base_v023_signal,
    f033obs_f033_obv_slope_obvz_42d_base_v024_signal,
    f033obs_f033_obv_slope_obvz_63d_base_v025_signal,
    f033obs_f033_obv_slope_obvz_126d_base_v026_signal,
    f033obs_f033_obv_slope_obvz_189d_base_v027_signal,
    f033obs_f033_obv_slope_obvz_252d_base_v028_signal,
    f033obs_f033_obv_slope_obvz_378d_base_v029_signal,
    f033obs_f033_obv_slope_obvz_504d_base_v030_signal,
    f033obs_f033_obv_slope_obvmean_5d_base_v031_signal,
    f033obs_f033_obv_slope_obvmean_10d_base_v032_signal,
    f033obs_f033_obv_slope_obvmean_21d_base_v033_signal,
    f033obs_f033_obv_slope_obvmean_42d_base_v034_signal,
    f033obs_f033_obv_slope_obvmean_63d_base_v035_signal,
    f033obs_f033_obv_slope_obvmean_126d_base_v036_signal,
    f033obs_f033_obv_slope_obvmean_189d_base_v037_signal,
    f033obs_f033_obv_slope_obvmean_252d_base_v038_signal,
    f033obs_f033_obv_slope_obvmean_378d_base_v039_signal,
    f033obs_f033_obv_slope_obvmean_504d_base_v040_signal,
    f033obs_f033_obv_slope_smobvslope_5d_base_v041_signal,
    f033obs_f033_obv_slope_smobvslope_10d_base_v042_signal,
    f033obs_f033_obv_slope_smobvslope_21d_base_v043_signal,
    f033obs_f033_obv_slope_smobvslope_42d_base_v044_signal,
    f033obs_f033_obv_slope_smobvslope_63d_base_v045_signal,
    f033obs_f033_obv_slope_smobvslope_126d_base_v046_signal,
    f033obs_f033_obv_slope_smobvslope_189d_base_v047_signal,
    f033obs_f033_obv_slope_smobvslope_252d_base_v048_signal,
    f033obs_f033_obv_slope_smobvslope_378d_base_v049_signal,
    f033obs_f033_obv_slope_smobvslope_504d_base_v050_signal,
    f033obs_f033_obv_slope_zobvslope_5d_base_v051_signal,
    f033obs_f033_obv_slope_zobvslope_10d_base_v052_signal,
    f033obs_f033_obv_slope_zobvslope_21d_base_v053_signal,
    f033obs_f033_obv_slope_zobvslope_42d_base_v054_signal,
    f033obs_f033_obv_slope_zobvslope_63d_base_v055_signal,
    f033obs_f033_obv_slope_zobvslope_126d_base_v056_signal,
    f033obs_f033_obv_slope_zobvslope_189d_base_v057_signal,
    f033obs_f033_obv_slope_zobvslope_252d_base_v058_signal,
    f033obs_f033_obv_slope_zobvslope_378d_base_v059_signal,
    f033obs_f033_obv_slope_zobvslope_504d_base_v060_signal,
    f033obs_f033_obv_slope_smobvtrend_5d_base_v061_signal,
    f033obs_f033_obv_slope_smobvtrend_10d_base_v062_signal,
    f033obs_f033_obv_slope_smobvtrend_21d_base_v063_signal,
    f033obs_f033_obv_slope_smobvtrend_42d_base_v064_signal,
    f033obs_f033_obv_slope_smobvtrend_63d_base_v065_signal,
    f033obs_f033_obv_slope_smobvtrend_126d_base_v066_signal,
    f033obs_f033_obv_slope_smobvtrend_189d_base_v067_signal,
    f033obs_f033_obv_slope_smobvtrend_252d_base_v068_signal,
    f033obs_f033_obv_slope_smobvtrend_378d_base_v069_signal,
    f033obs_f033_obv_slope_smobvtrend_504d_base_v070_signal,
    f033obs_f033_obv_slope_obvslopexsign_5d_base_v071_signal,
    f033obs_f033_obv_slope_obvslopexsign_10d_base_v072_signal,
    f033obs_f033_obv_slope_obvslopexsign_21d_base_v073_signal,
    f033obs_f033_obv_slope_obvslopexsign_42d_base_v074_signal,
    f033obs_f033_obv_slope_obvslopexsign_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F033_OBV_SLOPE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f033_obv', '_f033_obv_slope', '_f033_obv_trend')
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
    print(f"OK f033_obv_slope_base_001_075_claude: {n_features} features pass")
