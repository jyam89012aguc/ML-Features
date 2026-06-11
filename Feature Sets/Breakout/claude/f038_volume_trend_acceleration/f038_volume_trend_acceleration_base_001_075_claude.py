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
def _f038_vol_avg(volume, w):
    return volume.rolling(w, min_periods=max(1, w // 2)).mean()


def _f038_vol_slope(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return avg.diff(periods=w) / avg.abs().replace(0, np.nan)


def _f038_vol_slope_acceleration(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    sl = avg.diff(periods=w) / avg.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# 21d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_21d_base_v001_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_63d_base_v002_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_126d_base_v003_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_252d_base_v004_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_504d_base_v005_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_5d_base_v006_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 5) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_10d_base_v007_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 10) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_42d_base_v008_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_189d_base_v009_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vol avg × close
def f038vta_f038_volume_trend_acceleration_vavg_378d_base_v010_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_21d_base_v011_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_63d_base_v012_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_126d_base_v013_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_252d_base_v014_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_504d_base_v015_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_5d_base_v016_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_10d_base_v017_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_42d_base_v018_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_189d_base_v019_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vol slope × close
def f038vta_f038_volume_trend_acceleration_vslope_378d_base_v020_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope acceleration × close
def f038vta_f038_volume_trend_acceleration_vaccel_21d_base_v021_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope acceleration × close
def f038vta_f038_volume_trend_acceleration_vaccel_63d_base_v022_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol slope acceleration × close
def f038vta_f038_volume_trend_acceleration_vaccel_126d_base_v023_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope acceleration × close
def f038vta_f038_volume_trend_acceleration_vaccel_252d_base_v024_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol slope acceleration × close
def f038vta_f038_volume_trend_acceleration_vaccel_504d_base_v025_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vol accel × close
def f038vta_f038_volume_trend_acceleration_vaccel_5d_base_v026_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vol accel × close
def f038vta_f038_volume_trend_acceleration_vaccel_10d_base_v027_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vol accel × close
def f038vta_f038_volume_trend_acceleration_vaccel_42d_base_v028_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d vol accel × close
def f038vta_f038_volume_trend_acceleration_vaccel_189d_base_v029_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d vol accel × close
def f038vta_f038_volume_trend_acceleration_vaccel_378d_base_v030_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d short - long vol avg gap (21 vs 252) × close
def f038vta_f038_volume_trend_acceleration_vavggap_21_252_base_v031_signal(volume, closeadj):
    result = (_f038_vol_avg(volume, 21) - _f038_vol_avg(volume, 252)) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21 vs 504 vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavggap_21_504_base_v032_signal(volume, closeadj):
    result = (_f038_vol_avg(volume, 21) - _f038_vol_avg(volume, 504)) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63 vs 252 vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavggap_63_252_base_v033_signal(volume, closeadj):
    result = (_f038_vol_avg(volume, 63) - _f038_vol_avg(volume, 252)) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63 vs 504 vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavggap_63_504_base_v034_signal(volume, closeadj):
    result = (_f038_vol_avg(volume, 63) - _f038_vol_avg(volume, 504)) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 126 vs 504 vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavggap_126_504_base_v035_signal(volume, closeadj):
    result = (_f038_vol_avg(volume, 126) - _f038_vol_avg(volume, 504)) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg ratio (21/252) × close
def f038vta_f038_volume_trend_acceleration_vavgratio_21_252_base_v036_signal(volume, closeadj):
    result = _safe_div(_f038_vol_avg(volume, 21), _f038_vol_avg(volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21 vs 504 vol avg ratio × close
def f038vta_f038_volume_trend_acceleration_vavgratio_21_504_base_v037_signal(volume, closeadj):
    result = _safe_div(_f038_vol_avg(volume, 21), _f038_vol_avg(volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63 vs 252 vol avg ratio × close
def f038vta_f038_volume_trend_acceleration_vavgratio_63_252_base_v038_signal(volume, closeadj):
    result = _z(_safe_div(_f038_vol_avg(volume, 63), _f038_vol_avg(volume, 252)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63 vs 504 vol avg ratio × close
def f038vta_f038_volume_trend_acceleration_vavgratio_63_504_base_v039_signal(volume, closeadj):
    result = _z(_safe_div(_f038_vol_avg(volume, 63), _f038_vol_avg(volume, 504)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126 vs 504 vol avg ratio × close
def f038vta_f038_volume_trend_acceleration_vavgratio_126_504_base_v040_signal(volume, closeadj):
    result = _z(_safe_div(_f038_vol_avg(volume, 126), _f038_vol_avg(volume, 504)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vslopxdvm_21d_base_v041_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _mean(closeadj * volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vslopxdvm_63d_base_v042_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _mean(closeadj * volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vslopxdvm_252d_base_v043_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 252) * _mean(closeadj * volume, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vaccelxdvm_21d_base_v044_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * _mean(closeadj * volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vaccelxdvm_63d_base_v045_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * _mean(closeadj * volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol accel × dollar volume avg
def f038vta_f038_volume_trend_acceleration_vaccelxdvm_252d_base_v046_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 252) * _mean(closeadj * volume, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vol avg × close
def f038vta_f038_volume_trend_acceleration_emavavg_21d_base_v047_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vol avg × close
def f038vta_f038_volume_trend_acceleration_emavavg_63d_base_v048_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of vol avg × close
def f038vta_f038_volume_trend_acceleration_emavavg_252d_base_v049_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 252).ewm(span=126, adjust=False, min_periods=21).mean()
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vol slope × close
def f038vta_f038_volume_trend_acceleration_emavslope_21d_base_v050_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vol slope × close
def f038vta_f038_volume_trend_acceleration_emavslope_63d_base_v051_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of vol slope × close
def f038vta_f038_volume_trend_acceleration_emavslope_252d_base_v052_signal(volume, closeadj):
    base = _f038_vol_slope(volume, 252).ewm(span=126, adjust=False, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vol accel × close
def f038vta_f038_volume_trend_acceleration_emavaccel_21d_base_v053_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vol accel × close
def f038vta_f038_volume_trend_acceleration_emavaccel_63d_base_v054_signal(volume, closeadj):
    base = _f038_vol_slope_acceleration(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of vol avg × close
def f038vta_f038_volume_trend_acceleration_stdvavg_21d_base_v055_signal(volume, closeadj):
    result = _std(_f038_vol_avg(volume, 21), 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of vol avg × close
def f038vta_f038_volume_trend_acceleration_stdvavg_63d_base_v056_signal(volume, closeadj):
    result = _std(_f038_vol_avg(volume, 63), 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of vol slope × close
def f038vta_f038_volume_trend_acceleration_stdvslope_21d_base_v057_signal(volume, closeadj):
    result = _std(_f038_vol_slope(volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of vol slope × close
def f038vta_f038_volume_trend_acceleration_stdvslope_63d_base_v058_signal(volume, closeadj):
    result = _std(_f038_vol_slope(volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score vol slope × close
def f038vta_f038_volume_trend_acceleration_zvslope_21d_base_v059_signal(volume, closeadj):
    result = _z(_f038_vol_slope(volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score vol slope × close
def f038vta_f038_volume_trend_acceleration_zvslope_63d_base_v060_signal(volume, closeadj):
    result = _z(_f038_vol_slope(volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score vol accel × close
def f038vta_f038_volume_trend_acceleration_zvaccel_21d_base_v061_signal(volume, closeadj):
    result = _z(_f038_vol_slope_acceleration(volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score vol accel × close
def f038vta_f038_volume_trend_acceleration_zvaccel_63d_base_v062_signal(volume, closeadj):
    result = _z(_f038_vol_slope_acceleration(volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of vol slope × close
def f038vta_f038_volume_trend_acceleration_signvslope_21d_base_v063_signal(volume, closeadj):
    result = np.sign(_f038_vol_slope(volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of vol slope × close
def f038vta_f038_volume_trend_acceleration_signvslope_63d_base_v064_signal(volume, closeadj):
    result = np.sign(_f038_vol_slope(volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of vol accel × close
def f038vta_f038_volume_trend_acceleration_signvaccel_21d_base_v065_signal(volume, closeadj):
    result = np.sign(_f038_vol_slope_acceleration(volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of vol accel × close
def f038vta_f038_volume_trend_acceleration_signvaccel_63d_base_v066_signal(volume, closeadj):
    result = np.sign(_f038_vol_slope_acceleration(volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log vol avg × close
def f038vta_f038_volume_trend_acceleration_logvavg_21d_base_v067_signal(volume, closeadj):
    result = _z(np.log(_f038_vol_avg(volume, 21).abs().replace(0, np.nan)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log vol avg × close
def f038vta_f038_volume_trend_acceleration_logvavg_63d_base_v068_signal(volume, closeadj):
    result = _z(np.log(_f038_vol_avg(volume, 63).abs().replace(0, np.nan)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log vol avg × close
def f038vta_f038_volume_trend_acceleration_logvavg_252d_base_v069_signal(volume, closeadj):
    result = _z(np.log(_f038_vol_avg(volume, 252).abs().replace(0, np.nan)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope squared × close
def f038vta_f038_volume_trend_acceleration_vslopesq_21d_base_v070_signal(volume, closeadj):
    s = _f038_vol_slope(volume, 21)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope squared × close
def f038vta_f038_volume_trend_acceleration_vslopesq_63d_base_v071_signal(volume, closeadj):
    s = _f038_vol_slope(volume, 63)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel squared × close
def f038vta_f038_volume_trend_acceleration_vaccelsq_21d_base_v072_signal(volume, closeadj):
    s = _f038_vol_slope_acceleration(volume, 21)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel squared × close
def f038vta_f038_volume_trend_acceleration_vaccelsq_63d_base_v073_signal(volume, closeadj):
    s = _f038_vol_slope_acceleration(volume, 63)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × abs vol accel × close (composite)
def f038vta_f038_volume_trend_acceleration_slxabsac_21d_base_v074_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _f038_vol_slope_acceleration(volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × abs vol accel × close
def f038vta_f038_volume_trend_acceleration_slxabsac_63d_base_v075_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _f038_vol_slope_acceleration(volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f038vta_f038_volume_trend_acceleration_vavg_21d_base_v001_signal,
    f038vta_f038_volume_trend_acceleration_vavg_63d_base_v002_signal,
    f038vta_f038_volume_trend_acceleration_vavg_126d_base_v003_signal,
    f038vta_f038_volume_trend_acceleration_vavg_252d_base_v004_signal,
    f038vta_f038_volume_trend_acceleration_vavg_504d_base_v005_signal,
    f038vta_f038_volume_trend_acceleration_vavg_5d_base_v006_signal,
    f038vta_f038_volume_trend_acceleration_vavg_10d_base_v007_signal,
    f038vta_f038_volume_trend_acceleration_vavg_42d_base_v008_signal,
    f038vta_f038_volume_trend_acceleration_vavg_189d_base_v009_signal,
    f038vta_f038_volume_trend_acceleration_vavg_378d_base_v010_signal,
    f038vta_f038_volume_trend_acceleration_vslope_21d_base_v011_signal,
    f038vta_f038_volume_trend_acceleration_vslope_63d_base_v012_signal,
    f038vta_f038_volume_trend_acceleration_vslope_126d_base_v013_signal,
    f038vta_f038_volume_trend_acceleration_vslope_252d_base_v014_signal,
    f038vta_f038_volume_trend_acceleration_vslope_504d_base_v015_signal,
    f038vta_f038_volume_trend_acceleration_vslope_5d_base_v016_signal,
    f038vta_f038_volume_trend_acceleration_vslope_10d_base_v017_signal,
    f038vta_f038_volume_trend_acceleration_vslope_42d_base_v018_signal,
    f038vta_f038_volume_trend_acceleration_vslope_189d_base_v019_signal,
    f038vta_f038_volume_trend_acceleration_vslope_378d_base_v020_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_21d_base_v021_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_63d_base_v022_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_126d_base_v023_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_252d_base_v024_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_504d_base_v025_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_5d_base_v026_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_10d_base_v027_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_42d_base_v028_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_189d_base_v029_signal,
    f038vta_f038_volume_trend_acceleration_vaccel_378d_base_v030_signal,
    f038vta_f038_volume_trend_acceleration_vavggap_21_252_base_v031_signal,
    f038vta_f038_volume_trend_acceleration_vavggap_21_504_base_v032_signal,
    f038vta_f038_volume_trend_acceleration_vavggap_63_252_base_v033_signal,
    f038vta_f038_volume_trend_acceleration_vavggap_63_504_base_v034_signal,
    f038vta_f038_volume_trend_acceleration_vavggap_126_504_base_v035_signal,
    f038vta_f038_volume_trend_acceleration_vavgratio_21_252_base_v036_signal,
    f038vta_f038_volume_trend_acceleration_vavgratio_21_504_base_v037_signal,
    f038vta_f038_volume_trend_acceleration_vavgratio_63_252_base_v038_signal,
    f038vta_f038_volume_trend_acceleration_vavgratio_63_504_base_v039_signal,
    f038vta_f038_volume_trend_acceleration_vavgratio_126_504_base_v040_signal,
    f038vta_f038_volume_trend_acceleration_vslopxdvm_21d_base_v041_signal,
    f038vta_f038_volume_trend_acceleration_vslopxdvm_63d_base_v042_signal,
    f038vta_f038_volume_trend_acceleration_vslopxdvm_252d_base_v043_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxdvm_21d_base_v044_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxdvm_63d_base_v045_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxdvm_252d_base_v046_signal,
    f038vta_f038_volume_trend_acceleration_emavavg_21d_base_v047_signal,
    f038vta_f038_volume_trend_acceleration_emavavg_63d_base_v048_signal,
    f038vta_f038_volume_trend_acceleration_emavavg_252d_base_v049_signal,
    f038vta_f038_volume_trend_acceleration_emavslope_21d_base_v050_signal,
    f038vta_f038_volume_trend_acceleration_emavslope_63d_base_v051_signal,
    f038vta_f038_volume_trend_acceleration_emavslope_252d_base_v052_signal,
    f038vta_f038_volume_trend_acceleration_emavaccel_21d_base_v053_signal,
    f038vta_f038_volume_trend_acceleration_emavaccel_63d_base_v054_signal,
    f038vta_f038_volume_trend_acceleration_stdvavg_21d_base_v055_signal,
    f038vta_f038_volume_trend_acceleration_stdvavg_63d_base_v056_signal,
    f038vta_f038_volume_trend_acceleration_stdvslope_21d_base_v057_signal,
    f038vta_f038_volume_trend_acceleration_stdvslope_63d_base_v058_signal,
    f038vta_f038_volume_trend_acceleration_zvslope_21d_base_v059_signal,
    f038vta_f038_volume_trend_acceleration_zvslope_63d_base_v060_signal,
    f038vta_f038_volume_trend_acceleration_zvaccel_21d_base_v061_signal,
    f038vta_f038_volume_trend_acceleration_zvaccel_63d_base_v062_signal,
    f038vta_f038_volume_trend_acceleration_signvslope_21d_base_v063_signal,
    f038vta_f038_volume_trend_acceleration_signvslope_63d_base_v064_signal,
    f038vta_f038_volume_trend_acceleration_signvaccel_21d_base_v065_signal,
    f038vta_f038_volume_trend_acceleration_signvaccel_63d_base_v066_signal,
    f038vta_f038_volume_trend_acceleration_logvavg_21d_base_v067_signal,
    f038vta_f038_volume_trend_acceleration_logvavg_63d_base_v068_signal,
    f038vta_f038_volume_trend_acceleration_logvavg_252d_base_v069_signal,
    f038vta_f038_volume_trend_acceleration_vslopesq_21d_base_v070_signal,
    f038vta_f038_volume_trend_acceleration_vslopesq_63d_base_v071_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsq_21d_base_v072_signal,
    f038vta_f038_volume_trend_acceleration_vaccelsq_63d_base_v073_signal,
    f038vta_f038_volume_trend_acceleration_slxabsac_21d_base_v074_signal,
    f038vta_f038_volume_trend_acceleration_slxabsac_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F038_VOLUME_TREND_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f038_volume_trend_acceleration_base_001_075_claude: {n_features} features pass")
