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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


def f033obs_f033_obv_slope_obvslope_21d_slope_v001_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_21d_slope_v002_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_63d_slope_v003_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_63d_slope_v004_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_126d_slope_v005_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_126d_slope_v006_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_252d_slope_v007_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_252d_slope_v008_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_252d_slope_v009_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslope_252d_slope_v010_signal(closeadj, volume):
    base = _f033_obv_slope(closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_21d_slope_v011_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_21d_slope_v012_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_63d_slope_v013_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_63d_slope_v014_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_126d_slope_v015_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_126d_slope_v016_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_252d_slope_v017_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_252d_slope_v018_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_252d_slope_v019_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvtrend_252d_slope_v020_signal(closeadj, volume):
    base = _f033_obv_trend(closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_21d_slope_v021_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 21) * closeadj * np.log(21 + 1.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_21d_slope_v022_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 21) * closeadj * np.log(21 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_63d_slope_v023_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 63) * closeadj * np.log(63 + 1.0)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_63d_slope_v024_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 63) * closeadj * np.log(63 + 1.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_126d_slope_v025_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 126) * closeadj * np.log(126 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_126d_slope_v026_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 126) * closeadj * np.log(126 + 1.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_252d_slope_v027_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_252d_slope_v028_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 252) * closeadj * np.log(252 + 1.0)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_252d_slope_v029_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvz_252d_slope_v030_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = _z(o, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_21d_slope_v031_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 21)) / o.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_21d_slope_v032_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 21)) / o.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_63d_slope_v033_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 63)) / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_63d_slope_v034_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 63)) / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_126d_slope_v035_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 126)) / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_126d_slope_v036_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 126)) / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_252d_slope_v037_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 252)) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_252d_slope_v038_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 252)) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_252d_slope_v039_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 252)) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvmean_252d_slope_v040_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    base = (o - _mean(o, 252)) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_21d_slope_v041_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _mean(sl, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_21d_slope_v042_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _mean(sl, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_63d_slope_v043_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _mean(sl, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_63d_slope_v044_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _mean(sl, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_126d_slope_v045_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _mean(sl, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_126d_slope_v046_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _mean(sl, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_252d_slope_v047_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_252d_slope_v048_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_252d_slope_v049_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvslope_252d_slope_v050_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_21d_slope_v051_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_21d_slope_v052_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _z(sl, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_63d_slope_v053_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _z(sl, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_63d_slope_v054_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_126d_slope_v055_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _z(sl, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_126d_slope_v056_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _z(sl, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_252d_slope_v057_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_252d_slope_v058_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_252d_slope_v059_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvslope_252d_slope_v060_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_21d_slope_v061_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    base = _mean(t, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_21d_slope_v062_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    base = _mean(t, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_63d_slope_v063_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    base = _mean(t, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_63d_slope_v064_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    base = _mean(t, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_126d_slope_v065_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    base = _mean(t, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_126d_slope_v066_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    base = _mean(t, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_252d_slope_v067_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _mean(t, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_252d_slope_v068_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _mean(t, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_252d_slope_v069_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _mean(t, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_smobvtrend_252d_slope_v070_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _mean(t, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_21d_slope_v071_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=21, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_21d_slope_v072_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=21, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_63d_slope_v073_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=63, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_63d_slope_v074_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=63, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_126d_slope_v075_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=126, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_126d_slope_v076_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=126, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_252d_slope_v077_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=252, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_252d_slope_v078_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=252, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_252d_slope_v079_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=252, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_252d_slope_v080_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=252, adjust=False).mean()
    base = (o - ema) / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_21d_slope_v081_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _std(sl, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_21d_slope_v082_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = _std(sl, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_63d_slope_v083_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _std(sl, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_63d_slope_v084_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = _std(sl, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_126d_slope_v085_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _std(sl, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_126d_slope_v086_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = _std(sl, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_252d_slope_v087_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_252d_slope_v088_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_252d_slope_v089_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_252d_slope_v090_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_21d_slope_v091_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_21d_slope_v092_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_63d_slope_v093_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_63d_slope_v094_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_126d_slope_v095_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_126d_slope_v096_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_252d_slope_v097_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_252d_slope_v098_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_252d_slope_v099_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_252d_slope_v100_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_21d_slope_v101_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    tr = _f033_obv_trend(closeadj, volume, 21)
    base = (sl - tr) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_21d_slope_v102_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    tr = _f033_obv_trend(closeadj, volume, 21)
    base = (sl - tr) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_63d_slope_v103_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    tr = _f033_obv_trend(closeadj, volume, 63)
    base = (sl - tr) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_63d_slope_v104_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    tr = _f033_obv_trend(closeadj, volume, 63)
    base = (sl - tr) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_126d_slope_v105_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    tr = _f033_obv_trend(closeadj, volume, 126)
    base = (sl - tr) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_126d_slope_v106_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    tr = _f033_obv_trend(closeadj, volume, 126)
    base = (sl - tr) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_252d_slope_v107_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    tr = _f033_obv_trend(closeadj, volume, 252)
    base = (sl - tr) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_252d_slope_v108_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    tr = _f033_obv_trend(closeadj, volume, 252)
    base = (sl - tr) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_252d_slope_v109_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    tr = _f033_obv_trend(closeadj, volume, 252)
    base = (sl - tr) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_252d_slope_v110_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    tr = _f033_obv_trend(closeadj, volume, 252)
    base = (sl - tr) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_21d_slope_v111_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    vavg = _mean(volume, 21)
    base = sl * vavg / 1e6
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_21d_slope_v112_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    vavg = _mean(volume, 21)
    base = sl * vavg / 1e6
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_63d_slope_v113_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    vavg = _mean(volume, 63)
    base = sl * vavg / 1e6
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_63d_slope_v114_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    vavg = _mean(volume, 63)
    base = sl * vavg / 1e6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_126d_slope_v115_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    vavg = _mean(volume, 126)
    base = sl * vavg / 1e6
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_126d_slope_v116_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    vavg = _mean(volume, 126)
    base = sl * vavg / 1e6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_252d_slope_v117_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    vavg = _mean(volume, 252)
    base = sl * vavg / 1e6
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_252d_slope_v118_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    vavg = _mean(volume, 252)
    base = sl * vavg / 1e6
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_252d_slope_v119_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    vavg = _mean(volume, 252)
    base = sl * vavg / 1e6
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_252d_slope_v120_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    vavg = _mean(volume, 252)
    base = sl * vavg / 1e6
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_21d_slope_v121_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    base = _z(t, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_21d_slope_v122_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    base = _z(t, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_63d_slope_v123_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    base = _z(t, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_63d_slope_v124_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    base = _z(t, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_126d_slope_v125_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    base = _z(t, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_126d_slope_v126_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    base = _z(t, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_252d_slope_v127_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _z(t, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_252d_slope_v128_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _z(t, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_252d_slope_v129_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _z(t, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_252d_slope_v130_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    base = _z(t, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_21d_slope_v131_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_21d_slope_v132_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_63d_slope_v133_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_63d_slope_v134_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_126d_slope_v135_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_126d_slope_v136_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_252d_slope_v137_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_252d_slope_v138_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_252d_slope_v139_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_252d_slope_v140_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_21d_slope_v141_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_21d_slope_v142_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_63d_slope_v143_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_63d_slope_v144_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_126d_slope_v145_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_126d_slope_v146_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_252d_slope_v147_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_252d_slope_v148_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_252d_slope_v149_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_absobvslope_252d_slope_v150_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f033obs_f033_obv_slope_obvslope_21d_slope_v001_signal,
    f033obs_f033_obv_slope_obvslope_21d_slope_v002_signal,
    f033obs_f033_obv_slope_obvslope_63d_slope_v003_signal,
    f033obs_f033_obv_slope_obvslope_63d_slope_v004_signal,
    f033obs_f033_obv_slope_obvslope_126d_slope_v005_signal,
    f033obs_f033_obv_slope_obvslope_126d_slope_v006_signal,
    f033obs_f033_obv_slope_obvslope_252d_slope_v007_signal,
    f033obs_f033_obv_slope_obvslope_252d_slope_v008_signal,
    f033obs_f033_obv_slope_obvslope_252d_slope_v009_signal,
    f033obs_f033_obv_slope_obvslope_252d_slope_v010_signal,
    f033obs_f033_obv_slope_obvtrend_21d_slope_v011_signal,
    f033obs_f033_obv_slope_obvtrend_21d_slope_v012_signal,
    f033obs_f033_obv_slope_obvtrend_63d_slope_v013_signal,
    f033obs_f033_obv_slope_obvtrend_63d_slope_v014_signal,
    f033obs_f033_obv_slope_obvtrend_126d_slope_v015_signal,
    f033obs_f033_obv_slope_obvtrend_126d_slope_v016_signal,
    f033obs_f033_obv_slope_obvtrend_252d_slope_v017_signal,
    f033obs_f033_obv_slope_obvtrend_252d_slope_v018_signal,
    f033obs_f033_obv_slope_obvtrend_252d_slope_v019_signal,
    f033obs_f033_obv_slope_obvtrend_252d_slope_v020_signal,
    f033obs_f033_obv_slope_obvz_21d_slope_v021_signal,
    f033obs_f033_obv_slope_obvz_21d_slope_v022_signal,
    f033obs_f033_obv_slope_obvz_63d_slope_v023_signal,
    f033obs_f033_obv_slope_obvz_63d_slope_v024_signal,
    f033obs_f033_obv_slope_obvz_126d_slope_v025_signal,
    f033obs_f033_obv_slope_obvz_126d_slope_v026_signal,
    f033obs_f033_obv_slope_obvz_252d_slope_v027_signal,
    f033obs_f033_obv_slope_obvz_252d_slope_v028_signal,
    f033obs_f033_obv_slope_obvz_252d_slope_v029_signal,
    f033obs_f033_obv_slope_obvz_252d_slope_v030_signal,
    f033obs_f033_obv_slope_obvmean_21d_slope_v031_signal,
    f033obs_f033_obv_slope_obvmean_21d_slope_v032_signal,
    f033obs_f033_obv_slope_obvmean_63d_slope_v033_signal,
    f033obs_f033_obv_slope_obvmean_63d_slope_v034_signal,
    f033obs_f033_obv_slope_obvmean_126d_slope_v035_signal,
    f033obs_f033_obv_slope_obvmean_126d_slope_v036_signal,
    f033obs_f033_obv_slope_obvmean_252d_slope_v037_signal,
    f033obs_f033_obv_slope_obvmean_252d_slope_v038_signal,
    f033obs_f033_obv_slope_obvmean_252d_slope_v039_signal,
    f033obs_f033_obv_slope_obvmean_252d_slope_v040_signal,
    f033obs_f033_obv_slope_smobvslope_21d_slope_v041_signal,
    f033obs_f033_obv_slope_smobvslope_21d_slope_v042_signal,
    f033obs_f033_obv_slope_smobvslope_63d_slope_v043_signal,
    f033obs_f033_obv_slope_smobvslope_63d_slope_v044_signal,
    f033obs_f033_obv_slope_smobvslope_126d_slope_v045_signal,
    f033obs_f033_obv_slope_smobvslope_126d_slope_v046_signal,
    f033obs_f033_obv_slope_smobvslope_252d_slope_v047_signal,
    f033obs_f033_obv_slope_smobvslope_252d_slope_v048_signal,
    f033obs_f033_obv_slope_smobvslope_252d_slope_v049_signal,
    f033obs_f033_obv_slope_smobvslope_252d_slope_v050_signal,
    f033obs_f033_obv_slope_zobvslope_21d_slope_v051_signal,
    f033obs_f033_obv_slope_zobvslope_21d_slope_v052_signal,
    f033obs_f033_obv_slope_zobvslope_63d_slope_v053_signal,
    f033obs_f033_obv_slope_zobvslope_63d_slope_v054_signal,
    f033obs_f033_obv_slope_zobvslope_126d_slope_v055_signal,
    f033obs_f033_obv_slope_zobvslope_126d_slope_v056_signal,
    f033obs_f033_obv_slope_zobvslope_252d_slope_v057_signal,
    f033obs_f033_obv_slope_zobvslope_252d_slope_v058_signal,
    f033obs_f033_obv_slope_zobvslope_252d_slope_v059_signal,
    f033obs_f033_obv_slope_zobvslope_252d_slope_v060_signal,
    f033obs_f033_obv_slope_smobvtrend_21d_slope_v061_signal,
    f033obs_f033_obv_slope_smobvtrend_21d_slope_v062_signal,
    f033obs_f033_obv_slope_smobvtrend_63d_slope_v063_signal,
    f033obs_f033_obv_slope_smobvtrend_63d_slope_v064_signal,
    f033obs_f033_obv_slope_smobvtrend_126d_slope_v065_signal,
    f033obs_f033_obv_slope_smobvtrend_126d_slope_v066_signal,
    f033obs_f033_obv_slope_smobvtrend_252d_slope_v067_signal,
    f033obs_f033_obv_slope_smobvtrend_252d_slope_v068_signal,
    f033obs_f033_obv_slope_smobvtrend_252d_slope_v069_signal,
    f033obs_f033_obv_slope_smobvtrend_252d_slope_v070_signal,
    f033obs_f033_obv_slope_emaobv_21d_slope_v071_signal,
    f033obs_f033_obv_slope_emaobv_21d_slope_v072_signal,
    f033obs_f033_obv_slope_emaobv_63d_slope_v073_signal,
    f033obs_f033_obv_slope_emaobv_63d_slope_v074_signal,
    f033obs_f033_obv_slope_emaobv_126d_slope_v075_signal,
    f033obs_f033_obv_slope_emaobv_126d_slope_v076_signal,
    f033obs_f033_obv_slope_emaobv_252d_slope_v077_signal,
    f033obs_f033_obv_slope_emaobv_252d_slope_v078_signal,
    f033obs_f033_obv_slope_emaobv_252d_slope_v079_signal,
    f033obs_f033_obv_slope_emaobv_252d_slope_v080_signal,
    f033obs_f033_obv_slope_stdobvslope_21d_slope_v081_signal,
    f033obs_f033_obv_slope_stdobvslope_21d_slope_v082_signal,
    f033obs_f033_obv_slope_stdobvslope_63d_slope_v083_signal,
    f033obs_f033_obv_slope_stdobvslope_63d_slope_v084_signal,
    f033obs_f033_obv_slope_stdobvslope_126d_slope_v085_signal,
    f033obs_f033_obv_slope_stdobvslope_126d_slope_v086_signal,
    f033obs_f033_obv_slope_stdobvslope_252d_slope_v087_signal,
    f033obs_f033_obv_slope_stdobvslope_252d_slope_v088_signal,
    f033obs_f033_obv_slope_stdobvslope_252d_slope_v089_signal,
    f033obs_f033_obv_slope_stdobvslope_252d_slope_v090_signal,
    f033obs_f033_obv_slope_sqobvslope_21d_slope_v091_signal,
    f033obs_f033_obv_slope_sqobvslope_21d_slope_v092_signal,
    f033obs_f033_obv_slope_sqobvslope_63d_slope_v093_signal,
    f033obs_f033_obv_slope_sqobvslope_63d_slope_v094_signal,
    f033obs_f033_obv_slope_sqobvslope_126d_slope_v095_signal,
    f033obs_f033_obv_slope_sqobvslope_126d_slope_v096_signal,
    f033obs_f033_obv_slope_sqobvslope_252d_slope_v097_signal,
    f033obs_f033_obv_slope_sqobvslope_252d_slope_v098_signal,
    f033obs_f033_obv_slope_sqobvslope_252d_slope_v099_signal,
    f033obs_f033_obv_slope_sqobvslope_252d_slope_v100_signal,
    f033obs_f033_obv_slope_obvgap_21d_slope_v101_signal,
    f033obs_f033_obv_slope_obvgap_21d_slope_v102_signal,
    f033obs_f033_obv_slope_obvgap_63d_slope_v103_signal,
    f033obs_f033_obv_slope_obvgap_63d_slope_v104_signal,
    f033obs_f033_obv_slope_obvgap_126d_slope_v105_signal,
    f033obs_f033_obv_slope_obvgap_126d_slope_v106_signal,
    f033obs_f033_obv_slope_obvgap_252d_slope_v107_signal,
    f033obs_f033_obv_slope_obvgap_252d_slope_v108_signal,
    f033obs_f033_obv_slope_obvgap_252d_slope_v109_signal,
    f033obs_f033_obv_slope_obvgap_252d_slope_v110_signal,
    f033obs_f033_obv_slope_obvslopexvol_21d_slope_v111_signal,
    f033obs_f033_obv_slope_obvslopexvol_21d_slope_v112_signal,
    f033obs_f033_obv_slope_obvslopexvol_63d_slope_v113_signal,
    f033obs_f033_obv_slope_obvslopexvol_63d_slope_v114_signal,
    f033obs_f033_obv_slope_obvslopexvol_126d_slope_v115_signal,
    f033obs_f033_obv_slope_obvslopexvol_126d_slope_v116_signal,
    f033obs_f033_obv_slope_obvslopexvol_252d_slope_v117_signal,
    f033obs_f033_obv_slope_obvslopexvol_252d_slope_v118_signal,
    f033obs_f033_obv_slope_obvslopexvol_252d_slope_v119_signal,
    f033obs_f033_obv_slope_obvslopexvol_252d_slope_v120_signal,
    f033obs_f033_obv_slope_zobvtrend_21d_slope_v121_signal,
    f033obs_f033_obv_slope_zobvtrend_21d_slope_v122_signal,
    f033obs_f033_obv_slope_zobvtrend_63d_slope_v123_signal,
    f033obs_f033_obv_slope_zobvtrend_63d_slope_v124_signal,
    f033obs_f033_obv_slope_zobvtrend_126d_slope_v125_signal,
    f033obs_f033_obv_slope_zobvtrend_126d_slope_v126_signal,
    f033obs_f033_obv_slope_zobvtrend_252d_slope_v127_signal,
    f033obs_f033_obv_slope_zobvtrend_252d_slope_v128_signal,
    f033obs_f033_obv_slope_zobvtrend_252d_slope_v129_signal,
    f033obs_f033_obv_slope_zobvtrend_252d_slope_v130_signal,
    f033obs_f033_obv_slope_obvslopexsign_21d_slope_v131_signal,
    f033obs_f033_obv_slope_obvslopexsign_21d_slope_v132_signal,
    f033obs_f033_obv_slope_obvslopexsign_63d_slope_v133_signal,
    f033obs_f033_obv_slope_obvslopexsign_63d_slope_v134_signal,
    f033obs_f033_obv_slope_obvslopexsign_126d_slope_v135_signal,
    f033obs_f033_obv_slope_obvslopexsign_126d_slope_v136_signal,
    f033obs_f033_obv_slope_obvslopexsign_252d_slope_v137_signal,
    f033obs_f033_obv_slope_obvslopexsign_252d_slope_v138_signal,
    f033obs_f033_obv_slope_obvslopexsign_252d_slope_v139_signal,
    f033obs_f033_obv_slope_obvslopexsign_252d_slope_v140_signal,
    f033obs_f033_obv_slope_absobvslope_21d_slope_v141_signal,
    f033obs_f033_obv_slope_absobvslope_21d_slope_v142_signal,
    f033obs_f033_obv_slope_absobvslope_63d_slope_v143_signal,
    f033obs_f033_obv_slope_absobvslope_63d_slope_v144_signal,
    f033obs_f033_obv_slope_absobvslope_126d_slope_v145_signal,
    f033obs_f033_obv_slope_absobvslope_126d_slope_v146_signal,
    f033obs_f033_obv_slope_absobvslope_252d_slope_v147_signal,
    f033obs_f033_obv_slope_absobvslope_252d_slope_v148_signal,
    f033obs_f033_obv_slope_absobvslope_252d_slope_v149_signal,
    f033obs_f033_obv_slope_absobvslope_252d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F033_OBV_SLOPE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f033_obv_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
