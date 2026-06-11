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


def _f038_vol_avg(volume, w):
    return volume.rolling(w, min_periods=max(1, w // 2)).mean()


def _f038_vol_slope(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return avg.diff(periods=w) / avg.abs().replace(0, np.nan)


def _f038_vol_slope_acceleration(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    sl = avg.diff(periods=w) / avg.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def f038vta_f038_volume_trend_acceleration_vavg_10d_jerk_v001_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 10) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_21d_jerk_v002_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v003_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 42) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v004_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 42) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v005_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 42) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v006_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 42) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v007_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v008_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v009_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v010_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v011_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 126) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v012_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 126) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v013_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 126) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v014_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 126) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v015_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 189) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v016_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 189) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v017_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 189) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v018_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 189) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v019_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 252) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v020_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 252) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v021_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 252) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v022_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 252) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v023_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 378) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v024_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 378) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v025_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 378) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v026_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 378) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v027_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 504) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v028_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 504) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v029_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 504) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v030_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 504) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_5d_jerk_v031_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 5), 21) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_10d_jerk_v032_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 10), 21) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_21d_jerk_v033_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 21), 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_42d_jerk_v034_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 42), 21) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_63d_jerk_v035_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 63), 21) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_126d_jerk_v036_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 126), 21) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_189d_jerk_v037_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 189), 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_252d_jerk_v038_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 252), 21) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_378d_jerk_v039_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 378), 21) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_504d_jerk_v040_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 504), 21) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_5d_jerk_v041_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 5), 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_10d_jerk_v042_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 10), 21) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_21d_jerk_v043_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 21), 21) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_42d_jerk_v044_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 42), 21) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_63d_jerk_v045_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 63), 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_126d_jerk_v046_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 126), 21) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_189d_jerk_v047_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 189), 21) * closeadj / 1e3
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_252d_jerk_v048_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 252), 21) * closeadj / 1e3
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_378d_jerk_v049_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 378), 21) * closeadj / 1e3
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vavgsmooth_504d_jerk_v050_signal(volume, closeadj):
    base = _mean(_f038_vol_avg(volume, 504), 21) * closeadj / 1e3
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_10d_jerk_v051_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_21d_jerk_v052_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v053_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v054_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v055_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v056_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v057_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v058_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v059_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v060_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v061_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v062_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v063_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v064_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v065_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v066_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v067_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v068_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v069_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v070_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v071_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v072_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v073_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v074_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v075_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v076_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v077_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v078_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v079_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v080_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_5d_jerk_v081_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 5), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_10d_jerk_v082_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 10), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_21d_jerk_v083_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_42d_jerk_v084_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_63d_jerk_v085_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_126d_jerk_v086_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 126), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_189d_jerk_v087_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 189), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_252d_jerk_v088_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 252), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_378d_jerk_v089_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 378), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_504d_jerk_v090_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 504), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_5d_jerk_v091_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 5), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_10d_jerk_v092_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 10), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_21d_jerk_v093_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_42d_jerk_v094_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 42), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_63d_jerk_v095_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_126d_jerk_v096_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_189d_jerk_v097_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_252d_jerk_v098_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 252), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_378d_jerk_v099_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 378), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vslopesm_504d_jerk_v100_signal(volume, closeadj):
    base = _mean(_f038_vol_slope(volume, 504), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_10d_jerk_v101_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_21d_jerk_v102_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v103_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v104_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v105_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v106_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v107_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v108_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v109_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v110_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v111_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v112_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v113_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v114_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v115_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v116_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v117_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v118_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v119_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v120_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v121_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v122_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v123_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v124_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v125_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v126_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v127_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v128_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v129_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v130_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 252) * closeadj
    result = _jerk(base, 21) * (volume / volume.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_5d_jerk_v131_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 5), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_10d_jerk_v132_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 10), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_21d_jerk_v133_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_42d_jerk_v134_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_63d_jerk_v135_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_126d_jerk_v136_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 126), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_189d_jerk_v137_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 189), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_252d_jerk_v138_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 252), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_378d_jerk_v139_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 378), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_504d_jerk_v140_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 252), 21) * closeadj
    result = _jerk(base, 21) * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_5d_jerk_v141_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 5), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_10d_jerk_v142_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 10), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_21d_jerk_v143_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_42d_jerk_v144_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 42), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_63d_jerk_v145_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_126d_jerk_v146_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_189d_jerk_v147_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_252d_jerk_v148_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 252), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_378d_jerk_v149_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 378), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f038vta_f038_volume_trend_acceleration_vaccelsm_504d_jerk_v150_signal(volume, closeadj):
    base = _mean(_f038_vol_slope_acceleration(volume, 504), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f038vta_f038_volume_trend_acceleration_vavg_10d_jerk_v001_signal,
    f038vta_f038_volume_trend_acceleration_vavg_21d_jerk_v002_signal,
    f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v003_signal,
    f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v004_signal,
    f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v005_signal,
    f038vta_f038_volume_trend_acceleration_vavg_42d_jerk_v006_signal,
    f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v007_signal,
    f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v008_signal,
    f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v009_signal,
    f038vta_f038_volume_trend_acceleration_vavg_63d_jerk_v010_signal,
    f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v011_signal,
    f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v012_signal,
    f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v013_signal,
    f038vta_f038_volume_trend_acceleration_vavg_126d_jerk_v014_signal,
    f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v015_signal,
    f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v016_signal,
    f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v017_signal,
    f038vta_f038_volume_trend_acceleration_vavg_189d_jerk_v018_signal,
    f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v019_signal,
    f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v020_signal,
    f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v021_signal,
    f038vta_f038_volume_trend_acceleration_vavg_252d_jerk_v022_signal,
    f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v023_signal,
    f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v024_signal,
    f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v025_signal,
    f038vta_f038_volume_trend_acceleration_vavg_378d_jerk_v026_signal,
    f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v027_signal,
    f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v028_signal,
    f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v029_signal,
    f038vta_f038_volume_trend_acceleration_vavg_504d_jerk_v030_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_5d_jerk_v031_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_10d_jerk_v032_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_21d_jerk_v033_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_42d_jerk_v034_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_63d_jerk_v035_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_126d_jerk_v036_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_189d_jerk_v037_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_252d_jerk_v038_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_378d_jerk_v039_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_504d_jerk_v040_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_5d_jerk_v041_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_10d_jerk_v042_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_21d_jerk_v043_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_42d_jerk_v044_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_63d_jerk_v045_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_126d_jerk_v046_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_189d_jerk_v047_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_252d_jerk_v048_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_378d_jerk_v049_signal,
    f038vta_f038_volume_trend_acceleration_vavgsmooth_504d_jerk_v050_signal,
    f038vta_f038_volume_trend_acceleration_vslope_10d_jerk_v051_signal,
    f038vta_f038_volume_trend_acceleration_vslope_21d_jerk_v052_signal,
    f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v053_signal,
    f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v054_signal,
    f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v055_signal,
    f038vta_f038_volume_trend_acceleration_vslope_42d_jerk_v056_signal,
    f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v057_signal,
    f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v058_signal,
    f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v059_signal,
    f038vta_f038_volume_trend_acceleration_vslope_63d_jerk_v060_signal,
    f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v061_signal,
    f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v062_signal,
    f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v063_signal,
    f038vta_f038_volume_trend_acceleration_vslope_126d_jerk_v064_signal,
    f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v065_signal,
    f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v066_signal,
    f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v067_signal,
    f038vta_f038_volume_trend_acceleration_vslope_189d_jerk_v068_signal,
    f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v069_signal,
    f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v070_signal,
    f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v071_signal,
    f038vta_f038_volume_trend_acceleration_vslope_252d_jerk_v072_signal,
    f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v073_signal,
    f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v074_signal,
    f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v075_signal,
    f038vta_f038_volume_trend_acceleration_vslope_378d_jerk_v076_signal,
    f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v077_signal,
    f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v078_signal,
    f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v079_signal,
    f038vta_f038_volume_trend_acceleration_vslope_504d_jerk_v080_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_5d_jerk_v081_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_10d_jerk_v082_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_21d_jerk_v083_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_42d_jerk_v084_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_63d_jerk_v085_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_126d_jerk_v086_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_189d_jerk_v087_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_252d_jerk_v088_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_378d_jerk_v089_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_504d_jerk_v090_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_5d_jerk_v091_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_10d_jerk_v092_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_21d_jerk_v093_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_42d_jerk_v094_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_63d_jerk_v095_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_126d_jerk_v096_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_189d_jerk_v097_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_252d_jerk_v098_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_378d_jerk_v099_signal,
    f038vta_f038_volume_trend_acceleration_vslopesm_504d_jerk_v100_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_10d_jerk_v101_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_21d_jerk_v102_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v103_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v104_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v105_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_42d_jerk_v106_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v107_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v108_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v109_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_63d_jerk_v110_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v111_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v112_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v113_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_126d_jerk_v114_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v115_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v116_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v117_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_189d_jerk_v118_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v119_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v120_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v121_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_252d_jerk_v122_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v123_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v124_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v125_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_378d_jerk_v126_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v127_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v128_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v129_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_504d_jerk_v130_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_5d_jerk_v131_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_10d_jerk_v132_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_21d_jerk_v133_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_42d_jerk_v134_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_63d_jerk_v135_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_126d_jerk_v136_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_189d_jerk_v137_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_252d_jerk_v138_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_378d_jerk_v139_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_504d_jerk_v140_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_5d_jerk_v141_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_10d_jerk_v142_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_21d_jerk_v143_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_42d_jerk_v144_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_63d_jerk_v145_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_126d_jerk_v146_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_189d_jerk_v147_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_252d_jerk_v148_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_378d_jerk_v149_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsm_504d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F038_VOLUME_TREND_ACCELERATION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f038_vol_avg", "_f038_vol_slope", "_f038_vol_slope_acceleration")
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
    print(f"OK f038_volume_trend_acceleration_3rd_derivatives_001_150_claude: {n_features} features pass")
