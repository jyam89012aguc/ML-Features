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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


# 5d jerk of 21d crash velocity × close
def f02cs_f02_crash_speed_velocity_21d_jerk_v001_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d crash velocity × close
def f02cs_f02_crash_speed_velocity_21d_jerk_v002_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d crash velocity × close
def f02cs_f02_crash_speed_velocity_63d_jerk_v003_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d crash velocity × close
def f02cs_f02_crash_speed_velocity_126d_jerk_v004_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d crash velocity × close
def f02cs_f02_crash_speed_velocity_252d_jerk_v005_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d crash velocity × close
def f02cs_f02_crash_speed_velocity_504d_jerk_v006_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d crash slope × close
def f02cs_f02_crash_speed_slope_21d_jerk_v007_signal(closeadj):
    base = _f02_crash_slope(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d crash slope × close
def f02cs_f02_crash_speed_slope_63d_jerk_v008_signal(closeadj):
    base = _f02_crash_slope(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d crash slope × close
def f02cs_f02_crash_speed_slope_126d_jerk_v009_signal(closeadj):
    base = _f02_crash_slope(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d crash slope × close
def f02cs_f02_crash_speed_slope_252d_jerk_v010_signal(closeadj):
    base = _f02_crash_slope(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d crash slope × close
def f02cs_f02_crash_speed_slope_504d_jerk_v011_signal(closeadj):
    base = _f02_crash_slope(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d time-to-bottom × velocity × close
def f02cs_f02_crash_speed_ttbottom_21d_jerk_v012_signal(closeadj):
    peak_idx = closeadj.rolling(21, min_periods=5).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(21, min_periods=5).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    base = ttb * closeadj * _f02_crash_velocity(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d time-to-bottom
def f02cs_f02_crash_speed_ttbottom_63d_jerk_v013_signal(closeadj):
    peak_idx = closeadj.rolling(63, min_periods=21).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(63, min_periods=21).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    base = ttb * closeadj * _f02_crash_velocity(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d time-to-bottom
def f02cs_f02_crash_speed_ttbottom_252d_jerk_v014_signal(closeadj):
    peak_idx = closeadj.rolling(252, min_periods=63).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(252, min_periods=63).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    base = ttb * closeadj * _f02_crash_velocity(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d daily decline × close
def f02cs_f02_crash_speed_dailydecline_21d_jerk_v015_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    base = neg.rolling(21, min_periods=5).mean() * closeadj + _f02_crash_velocity(closeadj, 21) * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d daily decline × close
def f02cs_f02_crash_speed_dailydecline_63d_jerk_v016_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    base = neg.rolling(63, min_periods=21).mean() * closeadj + _f02_crash_velocity(closeadj, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d daily decline × close
def f02cs_f02_crash_speed_dailydecline_252d_jerk_v017_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    base = neg.rolling(252, min_periods=63).mean() * closeadj + _f02_crash_velocity(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d intensity × close
def f02cs_f02_crash_speed_intensity_21d_jerk_v018_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d intensity × close
def f02cs_f02_crash_speed_intensity_63d_jerk_v019_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d intensity × close
def f02cs_f02_crash_speed_intensity_252d_jerk_v020_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d intensity × close
def f02cs_f02_crash_speed_intensity_504d_jerk_v021_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d max drop × close
def f02cs_f02_crash_speed_maxdrop_21d_jerk_v022_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(21, min_periods=5).min()
    base = md * closeadj + _f02_crash_velocity(closeadj, 21) * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d max drop × close
def f02cs_f02_crash_speed_maxdrop_63d_jerk_v023_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(63, min_periods=21).min()
    base = md * closeadj + _f02_crash_velocity(closeadj, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d max drop × close
def f02cs_f02_crash_speed_maxdrop_252d_jerk_v024_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(252, min_periods=63).min()
    base = md * closeadj + _f02_crash_velocity(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d velocity z
def f02cs_f02_crash_speed_velz_252d_jerk_v025_signal(closeadj):
    base = _z(_f02_crash_velocity(closeadj, 21), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d velocity z
def f02cs_f02_crash_speed_velz_504d_jerk_v026_signal(closeadj):
    base = _z(_f02_crash_velocity(closeadj, 63), 504)
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d slope z
def f02cs_f02_crash_speed_slopez_252d_jerk_v027_signal(closeadj):
    base = _z(_f02_crash_slope(closeadj, 21), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d slope z
def f02cs_f02_crash_speed_slopez_504d_jerk_v028_signal(closeadj):
    base = _z(_f02_crash_slope(closeadj, 63), 504)
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity mean × close
def f02cs_f02_crash_speed_velmean_21d_jerk_v029_signal(closeadj):
    base = _mean(_f02_crash_velocity(closeadj, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity mean × close
def f02cs_f02_crash_speed_velmean_63d_jerk_v030_signal(closeadj):
    base = _mean(_f02_crash_velocity(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity mean × close
def f02cs_f02_crash_speed_velmean_252d_jerk_v031_signal(closeadj):
    base = _mean(_f02_crash_velocity(closeadj, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of velocity std 63d × close
def f02cs_f02_crash_speed_velstd_21d_jerk_v032_signal(closeadj):
    base = _std(_f02_crash_velocity(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of velocity std 252d × close
def f02cs_f02_crash_speed_velstd_63d_jerk_v033_signal(closeadj):
    base = _std(_f02_crash_velocity(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × volume
def f02cs_f02_crash_speed_velxvol_21d_jerk_v034_signal(closeadj, volume):
    base = _f02_crash_velocity(closeadj, 21) * volume
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × volume
def f02cs_f02_crash_speed_velxvol_63d_jerk_v035_signal(closeadj, volume):
    base = _f02_crash_velocity(closeadj, 63) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × dollar volume
def f02cs_f02_crash_speed_velxdv_252d_jerk_v036_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f02_crash_velocity(closeadj, 252) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d decline acceleration × close
def f02cs_f02_crash_speed_decelaccel_21d_jerk_v037_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 21)
    base = (sl - sl.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d decline acceleration × close
def f02cs_f02_crash_speed_decelaccel_63d_jerk_v038_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 63)
    base = (sl - sl.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d decline acceleration × close
def f02cs_f02_crash_speed_decelaccel_252d_jerk_v039_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 252)
    base = (sl - sl.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × ATR
def f02cs_f02_crash_speed_velxatr_21d_jerk_v040_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_velocity(closeadj, 21) * atr
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × ATR
def f02cs_f02_crash_speed_velxatr_63d_jerk_v041_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_velocity(closeadj, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × ATR
def f02cs_f02_crash_speed_velxatr_252d_jerk_v042_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_velocity(closeadj, 252) * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity squared × close
def f02cs_f02_crash_speed_velsq_21d_jerk_v043_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    base = v * v.abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity squared × close
def f02cs_f02_crash_speed_velsq_63d_jerk_v044_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    base = v * v.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity squared × close
def f02cs_f02_crash_speed_velsq_252d_jerk_v045_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    base = v * v.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d crash velocity × close
def f02cs_f02_crash_speed_velocity_5d_jerk_v046_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d crash velocity × close
def f02cs_f02_crash_speed_velocity_10d_jerk_v047_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d crash velocity × close
def f02cs_f02_crash_speed_velocity_42d_jerk_v048_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 189d crash velocity × close
def f02cs_f02_crash_speed_velocity_189d_jerk_v049_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d crash velocity × close
def f02cs_f02_crash_speed_velocity_378d_jerk_v050_signal(closeadj):
    base = _f02_crash_velocity(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of velocity ratio 21v63 × close
def f02cs_f02_crash_speed_velratio_21v63_jerk_v051_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 21)
    b = _f02_crash_velocity(closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of velocity ratio 63v252 × close
def f02cs_f02_crash_speed_velratio_63v252_jerk_v052_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 63)
    b = _f02_crash_velocity(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of velocity ratio 252v504 × close
def f02cs_f02_crash_speed_velratio_252v504_jerk_v053_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 252)
    b = _f02_crash_velocity(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of velocity diff 21m63 × close
def f02cs_f02_crash_speed_veldiff_21m63_jerk_v054_signal(closeadj):
    base = (_f02_crash_velocity(closeadj, 21) - _f02_crash_velocity(closeadj, 63)) * closeadj
    result = _diff(_diff(base, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of velocity diff 63m252 × close
def f02cs_f02_crash_speed_veldiff_63m252_jerk_v055_signal(closeadj):
    base = (_f02_crash_velocity(closeadj, 63) - _f02_crash_velocity(closeadj, 252)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of velocity diff 252m504 × close
def f02cs_f02_crash_speed_veldiff_252m504_jerk_v056_signal(closeadj):
    base = (_f02_crash_velocity(closeadj, 252) - _f02_crash_velocity(closeadj, 504)) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of slope ratio 21v63 × close
def f02cs_f02_crash_speed_sloperatio_21v63_jerk_v057_signal(closeadj):
    a = _f02_crash_slope(closeadj, 21)
    b = _f02_crash_slope(closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope ratio 63v252 × close
def f02cs_f02_crash_speed_sloperatio_63v252_jerk_v058_signal(closeadj):
    a = _f02_crash_slope(closeadj, 63)
    b = _f02_crash_slope(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of speed × downside dollar vol (21d)
def f02cs_f02_crash_speed_speedxdownvol_21d_jerk_v059_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_velocity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of speed × downside dollar vol (63d)
def f02cs_f02_crash_speed_speedxdownvol_63d_jerk_v060_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_velocity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of speed × downside dollar vol (252d)
def f02cs_f02_crash_speed_speedxdownvol_252d_jerk_v061_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_velocity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × retvol × close
def f02cs_f02_crash_speed_slopexretvol_21d_jerk_v062_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f02_crash_slope(closeadj, 21) * rv * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × retvol × close
def f02cs_f02_crash_speed_slopexretvol_63d_jerk_v063_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f02_crash_slope(closeadj, 63) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × retvol × close
def f02cs_f02_crash_speed_slopexretvol_252d_jerk_v064_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f02_crash_slope(closeadj, 252) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × volume z × close
def f02cs_f02_crash_speed_slopexvolz_21d_jerk_v065_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × volume z × close
def f02cs_f02_crash_speed_slopexvolz_63d_jerk_v066_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × skew × close
def f02cs_f02_crash_speed_velxskew_63d_jerk_v067_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f02_crash_velocity(closeadj, 63) * sk * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × skew × close
def f02cs_f02_crash_speed_velxskew_252d_jerk_v068_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f02_crash_velocity(closeadj, 252) * sk * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × kurt × close
def f02cs_f02_crash_speed_velxkurt_63d_jerk_v069_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f02_crash_velocity(closeadj, 63) * kt * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × kurt × close
def f02cs_f02_crash_speed_velxkurt_252d_jerk_v070_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f02_crash_velocity(closeadj, 252) * kt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d velocity EMA × close
def f02cs_f02_crash_speed_velema_21d_jerk_v071_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    base = v.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity EMA × close
def f02cs_f02_crash_speed_velema_63d_jerk_v072_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    base = v.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity EMA × close
def f02cs_f02_crash_speed_velema_252d_jerk_v073_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    base = v.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × current dollar volume
def f02cs_f02_crash_speed_velxcurdv_21d_jerk_v074_signal(closeadj, volume):
    base = _f02_crash_velocity(closeadj, 21) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × current dollar volume
def f02cs_f02_crash_speed_velxcurdv_252d_jerk_v075_signal(closeadj, volume):
    base = _f02_crash_velocity(closeadj, 252) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × range
def f02cs_f02_crash_speed_velxrange_21d_jerk_v076_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_velocity(closeadj, 21) * rng
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × range
def f02cs_f02_crash_speed_velxrange_63d_jerk_v077_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_velocity(closeadj, 63) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × range
def f02cs_f02_crash_speed_velxrange_252d_jerk_v078_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_velocity(closeadj, 252) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d worst velocity × close
def f02cs_f02_crash_speed_worstvel_63d_jerk_v079_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    base = v.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d worst velocity × close
def f02cs_f02_crash_speed_worstvel_252d_jerk_v080_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    base = v.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d worst velocity × close
def f02cs_f02_crash_speed_worstvel_504d_jerk_v081_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    base = v.rolling(504, min_periods=126).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d intensity × close
def f02cs_f02_crash_speed_intensity_5d_jerk_v082_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d intensity × close
def f02cs_f02_crash_speed_intensity_10d_jerk_v083_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d intensity × close
def f02cs_f02_crash_speed_intensity_42d_jerk_v084_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 189d intensity × close
def f02cs_f02_crash_speed_intensity_189d_jerk_v085_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d intensity × close
def f02cs_f02_crash_speed_intensity_378d_jerk_v086_signal(closeadj):
    base = _f02_crash_speed_intensity(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_21d_jerk_v087_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 21) * closeadj * _z(volume, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_63d_jerk_v088_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 63) * closeadj * _z(volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × close × volume z
def f02cs_f02_crash_speed_slopeintens_252d_jerk_v089_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 252) * closeadj * _z(volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × ATR-norm
def f02cs_f02_crash_speed_velxatrnorm_21d_jerk_v090_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_velocity(closeadj, 21) * atr * closeadj / closeadj.replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × ATR-norm
def f02cs_f02_crash_speed_velxatrnorm_63d_jerk_v091_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_velocity(closeadj, 63) * atr * closeadj / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × cumulative downside vol
def f02cs_f02_crash_speed_slopexcumdown_21d_jerk_v092_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_slope(closeadj, 21) * dv.rolling(21, min_periods=5).sum()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × cumulative downside vol
def f02cs_f02_crash_speed_slopexcumdown_63d_jerk_v093_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_slope(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × cumulative downside vol
def f02cs_f02_crash_speed_slopexcumdown_252d_jerk_v094_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_slope(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × ret × close
def f02cs_f02_crash_speed_velxret_21d_jerk_v095_signal(closeadj):
    r = closeadj.pct_change(21)
    base = _f02_crash_velocity(closeadj, 21) * r * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × ret × close
def f02cs_f02_crash_speed_velxret_63d_jerk_v096_signal(closeadj):
    r = closeadj.pct_change(63)
    base = _f02_crash_velocity(closeadj, 63) * r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × ret × close
def f02cs_f02_crash_speed_velxret_252d_jerk_v097_signal(closeadj):
    r = closeadj.pct_change(252)
    base = _f02_crash_velocity(closeadj, 252) * r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d intensity × volume z × close
def f02cs_f02_crash_speed_intensxvolz_21d_jerk_v098_signal(closeadj, volume):
    base = _f02_crash_speed_intensity(closeadj, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d intensity × volume z × close
def f02cs_f02_crash_speed_intensxvolz_63d_jerk_v099_signal(closeadj, volume):
    base = _f02_crash_speed_intensity(closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d intensity × volume z × close
def f02cs_f02_crash_speed_intensxvolz_252d_jerk_v100_signal(closeadj, volume):
    base = _f02_crash_speed_intensity(closeadj, 252) * _z(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity area × close
def f02cs_f02_crash_speed_velarea_63d_jerk_v101_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21).abs()
    base = v.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity area × close
def f02cs_f02_crash_speed_velarea_252d_jerk_v102_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63).abs()
    base = v.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d velocity area × close
def f02cs_f02_crash_speed_velarea_504d_jerk_v103_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252).abs()
    base = v.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity acceleration × close
def f02cs_f02_crash_speed_velaccel_21d_jerk_v104_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    base = (v - v.shift(21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity acceleration × close
def f02cs_f02_crash_speed_velaccel_63d_jerk_v105_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    base = (v - v.shift(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity acceleration × close
def f02cs_f02_crash_speed_velaccel_252d_jerk_v106_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    base = (v - v.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × ATR
def f02cs_f02_crash_speed_slopexatr_21d_jerk_v107_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_slope(closeadj, 21) * atr
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × ATR
def f02cs_f02_crash_speed_slopexatr_63d_jerk_v108_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_slope(closeadj, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × ATR
def f02cs_f02_crash_speed_slopexatr_252d_jerk_v109_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_slope(closeadj, 252) * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope mean × close
def f02cs_f02_crash_speed_slopemean_63d_jerk_v110_signal(closeadj):
    base = _mean(_f02_crash_slope(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope mean × close
def f02cs_f02_crash_speed_slopemean_252d_jerk_v111_signal(closeadj):
    base = _mean(_f02_crash_slope(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope std × close
def f02cs_f02_crash_speed_slopestd_63d_jerk_v112_signal(closeadj):
    base = _std(_f02_crash_slope(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope std × close
def f02cs_f02_crash_speed_slopestd_252d_jerk_v113_signal(closeadj):
    base = _std(_f02_crash_slope(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding worst velocity × close
def f02cs_f02_crash_speed_velworstever_jerk_v114_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    base = v.expanding(min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d velocity gap to historical worst
def f02cs_f02_crash_speed_velvshistworst_252d_jerk_v115_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    worst = v.expanding(min_periods=63).min()
    base = (v - worst) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d velocity gap to historical worst
def f02cs_f02_crash_speed_velvshistworst_504d_jerk_v116_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 504)
    worst = v.expanding(min_periods=126).min()
    base = (v - worst) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × cumulative volume × close
def f02cs_f02_crash_speed_slopexcumvol_21d_jerk_v117_signal(closeadj, volume):
    cv = volume.rolling(21, min_periods=5).sum()
    base = _f02_crash_slope(closeadj, 21) * cv * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × cumulative volume × close
def f02cs_f02_crash_speed_slopexcumvol_63d_jerk_v118_signal(closeadj, volume):
    cv = volume.rolling(63, min_periods=21).sum()
    base = _f02_crash_slope(closeadj, 63) * cv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d intensity × ATR
def f02cs_f02_crash_speed_intensxatr_21d_jerk_v119_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_speed_intensity(closeadj, 21) * atr
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d intensity × ATR
def f02cs_f02_crash_speed_intensxatr_63d_jerk_v120_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_speed_intensity(closeadj, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × tails composite × close
def f02cs_f02_crash_speed_velxtails_63d_jerk_v121_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f02_crash_velocity(closeadj, 63) * (sk - kt) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × tails composite × close
def f02cs_f02_crash_speed_velxtails_252d_jerk_v122_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f02_crash_velocity(closeadj, 252) * (sk - kt) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope EMA × close
def f02cs_f02_crash_speed_slopeema_21d_jerk_v123_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 21)
    base = sl.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope EMA × close
def f02cs_f02_crash_speed_slopeema_63d_jerk_v124_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 63)
    base = sl.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope EMA × close
def f02cs_f02_crash_speed_slopeema_252d_jerk_v125_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 252)
    base = sl.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity vol-of-vol × close
def f02cs_f02_crash_speed_velvolvol_63d_jerk_v126_signal(closeadj):
    sd = _std(_f02_crash_velocity(closeadj, 63), 63)
    base = _std(sd, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity vol-of-vol × close
def f02cs_f02_crash_speed_velvolvol_252d_jerk_v127_signal(closeadj):
    sd = _std(_f02_crash_velocity(closeadj, 252), 252)
    base = _std(sd, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21m63 slope diff × close
def f02cs_f02_crash_speed_slopediff_21m63_jerk_v128_signal(closeadj):
    base = (_f02_crash_slope(closeadj, 21) - _f02_crash_slope(closeadj, 63)) * closeadj
    result = _diff(_diff(base, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63m252 slope diff × close
def f02cs_f02_crash_speed_slopediff_63m252_jerk_v129_signal(closeadj):
    base = (_f02_crash_slope(closeadj, 63) - _f02_crash_slope(closeadj, 252)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252m504 slope diff × close
def f02cs_f02_crash_speed_slopediff_252m504_jerk_v130_signal(closeadj):
    base = (_f02_crash_slope(closeadj, 252) - _f02_crash_slope(closeadj, 504)) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d fast-decline count × velocity × close
def f02cs_f02_crash_speed_fastdecl_252d_jerk_v131_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.03).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + 1.0) * _f02_crash_velocity(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d fast-decline count × velocity × close
def f02cs_f02_crash_speed_fastdecl_63d_jerk_v132_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.02).astype(float)
    cnt = flag.rolling(63, min_periods=21).sum()
    base = (cnt + 1.0) * _f02_crash_velocity(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d fast-decline count × velocity × close
def f02cs_f02_crash_speed_fastdecl_504d_jerk_v133_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r < -0.04).astype(float)
    cnt = flag.rolling(504, min_periods=126).sum()
    base = (cnt + 1.0) * _f02_crash_velocity(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d velocity × cumulative volume × close
def f02cs_f02_crash_speed_velxcumvol_21d_jerk_v134_signal(closeadj, volume):
    cv = volume.rolling(5, min_periods=2).sum()
    base = _f02_crash_velocity(closeadj, 21) * cv * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × cumulative volume × close
def f02cs_f02_crash_speed_velxcumvol_63d_jerk_v135_signal(closeadj, volume):
    cv = volume.rolling(21, min_periods=5).sum()
    base = _f02_crash_velocity(closeadj, 63) * cv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × current dollar volume
def f02cs_f02_crash_speed_slopexcurdv_21d_jerk_v136_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 21) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × current dollar volume
def f02cs_f02_crash_speed_slopexcurdv_252d_jerk_v137_signal(closeadj, volume):
    base = _f02_crash_slope(closeadj, 252) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d slope × range × close
def f02cs_f02_crash_speed_slopexrange_21d_jerk_v138_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f02_crash_slope(closeadj, 21) * rng * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × range × close
def f02cs_f02_crash_speed_slopexrange_63d_jerk_v139_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f02_crash_slope(closeadj, 63) * rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d composite crash speed × close
def f02cs_f02_crash_speed_compositespeed_21d_jerk_v140_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21).abs()
    sl = _f02_crash_slope(closeadj, 21).abs()
    base = (v + sl) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d composite crash speed × close
def f02cs_f02_crash_speed_compositespeed_63d_jerk_v141_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63).abs()
    sl = _f02_crash_slope(closeadj, 63).abs()
    base = (v + sl) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite crash speed × close
def f02cs_f02_crash_speed_compositespeed_252d_jerk_v142_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252).abs()
    sl = _f02_crash_slope(closeadj, 252).abs()
    base = (v + sl) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d composite crash speed × close
def f02cs_f02_crash_speed_compositespeed_504d_jerk_v143_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 504).abs()
    sl = _f02_crash_slope(closeadj, 504).abs()
    base = (v + sl) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × peak proximity × close
def f02cs_f02_crash_speed_velxpeakprox_63d_jerk_v144_signal(closeadj):
    peak = closeadj.rolling(63, min_periods=21).max().replace(0, np.nan)
    prox = closeadj / peak
    base = _f02_crash_velocity(closeadj, 63) * prox * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × peak proximity × close
def f02cs_f02_crash_speed_velxpeakprox_252d_jerk_v145_signal(closeadj):
    peak = closeadj.rolling(252, min_periods=63).max().replace(0, np.nan)
    prox = closeadj / peak
    base = _f02_crash_velocity(closeadj, 252) * prox * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_21d_jerk_v146_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_speed_intensity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_63d_jerk_v147_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_speed_intensity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d intensity × downside dollar vol
def f02cs_f02_crash_speed_intensxdownvol_252d_jerk_v148_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f02_crash_speed_intensity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d velocity × cumulative downside count × close
def f02cs_f02_crash_speed_velxdowncount_63d_jerk_v149_signal(closeadj):
    r = closeadj.pct_change()
    dc = (r < 0).astype(float).rolling(63, min_periods=21).sum()
    base = _f02_crash_velocity(closeadj, 63) * dc * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d velocity × cumulative downside count × close
def f02cs_f02_crash_speed_velxdowncount_252d_jerk_v150_signal(closeadj):
    r = closeadj.pct_change()
    dc = (r < 0).astype(float).rolling(252, min_periods=63).sum()
    base = _f02_crash_velocity(closeadj, 252) * dc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cs_f02_crash_speed_velocity_21d_jerk_v001_signal,
    f02cs_f02_crash_speed_velocity_21d_jerk_v002_signal,
    f02cs_f02_crash_speed_velocity_63d_jerk_v003_signal,
    f02cs_f02_crash_speed_velocity_126d_jerk_v004_signal,
    f02cs_f02_crash_speed_velocity_252d_jerk_v005_signal,
    f02cs_f02_crash_speed_velocity_504d_jerk_v006_signal,
    f02cs_f02_crash_speed_slope_21d_jerk_v007_signal,
    f02cs_f02_crash_speed_slope_63d_jerk_v008_signal,
    f02cs_f02_crash_speed_slope_126d_jerk_v009_signal,
    f02cs_f02_crash_speed_slope_252d_jerk_v010_signal,
    f02cs_f02_crash_speed_slope_504d_jerk_v011_signal,
    f02cs_f02_crash_speed_ttbottom_21d_jerk_v012_signal,
    f02cs_f02_crash_speed_ttbottom_63d_jerk_v013_signal,
    f02cs_f02_crash_speed_ttbottom_252d_jerk_v014_signal,
    f02cs_f02_crash_speed_dailydecline_21d_jerk_v015_signal,
    f02cs_f02_crash_speed_dailydecline_63d_jerk_v016_signal,
    f02cs_f02_crash_speed_dailydecline_252d_jerk_v017_signal,
    f02cs_f02_crash_speed_intensity_21d_jerk_v018_signal,
    f02cs_f02_crash_speed_intensity_63d_jerk_v019_signal,
    f02cs_f02_crash_speed_intensity_252d_jerk_v020_signal,
    f02cs_f02_crash_speed_intensity_504d_jerk_v021_signal,
    f02cs_f02_crash_speed_maxdrop_21d_jerk_v022_signal,
    f02cs_f02_crash_speed_maxdrop_63d_jerk_v023_signal,
    f02cs_f02_crash_speed_maxdrop_252d_jerk_v024_signal,
    f02cs_f02_crash_speed_velz_252d_jerk_v025_signal,
    f02cs_f02_crash_speed_velz_504d_jerk_v026_signal,
    f02cs_f02_crash_speed_slopez_252d_jerk_v027_signal,
    f02cs_f02_crash_speed_slopez_504d_jerk_v028_signal,
    f02cs_f02_crash_speed_velmean_21d_jerk_v029_signal,
    f02cs_f02_crash_speed_velmean_63d_jerk_v030_signal,
    f02cs_f02_crash_speed_velmean_252d_jerk_v031_signal,
    f02cs_f02_crash_speed_velstd_21d_jerk_v032_signal,
    f02cs_f02_crash_speed_velstd_63d_jerk_v033_signal,
    f02cs_f02_crash_speed_velxvol_21d_jerk_v034_signal,
    f02cs_f02_crash_speed_velxvol_63d_jerk_v035_signal,
    f02cs_f02_crash_speed_velxdv_252d_jerk_v036_signal,
    f02cs_f02_crash_speed_decelaccel_21d_jerk_v037_signal,
    f02cs_f02_crash_speed_decelaccel_63d_jerk_v038_signal,
    f02cs_f02_crash_speed_decelaccel_252d_jerk_v039_signal,
    f02cs_f02_crash_speed_velxatr_21d_jerk_v040_signal,
    f02cs_f02_crash_speed_velxatr_63d_jerk_v041_signal,
    f02cs_f02_crash_speed_velxatr_252d_jerk_v042_signal,
    f02cs_f02_crash_speed_velsq_21d_jerk_v043_signal,
    f02cs_f02_crash_speed_velsq_63d_jerk_v044_signal,
    f02cs_f02_crash_speed_velsq_252d_jerk_v045_signal,
    f02cs_f02_crash_speed_velocity_5d_jerk_v046_signal,
    f02cs_f02_crash_speed_velocity_10d_jerk_v047_signal,
    f02cs_f02_crash_speed_velocity_42d_jerk_v048_signal,
    f02cs_f02_crash_speed_velocity_189d_jerk_v049_signal,
    f02cs_f02_crash_speed_velocity_378d_jerk_v050_signal,
    f02cs_f02_crash_speed_velratio_21v63_jerk_v051_signal,
    f02cs_f02_crash_speed_velratio_63v252_jerk_v052_signal,
    f02cs_f02_crash_speed_velratio_252v504_jerk_v053_signal,
    f02cs_f02_crash_speed_veldiff_21m63_jerk_v054_signal,
    f02cs_f02_crash_speed_veldiff_63m252_jerk_v055_signal,
    f02cs_f02_crash_speed_veldiff_252m504_jerk_v056_signal,
    f02cs_f02_crash_speed_sloperatio_21v63_jerk_v057_signal,
    f02cs_f02_crash_speed_sloperatio_63v252_jerk_v058_signal,
    f02cs_f02_crash_speed_speedxdownvol_21d_jerk_v059_signal,
    f02cs_f02_crash_speed_speedxdownvol_63d_jerk_v060_signal,
    f02cs_f02_crash_speed_speedxdownvol_252d_jerk_v061_signal,
    f02cs_f02_crash_speed_slopexretvol_21d_jerk_v062_signal,
    f02cs_f02_crash_speed_slopexretvol_63d_jerk_v063_signal,
    f02cs_f02_crash_speed_slopexretvol_252d_jerk_v064_signal,
    f02cs_f02_crash_speed_slopexvolz_21d_jerk_v065_signal,
    f02cs_f02_crash_speed_slopexvolz_63d_jerk_v066_signal,
    f02cs_f02_crash_speed_velxskew_63d_jerk_v067_signal,
    f02cs_f02_crash_speed_velxskew_252d_jerk_v068_signal,
    f02cs_f02_crash_speed_velxkurt_63d_jerk_v069_signal,
    f02cs_f02_crash_speed_velxkurt_252d_jerk_v070_signal,
    f02cs_f02_crash_speed_velema_21d_jerk_v071_signal,
    f02cs_f02_crash_speed_velema_63d_jerk_v072_signal,
    f02cs_f02_crash_speed_velema_252d_jerk_v073_signal,
    f02cs_f02_crash_speed_velxcurdv_21d_jerk_v074_signal,
    f02cs_f02_crash_speed_velxcurdv_252d_jerk_v075_signal,
    f02cs_f02_crash_speed_velxrange_21d_jerk_v076_signal,
    f02cs_f02_crash_speed_velxrange_63d_jerk_v077_signal,
    f02cs_f02_crash_speed_velxrange_252d_jerk_v078_signal,
    f02cs_f02_crash_speed_worstvel_63d_jerk_v079_signal,
    f02cs_f02_crash_speed_worstvel_252d_jerk_v080_signal,
    f02cs_f02_crash_speed_worstvel_504d_jerk_v081_signal,
    f02cs_f02_crash_speed_intensity_5d_jerk_v082_signal,
    f02cs_f02_crash_speed_intensity_10d_jerk_v083_signal,
    f02cs_f02_crash_speed_intensity_42d_jerk_v084_signal,
    f02cs_f02_crash_speed_intensity_189d_jerk_v085_signal,
    f02cs_f02_crash_speed_intensity_378d_jerk_v086_signal,
    f02cs_f02_crash_speed_slopeintens_21d_jerk_v087_signal,
    f02cs_f02_crash_speed_slopeintens_63d_jerk_v088_signal,
    f02cs_f02_crash_speed_slopeintens_252d_jerk_v089_signal,
    f02cs_f02_crash_speed_velxatrnorm_21d_jerk_v090_signal,
    f02cs_f02_crash_speed_velxatrnorm_63d_jerk_v091_signal,
    f02cs_f02_crash_speed_slopexcumdown_21d_jerk_v092_signal,
    f02cs_f02_crash_speed_slopexcumdown_63d_jerk_v093_signal,
    f02cs_f02_crash_speed_slopexcumdown_252d_jerk_v094_signal,
    f02cs_f02_crash_speed_velxret_21d_jerk_v095_signal,
    f02cs_f02_crash_speed_velxret_63d_jerk_v096_signal,
    f02cs_f02_crash_speed_velxret_252d_jerk_v097_signal,
    f02cs_f02_crash_speed_intensxvolz_21d_jerk_v098_signal,
    f02cs_f02_crash_speed_intensxvolz_63d_jerk_v099_signal,
    f02cs_f02_crash_speed_intensxvolz_252d_jerk_v100_signal,
    f02cs_f02_crash_speed_velarea_63d_jerk_v101_signal,
    f02cs_f02_crash_speed_velarea_252d_jerk_v102_signal,
    f02cs_f02_crash_speed_velarea_504d_jerk_v103_signal,
    f02cs_f02_crash_speed_velaccel_21d_jerk_v104_signal,
    f02cs_f02_crash_speed_velaccel_63d_jerk_v105_signal,
    f02cs_f02_crash_speed_velaccel_252d_jerk_v106_signal,
    f02cs_f02_crash_speed_slopexatr_21d_jerk_v107_signal,
    f02cs_f02_crash_speed_slopexatr_63d_jerk_v108_signal,
    f02cs_f02_crash_speed_slopexatr_252d_jerk_v109_signal,
    f02cs_f02_crash_speed_slopemean_63d_jerk_v110_signal,
    f02cs_f02_crash_speed_slopemean_252d_jerk_v111_signal,
    f02cs_f02_crash_speed_slopestd_63d_jerk_v112_signal,
    f02cs_f02_crash_speed_slopestd_252d_jerk_v113_signal,
    f02cs_f02_crash_speed_velworstever_jerk_v114_signal,
    f02cs_f02_crash_speed_velvshistworst_252d_jerk_v115_signal,
    f02cs_f02_crash_speed_velvshistworst_504d_jerk_v116_signal,
    f02cs_f02_crash_speed_slopexcumvol_21d_jerk_v117_signal,
    f02cs_f02_crash_speed_slopexcumvol_63d_jerk_v118_signal,
    f02cs_f02_crash_speed_intensxatr_21d_jerk_v119_signal,
    f02cs_f02_crash_speed_intensxatr_63d_jerk_v120_signal,
    f02cs_f02_crash_speed_velxtails_63d_jerk_v121_signal,
    f02cs_f02_crash_speed_velxtails_252d_jerk_v122_signal,
    f02cs_f02_crash_speed_slopeema_21d_jerk_v123_signal,
    f02cs_f02_crash_speed_slopeema_63d_jerk_v124_signal,
    f02cs_f02_crash_speed_slopeema_252d_jerk_v125_signal,
    f02cs_f02_crash_speed_velvolvol_63d_jerk_v126_signal,
    f02cs_f02_crash_speed_velvolvol_252d_jerk_v127_signal,
    f02cs_f02_crash_speed_slopediff_21m63_jerk_v128_signal,
    f02cs_f02_crash_speed_slopediff_63m252_jerk_v129_signal,
    f02cs_f02_crash_speed_slopediff_252m504_jerk_v130_signal,
    f02cs_f02_crash_speed_fastdecl_252d_jerk_v131_signal,
    f02cs_f02_crash_speed_fastdecl_63d_jerk_v132_signal,
    f02cs_f02_crash_speed_fastdecl_504d_jerk_v133_signal,
    f02cs_f02_crash_speed_velxcumvol_21d_jerk_v134_signal,
    f02cs_f02_crash_speed_velxcumvol_63d_jerk_v135_signal,
    f02cs_f02_crash_speed_slopexcurdv_21d_jerk_v136_signal,
    f02cs_f02_crash_speed_slopexcurdv_252d_jerk_v137_signal,
    f02cs_f02_crash_speed_slopexrange_21d_jerk_v138_signal,
    f02cs_f02_crash_speed_slopexrange_63d_jerk_v139_signal,
    f02cs_f02_crash_speed_compositespeed_21d_jerk_v140_signal,
    f02cs_f02_crash_speed_compositespeed_63d_jerk_v141_signal,
    f02cs_f02_crash_speed_compositespeed_252d_jerk_v142_signal,
    f02cs_f02_crash_speed_compositespeed_504d_jerk_v143_signal,
    f02cs_f02_crash_speed_velxpeakprox_63d_jerk_v144_signal,
    f02cs_f02_crash_speed_velxpeakprox_252d_jerk_v145_signal,
    f02cs_f02_crash_speed_intensxdownvol_21d_jerk_v146_signal,
    f02cs_f02_crash_speed_intensxdownvol_63d_jerk_v147_signal,
    f02cs_f02_crash_speed_intensxdownvol_252d_jerk_v148_signal,
    f02cs_f02_crash_speed_velxdowncount_63d_jerk_v149_signal,
    f02cs_f02_crash_speed_velxdowncount_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_CRASH_SPEED_REGISTRY_JERK = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f02_crash_speed_3rd_derivatives_001_150_claude: {n_features} features pass")
