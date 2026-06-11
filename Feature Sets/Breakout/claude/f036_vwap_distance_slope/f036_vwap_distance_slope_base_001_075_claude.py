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
def _f036_vwap(close, volume, w):
    pv = (close * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return pv / vv.replace(0, np.nan)


def _f036_vwap_distance(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return (close - vwap) / vwap.replace(0, np.nan).abs()


def _f036_vwap_slope(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return vwap.diff(periods=w) / vwap.abs().replace(0, np.nan)


# 21d vwap level scaled by close
def f036vds_f036_vwap_distance_slope_vwaplevel_21d_base_v001_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 21) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_63d_base_v002_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 63) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_126d_base_v003_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 126) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_252d_base_v004_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 252) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_504d_base_v005_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 504) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_5d_base_v006_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 5) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_10d_base_v007_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 10) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_42d_base_v008_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 42) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_189d_base_v009_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 189) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vwap level
def f036vds_f036_vwap_distance_slope_vwaplevel_378d_base_v010_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 378) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap gap (price - vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_21d_base_v011_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_63d_base_v012_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_126d_base_v013_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_252d_base_v014_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_504d_base_v015_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_5d_base_v016_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_10d_base_v017_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_42d_base_v018_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_189d_base_v019_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vwap gap
def f036vds_f036_vwap_distance_slope_vwapgap_378d_base_v020_signal(closeadj, volume):
    result = closeadj - _f036_vwap(closeadj, volume, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_21d_base_v021_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_63d_base_v022_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_126d_base_v023_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_252d_base_v024_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_504d_base_v025_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_5d_base_v026_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_10d_base_v027_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_42d_base_v028_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_189d_base_v029_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vwap relative distance
def f036vds_f036_vwap_distance_slope_vwapdist_378d_base_v030_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × volume
def f036vds_f036_vwap_distance_slope_distxvol_21d_base_v031_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × volume
def f036vds_f036_vwap_distance_slope_distxvol_63d_base_v032_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap distance × volume
def f036vds_f036_vwap_distance_slope_distxvol_126d_base_v033_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × volume
def f036vds_f036_vwap_distance_slope_distxvol_252d_base_v034_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × dollar volume
def f036vds_f036_vwap_distance_slope_distxdv_21d_base_v035_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × dollar volume
def f036vds_f036_vwap_distance_slope_distxdv_63d_base_v036_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap distance × dollar volume
def f036vds_f036_vwap_distance_slope_distxdv_126d_base_v037_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 126) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × dollar volume
def f036vds_f036_vwap_distance_slope_distxdv_252d_base_v038_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of vwap distance × close
def f036vds_f036_vwap_distance_slope_meandist_21d_base_v039_signal(closeadj, volume):
    result = _mean(_f036_vwap_distance(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of vwap distance × close
def f036vds_f036_vwap_distance_slope_meandist_63d_base_v040_signal(closeadj, volume):
    result = _mean(_f036_vwap_distance(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of vwap distance × close
def f036vds_f036_vwap_distance_slope_meandist_126d_base_v041_signal(closeadj, volume):
    result = _mean(_f036_vwap_distance(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of vwap distance × close
def f036vds_f036_vwap_distance_slope_meandist_252d_base_v042_signal(closeadj, volume):
    result = _mean(_f036_vwap_distance(closeadj, volume, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of vwap distance × close
def f036vds_f036_vwap_distance_slope_stddist_21d_base_v043_signal(closeadj, volume):
    result = _std(_f036_vwap_distance(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of vwap distance × close
def f036vds_f036_vwap_distance_slope_stddist_63d_base_v044_signal(closeadj, volume):
    result = _std(_f036_vwap_distance(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of vwap distance × close
def f036vds_f036_vwap_distance_slope_stddist_126d_base_v045_signal(closeadj, volume):
    result = _std(_f036_vwap_distance(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of vwap distance × close
def f036vds_f036_vwap_distance_slope_zdist_21d_base_v046_signal(closeadj, volume):
    result = _z(_f036_vwap_distance(closeadj, volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of vwap distance × close
def f036vds_f036_vwap_distance_slope_zdist_63d_base_v047_signal(closeadj, volume):
    result = _z(_f036_vwap_distance(closeadj, volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of vwap distance × close
def f036vds_f036_vwap_distance_slope_zdist_126d_base_v048_signal(closeadj, volume):
    result = _z(_f036_vwap_distance(closeadj, volume, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_21d_base_v049_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_63d_base_v050_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_126d_base_v051_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_252d_base_v052_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_504d_base_v053_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_5d_base_v054_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_10d_base_v055_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_42d_base_v056_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_189d_base_v057_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vwap slope × close
def f036vds_f036_vwap_distance_slope_vwapslope_378d_base_v058_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × volume
def f036vds_f036_vwap_distance_slope_vslopevol_21d_base_v059_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × volume
def f036vds_f036_vwap_distance_slope_vslopevol_63d_base_v060_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap slope × volume
def f036vds_f036_vwap_distance_slope_vslopevol_126d_base_v061_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × volume
def f036vds_f036_vwap_distance_slope_vslopevol_252d_base_v062_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × dollar volume
def f036vds_f036_vwap_distance_slope_vslopedv_21d_base_v063_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × dollar volume
def f036vds_f036_vwap_distance_slope_vslopedv_63d_base_v064_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap slope × dollar volume
def f036vds_f036_vwap_distance_slope_vslopedv_126d_base_v065_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 126) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × dollar volume
def f036vds_f036_vwap_distance_slope_vslopedv_252d_base_v066_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of vwap slope × close
def f036vds_f036_vwap_distance_slope_meanslope_21d_base_v067_signal(closeadj, volume):
    result = _mean(_f036_vwap_slope(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of vwap slope × close
def f036vds_f036_vwap_distance_slope_meanslope_63d_base_v068_signal(closeadj, volume):
    result = _mean(_f036_vwap_slope(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of vwap slope × close
def f036vds_f036_vwap_distance_slope_meanslope_126d_base_v069_signal(closeadj, volume):
    result = _mean(_f036_vwap_slope(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of vwap slope × close
def f036vds_f036_vwap_distance_slope_stdslope_21d_base_v070_signal(closeadj, volume):
    result = _std(_f036_vwap_slope(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of vwap slope × close
def f036vds_f036_vwap_distance_slope_stdslope_63d_base_v071_signal(closeadj, volume):
    result = _std(_f036_vwap_slope(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of vwap slope × close
def f036vds_f036_vwap_distance_slope_zslope_21d_base_v072_signal(closeadj, volume):
    result = _z(_f036_vwap_slope(closeadj, volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of vwap slope × close
def f036vds_f036_vwap_distance_slope_zslope_63d_base_v073_signal(closeadj, volume):
    result = _z(_f036_vwap_slope(closeadj, volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × vwap slope (composite)
def f036vds_f036_vwap_distance_slope_distxslope_21d_base_v074_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * _f036_vwap_slope(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × vwap slope (composite)
def f036vds_f036_vwap_distance_slope_distxslope_63d_base_v075_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * _f036_vwap_slope(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f036vds_f036_vwap_distance_slope_vwaplevel_21d_base_v001_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_63d_base_v002_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_126d_base_v003_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_252d_base_v004_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_504d_base_v005_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_5d_base_v006_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_10d_base_v007_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_42d_base_v008_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_189d_base_v009_signal,
    f036vds_f036_vwap_distance_slope_vwaplevel_378d_base_v010_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_21d_base_v011_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_63d_base_v012_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_126d_base_v013_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_252d_base_v014_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_504d_base_v015_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_5d_base_v016_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_10d_base_v017_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_42d_base_v018_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_189d_base_v019_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_378d_base_v020_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_21d_base_v021_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_63d_base_v022_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_126d_base_v023_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_252d_base_v024_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_504d_base_v025_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_5d_base_v026_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_10d_base_v027_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_42d_base_v028_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_189d_base_v029_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_378d_base_v030_signal,
    f036vds_f036_vwap_distance_slope_distxvol_21d_base_v031_signal,
    f036vds_f036_vwap_distance_slope_distxvol_63d_base_v032_signal,
    f036vds_f036_vwap_distance_slope_distxvol_126d_base_v033_signal,
    f036vds_f036_vwap_distance_slope_distxvol_252d_base_v034_signal,
    f036vds_f036_vwap_distance_slope_distxdv_21d_base_v035_signal,
    f036vds_f036_vwap_distance_slope_distxdv_63d_base_v036_signal,
    f036vds_f036_vwap_distance_slope_distxdv_126d_base_v037_signal,
    f036vds_f036_vwap_distance_slope_distxdv_252d_base_v038_signal,
    f036vds_f036_vwap_distance_slope_meandist_21d_base_v039_signal,
    f036vds_f036_vwap_distance_slope_meandist_63d_base_v040_signal,
    f036vds_f036_vwap_distance_slope_meandist_126d_base_v041_signal,
    f036vds_f036_vwap_distance_slope_meandist_252d_base_v042_signal,
    f036vds_f036_vwap_distance_slope_stddist_21d_base_v043_signal,
    f036vds_f036_vwap_distance_slope_stddist_63d_base_v044_signal,
    f036vds_f036_vwap_distance_slope_stddist_126d_base_v045_signal,
    f036vds_f036_vwap_distance_slope_zdist_21d_base_v046_signal,
    f036vds_f036_vwap_distance_slope_zdist_63d_base_v047_signal,
    f036vds_f036_vwap_distance_slope_zdist_126d_base_v048_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_21d_base_v049_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_63d_base_v050_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_126d_base_v051_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_252d_base_v052_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_504d_base_v053_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_5d_base_v054_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_10d_base_v055_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_42d_base_v056_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_189d_base_v057_signal,
    f036vds_f036_vwap_distance_slope_vwapslope_378d_base_v058_signal,
    f036vds_f036_vwap_distance_slope_vslopevol_21d_base_v059_signal,
    f036vds_f036_vwap_distance_slope_vslopevol_63d_base_v060_signal,
    f036vds_f036_vwap_distance_slope_vslopevol_126d_base_v061_signal,
    f036vds_f036_vwap_distance_slope_vslopevol_252d_base_v062_signal,
    f036vds_f036_vwap_distance_slope_vslopedv_21d_base_v063_signal,
    f036vds_f036_vwap_distance_slope_vslopedv_63d_base_v064_signal,
    f036vds_f036_vwap_distance_slope_vslopedv_126d_base_v065_signal,
    f036vds_f036_vwap_distance_slope_vslopedv_252d_base_v066_signal,
    f036vds_f036_vwap_distance_slope_meanslope_21d_base_v067_signal,
    f036vds_f036_vwap_distance_slope_meanslope_63d_base_v068_signal,
    f036vds_f036_vwap_distance_slope_meanslope_126d_base_v069_signal,
    f036vds_f036_vwap_distance_slope_stdslope_21d_base_v070_signal,
    f036vds_f036_vwap_distance_slope_stdslope_63d_base_v071_signal,
    f036vds_f036_vwap_distance_slope_zslope_21d_base_v072_signal,
    f036vds_f036_vwap_distance_slope_zslope_63d_base_v073_signal,
    f036vds_f036_vwap_distance_slope_distxslope_21d_base_v074_signal,
    f036vds_f036_vwap_distance_slope_distxslope_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F036_VWAP_DISTANCE_SLOPE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f036_vwap", "_f036_vwap_distance", "_f036_vwap_slope")
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
    print(f"OK f036_vwap_distance_slope_base_001_075_claude: {n_features} features pass")
