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
def _f02_crash_velocity(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    drop = (trough - peak) / peak.replace(0, np.nan).abs()
    return drop / float(w)


def _f02_crash_slope(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - peak) / (peak.replace(0, np.nan).abs() * float(w))


def _f02_crash_speed_intensity(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    drop = (close - peak)
    rng = (close.rolling(w, min_periods=max(1, w // 2)).max()
           - close.rolling(w, min_periods=max(1, w // 2)).min())
    return drop / (rng.replace(0, np.nan) * float(w))


# 63d crash speed × range
def f02cs_f02_crash_speed_velxrange_63d_base_v076_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_velocity(closeadj, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed × range
def f02cs_f02_crash_speed_velxrange_252d_base_v077_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_velocity(closeadj, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst velocity over 63d window
def f02cs_f02_crash_speed_worstvel_63d_base_v078_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    result = v.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst velocity over 252d window
def f02cs_f02_crash_speed_worstvel_252d_base_v079_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    result = v.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst velocity over 504d window
def f02cs_f02_crash_speed_worstvel_504d_base_v080_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    result = v.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × range
def f02cs_f02_crash_speed_velxrange_21d_v2_base_v081_signal(closeadj, high, low):
    rng = (high - low).rolling(5, min_periods=2).mean()
    result = _f02_crash_velocity(closeadj, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 5d intensity × close (intraweek)
def f02cs_f02_crash_speed_intensity_5d_base_v082_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d intensity × close
def f02cs_f02_crash_speed_intensity_10d_base_v083_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d intensity × close
def f02cs_f02_crash_speed_intensity_42d_base_v084_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d intensity × close
def f02cs_f02_crash_speed_intensity_189d_base_v085_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d intensity × close
def f02cs_f02_crash_speed_intensity_378d_base_v086_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_21d_base_v087_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 21) * closeadj * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_63d_base_v088_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 63) * closeadj * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_252d_base_v089_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 252) * closeadj * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × ATR scaled by close
def f02cs_f02_crash_speed_velxatrnorm_21d_base_v090_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_velocity(closeadj, 21) * atr * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity × ATR-norm
def f02cs_f02_crash_speed_velxatrnorm_63d_base_v091_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_velocity(closeadj, 63) * atr * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × cumulative downside vol over 21d
def f02cs_f02_crash_speed_slopexcumdown_21d_base_v092_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_slope(closeadj, 21) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × cumulative downside vol
def f02cs_f02_crash_speed_slopexcumdown_63d_base_v093_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_slope(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × cumulative downside vol
def f02cs_f02_crash_speed_slopexcumdown_252d_base_v094_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_slope(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × current return × close
def f02cs_f02_crash_speed_velxret_21d_base_v095_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f02_crash_velocity(closeadj, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity × 63d return × close
def f02cs_f02_crash_speed_velxret_63d_base_v096_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f02_crash_velocity(closeadj, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity × 252d return × close
def f02cs_f02_crash_speed_velxret_252d_base_v097_signal(closeadj):
    r = closeadj.pct_change(252)
    result = _f02_crash_velocity(closeadj, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intensity × volume z
def f02cs_f02_crash_speed_intensxvolz_21d_base_v098_signal(closeadj, volume):
    result = _f02_crash_speed_intensity(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intensity × volume z
def f02cs_f02_crash_speed_intensxvolz_63d_base_v099_signal(closeadj, volume):
    result = _f02_crash_speed_intensity(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intensity × volume z
def f02cs_f02_crash_speed_intensxvolz_252d_base_v100_signal(closeadj, volume):
    result = _f02_crash_speed_intensity(closeadj, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity area (cumulative |velocity| over 63d)
def f02cs_f02_crash_speed_velarea_63d_base_v101_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21).abs()
    result = v.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity area (cumulative |velocity| over 252d)
def f02cs_f02_crash_speed_velarea_252d_base_v102_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63).abs()
    result = v.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity area (cumulative |velocity| over 504d)
def f02cs_f02_crash_speed_velarea_504d_base_v103_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252).abs()
    result = v.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity diff over 21d (acceleration)
def f02cs_f02_crash_speed_velaccel_21d_base_v104_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    result = (v - v.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity diff over 63d (acceleration)
def f02cs_f02_crash_speed_velaccel_63d_base_v105_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    result = (v - v.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity diff over 63d (acceleration)
def f02cs_f02_crash_speed_velaccel_252d_base_v106_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    result = (v - v.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × ATR (volatile-fast crash slope)
def f02cs_f02_crash_speed_slopexatr_21d_base_v107_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_slope(closeadj, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × ATR
def f02cs_f02_crash_speed_slopexatr_63d_base_v108_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_slope(closeadj, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × ATR
def f02cs_f02_crash_speed_slopexatr_252d_base_v109_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_slope(closeadj, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope mean over 63d × close
def f02cs_f02_crash_speed_slopemean_63d_base_v110_signal(closeadj):
    result = _mean(_f02_crash_slope(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope mean over 252d × close
def f02cs_f02_crash_speed_slopemean_252d_base_v111_signal(closeadj):
    result = _mean(_f02_crash_slope(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope std over 63d × close
def f02cs_f02_crash_speed_slopestd_63d_base_v112_signal(closeadj):
    result = _std(_f02_crash_slope(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope std over 252d × close
def f02cs_f02_crash_speed_slopestd_252d_base_v113_signal(closeadj):
    result = _std(_f02_crash_slope(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding crash velocity worst-ever × close
def f02cs_f02_crash_speed_velworstever_base_v114_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    result = v.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity gap to expanding worst-ever
def f02cs_f02_crash_speed_velvshistworst_252d_base_v115_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    worst = v.expanding(min_periods=63).min()
    result = (v - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash velocity gap to expanding worst-ever
def f02cs_f02_crash_speed_velvshistworst_504d_base_v116_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 504)
    worst = v.expanding(min_periods=126).min()
    result = (v - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × cumulative volume × close
def f02cs_f02_crash_speed_slopexcumvol_21d_base_v117_signal(closeadj, volume):
    cv = volume.rolling(21, min_periods=5).sum()
    result = _f02_crash_slope(closeadj, 21) * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × cumulative volume × close
def f02cs_f02_crash_speed_slopexcumvol_63d_base_v118_signal(closeadj, volume):
    cv = volume.rolling(63, min_periods=21).sum()
    result = _f02_crash_slope(closeadj, 63) * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intensity × ATR
def f02cs_f02_crash_speed_intensxatr_21d_base_v119_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_speed_intensity(closeadj, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intensity × ATR
def f02cs_f02_crash_speed_intensxatr_63d_base_v120_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_speed_intensity(closeadj, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × kurtosis-skew composite
def f02cs_f02_crash_speed_velxtails_63d_base_v121_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f02_crash_velocity(closeadj, 63) * (sk - kt) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity × kurtosis-skew composite
def f02cs_f02_crash_speed_velxtails_252d_base_v122_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f02_crash_velocity(closeadj, 252) * (sk - kt) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope EMA × close
def f02cs_f02_crash_speed_slopeema_21d_base_v123_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 21)
    result = sl.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope EMA × close
def f02cs_f02_crash_speed_slopeema_63d_base_v124_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 63)
    result = sl.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope EMA × close
def f02cs_f02_crash_speed_slopeema_252d_base_v125_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 252)
    result = sl.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity vol-of-vol over 63d × close
def f02cs_f02_crash_speed_velvolvol_63d_base_v126_signal(closeadj):
    sd = _std(_f02_crash_velocity(closeadj, 63), 63)
    result = _std(sd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity vol-of-vol over 252d × close
def f02cs_f02_crash_speed_velvolvol_252d_base_v127_signal(closeadj):
    sd = _std(_f02_crash_velocity(closeadj, 252), 252)
    result = _std(sd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope - 63d slope (slope acceleration)
def f02cs_f02_crash_speed_slopediff_21m63_base_v128_signal(closeadj):
    result = (_f02_crash_slope(closeadj, 21) - _f02_crash_slope(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope - 252d slope
def f02cs_f02_crash_speed_slopediff_63m252_base_v129_signal(closeadj):
    result = (_f02_crash_slope(closeadj, 63) - _f02_crash_slope(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope - 504d slope
def f02cs_f02_crash_speed_slopediff_252m504_base_v130_signal(closeadj):
    result = (_f02_crash_slope(closeadj, 252) - _f02_crash_slope(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of fast-crash days (large daily declines per window)
def f02cs_f02_crash_speed_fastdecl_252d_base_v131_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.03).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + 1.0) * _f02_crash_velocity(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of fast-crash days × velocity
def f02cs_f02_crash_speed_fastdecl_63d_base_v132_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.02).astype(float)
    cnt = flag.rolling(63, min_periods=21).sum()
    result = (cnt + 1.0) * _f02_crash_velocity(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of fast-crash days × velocity
def f02cs_f02_crash_speed_fastdecl_504d_base_v133_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.04).astype(float)
    cnt = flag.rolling(504, min_periods=126).sum()
    result = (cnt + 1.0) * _f02_crash_velocity(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × volume cumulated 5d
def f02cs_f02_crash_speed_velxcumvol_21d_base_v134_signal(closeadj, volume):
    cv = volume.rolling(5, min_periods=2).sum()
    result = _f02_crash_velocity(closeadj, 21) * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity × volume cumulated 21d
def f02cs_f02_crash_speed_velxcumvol_63d_base_v135_signal(closeadj, volume):
    cv = volume.rolling(21, min_periods=5).sum()
    result = _f02_crash_velocity(closeadj, 63) * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × current dollar volume
def f02cs_f02_crash_speed_slopexcurdv_21d_base_v136_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × current dollar volume
def f02cs_f02_crash_speed_slopexcurdv_252d_base_v137_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × range × close
def f02cs_f02_crash_speed_slopexrange_21d_base_v138_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_slope(closeadj, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × range × close
def f02cs_f02_crash_speed_slopexrange_63d_base_v139_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_slope(closeadj, 63) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite crash speed (vel + slope absolute)
def f02cs_f02_crash_speed_compositespeed_21d_base_v140_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21).abs()
    sl = _f02_crash_slope(closeadj, 21).abs()
    result = (v + sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite crash speed
def f02cs_f02_crash_speed_compositespeed_63d_base_v141_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63).abs()
    sl = _f02_crash_slope(closeadj, 63).abs()
    result = (v + sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite crash speed
def f02cs_f02_crash_speed_compositespeed_252d_base_v142_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252).abs()
    sl = _f02_crash_slope(closeadj, 252).abs()
    result = (v + sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite crash speed
def f02cs_f02_crash_speed_compositespeed_504d_base_v143_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 504).abs()
    sl = _f02_crash_slope(closeadj, 504).abs()
    result = (v + sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crash velocity × peak proximity (deeper decline if at low)
def f02cs_f02_crash_speed_velxpeakprox_63d_base_v144_signal(closeadj):
    peak = closeadj.rolling(63, min_periods=21).max().replace(0, np.nan)
    prox = closeadj / peak
    result = _f02_crash_velocity(closeadj, 63) * prox * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crash velocity × peak proximity at 252d
def f02cs_f02_crash_speed_velxpeakprox_252d_base_v145_signal(closeadj):
    peak = closeadj.rolling(252, min_periods=63).max().replace(0, np.nan)
    prox = closeadj / peak
    result = _f02_crash_velocity(closeadj, 252) * prox * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_21d_base_v146_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_speed_intensity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_63d_base_v147_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_speed_intensity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_252d_base_v148_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_speed_intensity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × cumulative downside count
def f02cs_f02_crash_speed_velxdowncount_63d_base_v149_signal(closeadj):
    r = closeadj.pct_change()
    dc = (r < 0).astype(float).rolling(63, min_periods=21).sum()
    result = _f02_crash_velocity(closeadj, 63) * dc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity × cumulative downside count
def f02cs_f02_crash_speed_velxdowncount_252d_base_v150_signal(closeadj):
    r = closeadj.pct_change()
    dc = (r < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _f02_crash_velocity(closeadj, 252) * dc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cs_f02_crash_speed_velxrange_63d_base_v076_signal,
    f02cs_f02_crash_speed_velxrange_252d_base_v077_signal,
    f02cs_f02_crash_speed_worstvel_63d_base_v078_signal,
    f02cs_f02_crash_speed_worstvel_252d_base_v079_signal,
    f02cs_f02_crash_speed_worstvel_504d_base_v080_signal,
    f02cs_f02_crash_speed_velxrange_21d_v2_base_v081_signal,
    f02cs_f02_crash_speed_intensity_5d_base_v082_signal,
    f02cs_f02_crash_speed_intensity_10d_base_v083_signal,
    f02cs_f02_crash_speed_intensity_42d_base_v084_signal,
    f02cs_f02_crash_speed_intensity_189d_base_v085_signal,
    f02cs_f02_crash_speed_intensity_378d_base_v086_signal,
    f02cs_f02_crash_speed_slopeintens_21d_base_v087_signal,
    f02cs_f02_crash_speed_slopeintens_63d_base_v088_signal,
    f02cs_f02_crash_speed_slopeintens_252d_base_v089_signal,
    f02cs_f02_crash_speed_velxatrnorm_21d_base_v090_signal,
    f02cs_f02_crash_speed_velxatrnorm_63d_base_v091_signal,
    f02cs_f02_crash_speed_slopexcumdown_21d_base_v092_signal,
    f02cs_f02_crash_speed_slopexcumdown_63d_base_v093_signal,
    f02cs_f02_crash_speed_slopexcumdown_252d_base_v094_signal,
    f02cs_f02_crash_speed_velxret_21d_base_v095_signal,
    f02cs_f02_crash_speed_velxret_63d_base_v096_signal,
    f02cs_f02_crash_speed_velxret_252d_base_v097_signal,
    f02cs_f02_crash_speed_intensxvolz_21d_base_v098_signal,
    f02cs_f02_crash_speed_intensxvolz_63d_base_v099_signal,
    f02cs_f02_crash_speed_intensxvolz_252d_base_v100_signal,
    f02cs_f02_crash_speed_velarea_63d_base_v101_signal,
    f02cs_f02_crash_speed_velarea_252d_base_v102_signal,
    f02cs_f02_crash_speed_velarea_504d_base_v103_signal,
    f02cs_f02_crash_speed_velaccel_21d_base_v104_signal,
    f02cs_f02_crash_speed_velaccel_63d_base_v105_signal,
    f02cs_f02_crash_speed_velaccel_252d_base_v106_signal,
    f02cs_f02_crash_speed_slopexatr_21d_base_v107_signal,
    f02cs_f02_crash_speed_slopexatr_63d_base_v108_signal,
    f02cs_f02_crash_speed_slopexatr_252d_base_v109_signal,
    f02cs_f02_crash_speed_slopemean_63d_base_v110_signal,
    f02cs_f02_crash_speed_slopemean_252d_base_v111_signal,
    f02cs_f02_crash_speed_slopestd_63d_base_v112_signal,
    f02cs_f02_crash_speed_slopestd_252d_base_v113_signal,
    f02cs_f02_crash_speed_velworstever_base_v114_signal,
    f02cs_f02_crash_speed_velvshistworst_252d_base_v115_signal,
    f02cs_f02_crash_speed_velvshistworst_504d_base_v116_signal,
    f02cs_f02_crash_speed_slopexcumvol_21d_base_v117_signal,
    f02cs_f02_crash_speed_slopexcumvol_63d_base_v118_signal,
    f02cs_f02_crash_speed_intensxatr_21d_base_v119_signal,
    f02cs_f02_crash_speed_intensxatr_63d_base_v120_signal,
    f02cs_f02_crash_speed_velxtails_63d_base_v121_signal,
    f02cs_f02_crash_speed_velxtails_252d_base_v122_signal,
    f02cs_f02_crash_speed_slopeema_21d_base_v123_signal,
    f02cs_f02_crash_speed_slopeema_63d_base_v124_signal,
    f02cs_f02_crash_speed_slopeema_252d_base_v125_signal,
    f02cs_f02_crash_speed_velvolvol_63d_base_v126_signal,
    f02cs_f02_crash_speed_velvolvol_252d_base_v127_signal,
    f02cs_f02_crash_speed_slopediff_21m63_base_v128_signal,
    f02cs_f02_crash_speed_slopediff_63m252_base_v129_signal,
    f02cs_f02_crash_speed_slopediff_252m504_base_v130_signal,
    f02cs_f02_crash_speed_fastdecl_252d_base_v131_signal,
    f02cs_f02_crash_speed_fastdecl_63d_base_v132_signal,
    f02cs_f02_crash_speed_fastdecl_504d_base_v133_signal,
    f02cs_f02_crash_speed_velxcumvol_21d_base_v134_signal,
    f02cs_f02_crash_speed_velxcumvol_63d_base_v135_signal,
    f02cs_f02_crash_speed_slopexcurdv_21d_base_v136_signal,
    f02cs_f02_crash_speed_slopexcurdv_252d_base_v137_signal,
    f02cs_f02_crash_speed_slopexrange_21d_base_v138_signal,
    f02cs_f02_crash_speed_slopexrange_63d_base_v139_signal,
    f02cs_f02_crash_speed_compositespeed_21d_base_v140_signal,
    f02cs_f02_crash_speed_compositespeed_63d_base_v141_signal,
    f02cs_f02_crash_speed_compositespeed_252d_base_v142_signal,
    f02cs_f02_crash_speed_compositespeed_504d_base_v143_signal,
    f02cs_f02_crash_speed_velxpeakprox_63d_base_v144_signal,
    f02cs_f02_crash_speed_velxpeakprox_252d_base_v145_signal,
    f02cs_f02_crash_speed_intensxdownvol_21d_base_v146_signal,
    f02cs_f02_crash_speed_intensxdownvol_63d_base_v147_signal,
    f02cs_f02_crash_speed_intensxdownvol_252d_base_v148_signal,
    f02cs_f02_crash_speed_velxdowncount_63d_base_v149_signal,
    f02cs_f02_crash_speed_velxdowncount_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_CRASH_SPEED_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f02_crash_velocity", "_f02_crash_slope", "_f02_crash_speed_intensity")
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
    print(f"OK f02_crash_speed_base_076_150_claude: {n_features} features pass")
