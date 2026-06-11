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


# 21d vol avg z-score × close
def f038vta_f038_volume_trend_acceleration_zvavg_21d_base_v076_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg z-score × close
def f038vta_f038_volume_trend_acceleration_zvavg_63d_base_v077_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol avg z-score × close
def f038vta_f038_volume_trend_acceleration_zvavg_252d_base_v078_signal(volume, closeadj):
    result = _z(_f038_vol_avg(volume, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg × close × std volume
def f038vta_f038_volume_trend_acceleration_vavgxstd_21d_base_v079_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * closeadj * _std(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × close × std volume
def f038vta_f038_volume_trend_acceleration_vavgxstd_63d_base_v080_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 63) * closeadj * _std(volume, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × close std
def f038vta_f038_volume_trend_acceleration_vslopexclstd_21d_base_v081_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × close std
def f038vta_f038_volume_trend_acceleration_vslopexclstd_63d_base_v082_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × close std
def f038vta_f038_volume_trend_acceleration_vaccelxclstd_21d_base_v083_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × close std
def f038vta_f038_volume_trend_acceleration_vaccelxclstd_63d_base_v084_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × close × volume
def f038vta_f038_volume_trend_acceleration_vslopexcv_21d_base_v085_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × close × volume
def f038vta_f038_volume_trend_acceleration_vslopexcv_63d_base_v086_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × close × volume
def f038vta_f038_volume_trend_acceleration_vaccelxcv_21d_base_v087_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × close × volume
def f038vta_f038_volume_trend_acceleration_vaccelxcv_63d_base_v088_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg × close × volume / 1e6
def f038vta_f038_volume_trend_acceleration_vavgxcv_21d_base_v089_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * closeadj * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × close × volume / 1e6
def f038vta_f038_volume_trend_acceleration_vavgxcv_63d_base_v090_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 63) * closeadj * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol avg × close × volume / 1e6
def f038vta_f038_volume_trend_acceleration_vavgxcv_252d_base_v091_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 252) * closeadj * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt vol avg × close
def f038vta_f038_volume_trend_acceleration_sqrtvavg_21d_base_v092_signal(volume, closeadj):
    result = _z(np.sqrt(_f038_vol_avg(volume, 21).abs()), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt vol avg × close
def f038vta_f038_volume_trend_acceleration_sqrtvavg_63d_base_v093_signal(volume, closeadj):
    result = _z(np.sqrt(_f038_vol_avg(volume, 63).abs()), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs vol slope × close
def f038vta_f038_volume_trend_acceleration_absvslope_21d_base_v094_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs vol slope × close
def f038vta_f038_volume_trend_acceleration_absvslope_63d_base_v095_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs vol slope × close
def f038vta_f038_volume_trend_acceleration_absvslope_252d_base_v096_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs vol accel × close
def f038vta_f038_volume_trend_acceleration_absvaccel_21d_base_v097_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs vol accel × close
def f038vta_f038_volume_trend_acceleration_absvaccel_63d_base_v098_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg × z close
def f038vta_f038_volume_trend_acceleration_vavgxzcl_21d_base_v099_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * _z(closeadj, 63) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × z close
def f038vta_f038_volume_trend_acceleration_vavgxzcl_63d_base_v100_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 63) * _z(closeadj, 126) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × z close
def f038vta_f038_volume_trend_acceleration_vslopexzcl_21d_base_v101_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × z close
def f038vta_f038_volume_trend_acceleration_vslopexzcl_63d_base_v102_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _z(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × z close
def f038vta_f038_volume_trend_acceleration_vaccelxzcl_21d_base_v103_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × z close
def f038vta_f038_volume_trend_acceleration_vaccelxzcl_63d_base_v104_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * _z(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × close mean
def f038vta_f038_volume_trend_acceleration_vslopexclmn_21d_base_v105_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × close mean
def f038vta_f038_volume_trend_acceleration_vslopexclmn_63d_base_v106_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope × close mean
def f038vta_f038_volume_trend_acceleration_vslopexclmn_252d_base_v107_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 252) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × close mean
def f038vta_f038_volume_trend_acceleration_vaccelxclmn_21d_base_v108_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × close mean
def f038vta_f038_volume_trend_acceleration_vaccelxclmn_63d_base_v109_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol accel × close mean
def f038vta_f038_volume_trend_acceleration_vaccelxclmn_252d_base_v110_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 252) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg × log close
def f038vta_f038_volume_trend_acceleration_vavgxlogcl_21d_base_v111_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × log close
def f038vta_f038_volume_trend_acceleration_vavgxlogcl_63d_base_v112_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol avg × log close
def f038vta_f038_volume_trend_acceleration_vavgxlogcl_252d_base_v113_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 252) * np.log(closeadj.replace(0, np.nan).abs()) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × log close
def f038vta_f038_volume_trend_acceleration_vslopexlogcl_21d_base_v114_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × log close
def f038vta_f038_volume_trend_acceleration_vslopexlogcl_63d_base_v115_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope acceleration × log close
def f038vta_f038_volume_trend_acceleration_vaccelxlogcl_21d_base_v116_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope acceleration × log close
def f038vta_f038_volume_trend_acceleration_vaccelxlogcl_63d_base_v117_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope cubed sign × close
def f038vta_f038_volume_trend_acceleration_vslopecub_21d_base_v118_signal(volume, closeadj):
    s = _f038_vol_slope(volume, 21)
    result = s * s.abs() * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope cubed sign × close
def f038vta_f038_volume_trend_acceleration_vslopecub_63d_base_v119_signal(volume, closeadj):
    s = _f038_vol_slope(volume, 63)
    result = s * s.abs() * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel cubed sign × close
def f038vta_f038_volume_trend_acceleration_vaccelcub_21d_base_v120_signal(volume, closeadj):
    s = _f038_vol_slope_acceleration(volume, 21)
    result = s * s.abs() * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d trend persistence count × close (vol slope > 0)
def f038vta_f038_volume_trend_acceleration_vsloperising_21d_base_v121_signal(volume, closeadj):
    rising = (_f038_vol_slope(volume, 21) > 0).astype(float)
    result = rising.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend persistence count × close (vol slope > 0)
def f038vta_f038_volume_trend_acceleration_vsloperising_63d_base_v122_signal(volume, closeadj):
    rising = (_f038_vol_slope(volume, 63) > 0).astype(float)
    result = rising.rolling(63, min_periods=10).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend persistence count × close (vol slope > 0)
def f038vta_f038_volume_trend_acceleration_vsloperising_252d_base_v123_signal(volume, closeadj):
    rising = (_f038_vol_slope(volume, 252) > 0).astype(float)
    result = rising.rolling(252, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel persistence count × close
def f038vta_f038_volume_trend_acceleration_vaccelrising_21d_base_v124_signal(volume, closeadj):
    rising = (_f038_vol_slope_acceleration(volume, 21) > 0).astype(float)
    result = rising.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel persistence count × close
def f038vta_f038_volume_trend_acceleration_vaccelrising_63d_base_v125_signal(volume, closeadj):
    rising = (_f038_vol_slope_acceleration(volume, 63) > 0).astype(float)
    result = rising.rolling(63, min_periods=10).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope normalized by std × close
def f038vta_f038_volume_trend_acceleration_vslopenorm_21d_base_v126_signal(volume, closeadj):
    sl = _f038_vol_slope(volume, 21)
    result = _safe_div(sl, _std(sl, 63) + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope normalized by std × close
def f038vta_f038_volume_trend_acceleration_vslopenorm_63d_base_v127_signal(volume, closeadj):
    sl = _f038_vol_slope(volume, 63)
    result = _safe_div(sl, _std(sl, 126) + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel normalized by std × close
def f038vta_f038_volume_trend_acceleration_vaccelnorm_21d_base_v128_signal(volume, closeadj):
    sl = _f038_vol_slope_acceleration(volume, 21)
    result = _safe_div(sl, _std(sl, 63) + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel normalized by std × close
def f038vta_f038_volume_trend_acceleration_vaccelnorm_63d_base_v129_signal(volume, closeadj):
    sl = _f038_vol_slope_acceleration(volume, 63)
    result = _safe_div(sl, _std(sl, 126) + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg / median vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavgmedgap_21d_base_v130_signal(volume, closeadj):
    avg = _f038_vol_avg(volume, 21)
    med = avg.rolling(63, min_periods=21).median()
    result = (avg - med) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg / median vol avg gap × close
def f038vta_f038_volume_trend_acceleration_vavgmedgap_63d_base_v131_signal(volume, closeadj):
    avg = _f038_vol_avg(volume, 63)
    med = avg.rolling(126, min_periods=21).median()
    result = (avg - med) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope + accel composite × close
def f038vta_f038_volume_trend_acceleration_vsla_21d_base_v132_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 21) + _f038_vol_slope_acceleration(volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope + accel composite × close
def f038vta_f038_volume_trend_acceleration_vsla_63d_base_v133_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 63) + _f038_vol_slope_acceleration(volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope + accel × close
def f038vta_f038_volume_trend_acceleration_vsla_252d_base_v134_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 252) + _f038_vol_slope_acceleration(volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope - accel divergence × close
def f038vta_f038_volume_trend_acceleration_vsdiv_21d_base_v135_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 21) - _f038_vol_slope_acceleration(volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope - accel divergence × close
def f038vta_f038_volume_trend_acceleration_vsdiv_63d_base_v136_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 63) - _f038_vol_slope_acceleration(volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol slope - accel × close
def f038vta_f038_volume_trend_acceleration_vsdiv_252d_base_v137_signal(volume, closeadj):
    result = (_f038_vol_slope(volume, 252) - _f038_vol_slope_acceleration(volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema vol avg × close × vol z
def f038vta_f038_volume_trend_acceleration_emaxvolz_21d_base_v138_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * _z(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema vol avg × close × vol z
def f038vta_f038_volume_trend_acceleration_emaxvolz_63d_base_v139_signal(volume, closeadj):
    base = _f038_vol_avg(volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * _z(volume, 63) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg × close × vol z
def f038vta_f038_volume_trend_acceleration_vavgxvolz_21d_base_v140_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 21) * closeadj * _z(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg × close × vol z
def f038vta_f038_volume_trend_acceleration_vavgxvolz_63d_base_v141_signal(volume, closeadj):
    result = _f038_vol_avg(volume, 63) * closeadj * _z(volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope × volume z
def f038vta_f038_volume_trend_acceleration_vslopexvolz_21d_base_v142_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol slope × volume z
def f038vta_f038_volume_trend_acceleration_vslopexvolz_63d_base_v143_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel × volume z
def f038vta_f038_volume_trend_acceleration_vaccelxvolz_21d_base_v144_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol accel × volume z
def f038vta_f038_volume_trend_acceleration_vaccelxvolz_63d_base_v145_signal(volume, closeadj):
    result = _f038_vol_slope_acceleration(volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol avg slope × volume std
def f038vta_f038_volume_trend_acceleration_vslopexvstd_21d_base_v146_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 21) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol avg slope × volume std
def f038vta_f038_volume_trend_acceleration_vslopexvstd_63d_base_v147_signal(volume, closeadj):
    result = _f038_vol_slope(volume, 63) * _std(volume, 63) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol slope ratio short vs long
def f038vta_f038_volume_trend_acceleration_vsloperatio_21_252_base_v148_signal(volume, closeadj):
    result = _safe_div(_f038_vol_slope(volume, 21), _f038_vol_slope(volume, 252).abs() + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 504d vol slope ratio
def f038vta_f038_volume_trend_acceleration_vsloperatio_63_504_base_v149_signal(volume, closeadj):
    result = _safe_div(_f038_vol_slope(volume, 63), _f038_vol_slope(volume, 504).abs() + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol accel ratio short vs long
def f038vta_f038_volume_trend_acceleration_vaccelratio_21_252_base_v150_signal(volume, closeadj):
    result = _safe_div(_f038_vol_slope_acceleration(volume, 21), _f038_vol_slope_acceleration(volume, 252).abs() + 1e-10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f038vta_f038_volume_trend_acceleration_zvavg_21d_base_v076_signal,
    f038vta_f038_volume_trend_acceleration_zvavg_63d_base_v077_signal,
    f038vta_f038_volume_trend_acceleration_zvavg_252d_base_v078_signal,
    f038vta_f038_volume_trend_acceleration_vavgxstd_21d_base_v079_signal,
    f038vta_f038_volume_trend_acceleration_vavgxstd_63d_base_v080_signal,
    f038vta_f038_volume_trend_acceleration_vslopexclstd_21d_base_v081_signal,
    f038vta_f038_volume_trend_acceleration_vslopexclstd_63d_base_v082_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxclstd_21d_base_v083_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxclstd_63d_base_v084_signal,
    f038vta_f038_volume_trend_acceleration_vslopexcv_21d_base_v085_signal,
    f038vta_f038_volume_trend_acceleration_vslopexcv_63d_base_v086_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxcv_21d_base_v087_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxcv_63d_base_v088_signal,
    f038vta_f038_volume_trend_acceleration_vavgxcv_21d_base_v089_signal,
    f038vta_f038_volume_trend_acceleration_vavgxcv_63d_base_v090_signal,
    f038vta_f038_volume_trend_acceleration_vavgxcv_252d_base_v091_signal,
    f038vta_f038_volume_trend_acceleration_sqrtvavg_21d_base_v092_signal,
    f038vta_f038_volume_trend_acceleration_sqrtvavg_63d_base_v093_signal,
    f038vta_f038_volume_trend_acceleration_absvslope_21d_base_v094_signal,
    f038vta_f038_volume_trend_acceleration_absvslope_63d_base_v095_signal,
    f038vta_f038_volume_trend_acceleration_absvslope_252d_base_v096_signal,
    f038vta_f038_volume_trend_acceleration_absvaccel_21d_base_v097_signal,
    f038vta_f038_volume_trend_acceleration_absvaccel_63d_base_v098_signal,
    f038vta_f038_volume_trend_acceleration_vavgxzcl_21d_base_v099_signal,
    f038vta_f038_volume_trend_acceleration_vavgxzcl_63d_base_v100_signal,
    f038vta_f038_volume_trend_acceleration_vslopexzcl_21d_base_v101_signal,
    f038vta_f038_volume_trend_acceleration_vslopexzcl_63d_base_v102_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxzcl_21d_base_v103_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxzcl_63d_base_v104_signal,
    f038vta_f038_volume_trend_acceleration_vslopexclmn_21d_base_v105_signal,
    f038vta_f038_volume_trend_acceleration_vslopexclmn_63d_base_v106_signal,
    f038vta_f038_volume_trend_acceleration_vslopexclmn_252d_base_v107_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxclmn_21d_base_v108_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxclmn_63d_base_v109_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxclmn_252d_base_v110_signal,
    f038vta_f038_volume_trend_acceleration_vavgxlogcl_21d_base_v111_signal,
    f038vta_f038_volume_trend_acceleration_vavgxlogcl_63d_base_v112_signal,
    f038vta_f038_volume_trend_acceleration_vavgxlogcl_252d_base_v113_signal,
    f038vta_f038_volume_trend_acceleration_vslopexlogcl_21d_base_v114_signal,
    f038vta_f038_volume_trend_acceleration_vslopexlogcl_63d_base_v115_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxlogcl_21d_base_v116_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxlogcl_63d_base_v117_signal,
    f038vta_f038_volume_trend_acceleration_vslopecub_21d_base_v118_signal,
    f038vta_f038_volume_trend_acceleration_vslopecub_63d_base_v119_signal,
    f038vta_f038_volume_trend_acceleration_vaccelcub_21d_base_v120_signal,
    f038vta_f038_volume_trend_acceleration_vsloperising_21d_base_v121_signal,
    f038vta_f038_volume_trend_acceleration_vsloperising_63d_base_v122_signal,
    f038vta_f038_volume_trend_acceleration_vsloperising_252d_base_v123_signal,
    f038vta_f038_volume_trend_acceleration_vaccelrising_21d_base_v124_signal,
    f038vta_f038_volume_trend_acceleration_vaccelrising_63d_base_v125_signal,
    f038vta_f038_volume_trend_acceleration_vslopenorm_21d_base_v126_signal,
    f038vta_f038_volume_trend_acceleration_vslopenorm_63d_base_v127_signal,
    f038vta_f038_volume_trend_acceleration_vaccelnorm_21d_base_v128_signal,
    f038vta_f038_volume_trend_acceleration_vaccelnorm_63d_base_v129_signal,
    f038vta_f038_volume_trend_acceleration_vavgmedgap_21d_base_v130_signal,
    f038vta_f038_volume_trend_acceleration_vavgmedgap_63d_base_v131_signal,
    f038vta_f038_volume_trend_acceleration_vsla_21d_base_v132_signal,
    f038vta_f038_volume_trend_acceleration_vsla_63d_base_v133_signal,
    f038vta_f038_volume_trend_acceleration_vsla_252d_base_v134_signal,
    f038vta_f038_volume_trend_acceleration_vsdiv_21d_base_v135_signal,
    f038vta_f038_volume_trend_acceleration_vsdiv_63d_base_v136_signal,
    f038vta_f038_volume_trend_acceleration_vsdiv_252d_base_v137_signal,
    f038vta_f038_volume_trend_acceleration_emaxvolz_21d_base_v138_signal,
    f038vta_f038_volume_trend_acceleration_emaxvolz_63d_base_v139_signal,
    f038vta_f038_volume_trend_acceleration_vavgxvolz_21d_base_v140_signal,
    f038vta_f038_volume_trend_acceleration_vavgxvolz_63d_base_v141_signal,
    f038vta_f038_volume_trend_acceleration_vslopexvolz_21d_base_v142_signal,
    f038vta_f038_volume_trend_acceleration_vslopexvolz_63d_base_v143_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxvolz_21d_base_v144_signal,
    f038vta_f038_volume_trend_acceleration_vaccelxvolz_63d_base_v145_signal,
    f038vta_f038_volume_trend_acceleration_vslopexvstd_21d_base_v146_signal,
    f038vta_f038_volume_trend_acceleration_vslopexvstd_63d_base_v147_signal,
    f038vta_f038_volume_trend_acceleration_vsloperatio_21_252_base_v148_signal,
    f038vta_f038_volume_trend_acceleration_vsloperatio_63_504_base_v149_signal,
    f038vta_f038_volume_trend_acceleration_vaccelratio_21_252_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F038_VOLUME_TREND_ACCELERATION_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f038_volume_trend_acceleration_base_076_150_claude: {n_features} features pass")
