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


# 21d crash velocity (peak-to-trough drop / window)
def f02cs_f02_crash_speed_velocity_21d_base_v001_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity
def f02cs_f02_crash_speed_velocity_63d_base_v002_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d crash velocity
def f02cs_f02_crash_speed_velocity_126d_base_v003_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity
def f02cs_f02_crash_speed_velocity_252d_base_v004_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash velocity
def f02cs_f02_crash_speed_velocity_504d_base_v005_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash slope (drawdown / window)
def f02cs_f02_crash_speed_slope_21d_base_v006_signal(closeadj):
    result = _f02_crash_slope(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash slope
def f02cs_f02_crash_speed_slope_63d_base_v007_signal(closeadj):
    result = _f02_crash_slope(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d crash slope
def f02cs_f02_crash_speed_slope_126d_base_v008_signal(closeadj):
    result = _f02_crash_slope(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash slope
def f02cs_f02_crash_speed_slope_252d_base_v009_signal(closeadj):
    result = _f02_crash_slope(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash slope
def f02cs_f02_crash_speed_slope_504d_base_v010_signal(closeadj):
    result = _f02_crash_slope(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d time-to-bottom (days from peak to trough)
def f02cs_f02_crash_speed_ttbottom_21d_base_v011_signal(closeadj):
    peak_idx = closeadj.rolling(21, min_periods=5).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(21, min_periods=5).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    result = ttb * closeadj * _f02_crash_velocity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d time-to-bottom
def f02cs_f02_crash_speed_ttbottom_63d_base_v012_signal(closeadj):
    peak_idx = closeadj.rolling(63, min_periods=21).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(63, min_periods=21).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    result = ttb * closeadj * _f02_crash_velocity(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d time-to-bottom
def f02cs_f02_crash_speed_ttbottom_252d_base_v013_signal(closeadj):
    peak_idx = closeadj.rolling(252, min_periods=63).apply(lambda x: float(np.argmax(x)), raw=True)
    trough_idx = closeadj.rolling(252, min_periods=63).apply(lambda x: float(np.argmin(x)), raw=True)
    ttb = (trough_idx - peak_idx).clip(lower=0)
    result = ttb * closeadj * _f02_crash_velocity(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d daily decline rate (avg negative return)
def f02cs_f02_crash_speed_dailydecline_21d_base_v014_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = neg.rolling(21, min_periods=5).mean() * closeadj + _f02_crash_velocity(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d daily decline rate
def f02cs_f02_crash_speed_dailydecline_63d_base_v015_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = neg.rolling(63, min_periods=21).mean() * closeadj + _f02_crash_velocity(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d daily decline rate
def f02cs_f02_crash_speed_dailydecline_252d_base_v016_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = neg.rolling(252, min_periods=63).mean() * closeadj + _f02_crash_velocity(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash speed intensity
def f02cs_f02_crash_speed_intensity_21d_base_v017_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash speed intensity
def f02cs_f02_crash_speed_intensity_63d_base_v018_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed intensity
def f02cs_f02_crash_speed_intensity_252d_base_v019_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash speed intensity
def f02cs_f02_crash_speed_intensity_504d_base_v020_signal(closeadj):
    result = _f02_crash_speed_intensity(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max single-day drop scaled by velocity
def f02cs_f02_crash_speed_maxdrop_21d_base_v021_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(21, min_periods=5).min()
    result = md * closeadj + _f02_crash_velocity(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max single-day drop scaled by velocity
def f02cs_f02_crash_speed_maxdrop_63d_base_v022_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(63, min_periods=21).min()
    result = md * closeadj + _f02_crash_velocity(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max single-day drop
def f02cs_f02_crash_speed_maxdrop_252d_base_v023_signal(closeadj):
    r = closeadj.pct_change()
    md = r.rolling(252, min_periods=63).min()
    result = md * closeadj + _f02_crash_velocity(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity zscore over 252d
def f02cs_f02_crash_speed_velz_252d_base_v024_signal(closeadj):
    result = _z(_f02_crash_velocity(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity zscore over 504d
def f02cs_f02_crash_speed_velz_504d_base_v025_signal(closeadj):
    result = _z(_f02_crash_velocity(closeadj, 63), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash slope zscore over 252d
def f02cs_f02_crash_speed_slopez_252d_base_v026_signal(closeadj):
    result = _z(_f02_crash_slope(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash slope zscore over 504d
def f02cs_f02_crash_speed_slopez_504d_base_v027_signal(closeadj):
    result = _z(_f02_crash_slope(closeadj, 63), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of velocity over 21d
def f02cs_f02_crash_speed_velmean_21d_base_v028_signal(closeadj):
    result = _mean(_f02_crash_velocity(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of velocity
def f02cs_f02_crash_speed_velmean_63d_base_v029_signal(closeadj):
    result = _mean(_f02_crash_velocity(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of velocity
def f02cs_f02_crash_speed_velmean_252d_base_v030_signal(closeadj):
    result = _mean(_f02_crash_velocity(closeadj, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling std of velocity
def f02cs_f02_crash_speed_velstd_21d_base_v031_signal(closeadj):
    result = _std(_f02_crash_velocity(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of velocity
def f02cs_f02_crash_speed_velstd_63d_base_v032_signal(closeadj):
    result = _std(_f02_crash_velocity(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × volume (capitulation pace)
def f02cs_f02_crash_speed_velxvol_21d_base_v033_signal(closeadj, volume):
    result = _f02_crash_velocity(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity × volume
def f02cs_f02_crash_speed_velxvol_63d_base_v034_signal(closeadj, volume):
    result = _f02_crash_velocity(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity × dollar volume
def f02cs_f02_crash_speed_velxdv_252d_base_v035_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f02_crash_velocity(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of decline (slope diff over 5d)
def f02cs_f02_crash_speed_decelaccel_21d_base_v036_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 21)
    result = (sl - sl.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of decline
def f02cs_f02_crash_speed_decelaccel_63d_base_v037_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 63)
    result = (sl - sl.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of decline
def f02cs_f02_crash_speed_decelaccel_252d_base_v038_signal(closeadj):
    sl = _f02_crash_slope(closeadj, 252)
    result = (sl - sl.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity × ATR
def f02cs_f02_crash_speed_velxatr_21d_base_v039_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_velocity(closeadj, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity × ATR
def f02cs_f02_crash_speed_velxatr_63d_base_v040_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_velocity(closeadj, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity × ATR
def f02cs_f02_crash_speed_velxatr_252d_base_v041_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f02_crash_velocity(closeadj, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity squared (severity emphasis)
def f02cs_f02_crash_speed_velsq_21d_base_v042_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    result = v * v.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity squared
def f02cs_f02_crash_speed_velsq_63d_base_v043_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    result = v * v.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity squared
def f02cs_f02_crash_speed_velsq_252d_base_v044_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    result = v * v.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d crash velocity (intraweek crash speed)
def f02cs_f02_crash_speed_velocity_5d_base_v045_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d crash velocity
def f02cs_f02_crash_speed_velocity_10d_base_v046_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d crash velocity
def f02cs_f02_crash_speed_velocity_42d_base_v047_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d crash velocity
def f02cs_f02_crash_speed_velocity_189d_base_v048_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d crash velocity
def f02cs_f02_crash_speed_velocity_378d_base_v049_signal(closeadj):
    result = _f02_crash_velocity(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity ratio: 21d / 63d (recent vs deeper)
def f02cs_f02_crash_speed_velratio_21v63_base_v050_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 21)
    b = _f02_crash_velocity(closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity ratio: 63d / 252d
def f02cs_f02_crash_speed_velratio_63v252_base_v051_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 63)
    b = _f02_crash_velocity(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity ratio: 252d / 504d
def f02cs_f02_crash_speed_velratio_252v504_base_v052_signal(closeadj):
    a = _f02_crash_velocity(closeadj, 252)
    b = _f02_crash_velocity(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash velocity diff: 21d - 63d
def f02cs_f02_crash_speed_veldiff_21m63_base_v053_signal(closeadj):
    result = (_f02_crash_velocity(closeadj, 21) - _f02_crash_velocity(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash velocity diff: 63d - 252d
def f02cs_f02_crash_speed_veldiff_63m252_base_v054_signal(closeadj):
    result = (_f02_crash_velocity(closeadj, 63) - _f02_crash_velocity(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash velocity diff: 252d - 504d
def f02cs_f02_crash_speed_veldiff_252m504_base_v055_signal(closeadj):
    result = (_f02_crash_velocity(closeadj, 252) - _f02_crash_velocity(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope ratio: 21d / 63d
def f02cs_f02_crash_speed_sloperatio_21v63_base_v056_signal(closeadj):
    a = _f02_crash_slope(closeadj, 21)
    b = _f02_crash_slope(closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope ratio: 63d / 252d
def f02cs_f02_crash_speed_sloperatio_63v252_base_v057_signal(closeadj):
    a = _f02_crash_slope(closeadj, 63)
    b = _f02_crash_slope(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash speed × downside dollar volume
def f02cs_f02_crash_speed_speedxdownvol_21d_base_v058_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_velocity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash speed × downside dollar volume
def f02cs_f02_crash_speed_speedxdownvol_63d_base_v059_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_velocity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed × downside dollar volume
def f02cs_f02_crash_speed_speedxdownvol_252d_base_v060_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f02_crash_velocity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × current return-volatility
def f02cs_f02_crash_speed_slopexretvol_21d_base_v061_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f02_crash_slope(closeadj, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × return-volatility
def f02cs_f02_crash_speed_slopexretvol_63d_base_v062_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f02_crash_slope(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × return-volatility
def f02cs_f02_crash_speed_slopexretvol_252d_base_v063_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f02_crash_slope(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × volume z (panic-pace)
def f02cs_f02_crash_speed_slopexvolz_21d_base_v064_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × volume z
def f02cs_f02_crash_speed_slopexvolz_63d_base_v065_signal(closeadj, volume):
    result = _f02_crash_slope(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash speed weighted by skew
def f02cs_f02_crash_speed_velxskew_63d_base_v066_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f02_crash_velocity(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed weighted by skew
def f02cs_f02_crash_speed_velxskew_252d_base_v067_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f02_crash_velocity(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash speed × kurt
def f02cs_f02_crash_speed_velxkurt_63d_base_v068_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f02_crash_velocity(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed × kurt
def f02cs_f02_crash_speed_velxkurt_252d_base_v069_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f02_crash_velocity(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of crash velocity × close
def f02cs_f02_crash_speed_velema_21d_base_v070_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 21)
    result = v.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of crash velocity × close
def f02cs_f02_crash_speed_velema_63d_base_v071_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 63)
    result = v.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of crash velocity × close
def f02cs_f02_crash_speed_velema_252d_base_v072_signal(closeadj):
    v = _f02_crash_velocity(closeadj, 252)
    result = v.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash speed × current dollar volume
def f02cs_f02_crash_speed_velxcurdv_21d_base_v073_signal(closeadj, volume):
    result = _f02_crash_velocity(closeadj, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash speed × current dollar volume
def f02cs_f02_crash_speed_velxcurdv_252d_base_v074_signal(closeadj, volume):
    result = _f02_crash_velocity(closeadj, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash speed × range (volatile-fast crash)
def f02cs_f02_crash_speed_velxrange_21d_base_v075_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f02_crash_velocity(closeadj, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cs_f02_crash_speed_velocity_21d_base_v001_signal,
    f02cs_f02_crash_speed_velocity_63d_base_v002_signal,
    f02cs_f02_crash_speed_velocity_126d_base_v003_signal,
    f02cs_f02_crash_speed_velocity_252d_base_v004_signal,
    f02cs_f02_crash_speed_velocity_504d_base_v005_signal,
    f02cs_f02_crash_speed_slope_21d_base_v006_signal,
    f02cs_f02_crash_speed_slope_63d_base_v007_signal,
    f02cs_f02_crash_speed_slope_126d_base_v008_signal,
    f02cs_f02_crash_speed_slope_252d_base_v009_signal,
    f02cs_f02_crash_speed_slope_504d_base_v010_signal,
    f02cs_f02_crash_speed_ttbottom_21d_base_v011_signal,
    f02cs_f02_crash_speed_ttbottom_63d_base_v012_signal,
    f02cs_f02_crash_speed_ttbottom_252d_base_v013_signal,
    f02cs_f02_crash_speed_dailydecline_21d_base_v014_signal,
    f02cs_f02_crash_speed_dailydecline_63d_base_v015_signal,
    f02cs_f02_crash_speed_dailydecline_252d_base_v016_signal,
    f02cs_f02_crash_speed_intensity_21d_base_v017_signal,
    f02cs_f02_crash_speed_intensity_63d_base_v018_signal,
    f02cs_f02_crash_speed_intensity_252d_base_v019_signal,
    f02cs_f02_crash_speed_intensity_504d_base_v020_signal,
    f02cs_f02_crash_speed_maxdrop_21d_base_v021_signal,
    f02cs_f02_crash_speed_maxdrop_63d_base_v022_signal,
    f02cs_f02_crash_speed_maxdrop_252d_base_v023_signal,
    f02cs_f02_crash_speed_velz_252d_base_v024_signal,
    f02cs_f02_crash_speed_velz_504d_base_v025_signal,
    f02cs_f02_crash_speed_slopez_252d_base_v026_signal,
    f02cs_f02_crash_speed_slopez_504d_base_v027_signal,
    f02cs_f02_crash_speed_velmean_21d_base_v028_signal,
    f02cs_f02_crash_speed_velmean_63d_base_v029_signal,
    f02cs_f02_crash_speed_velmean_252d_base_v030_signal,
    f02cs_f02_crash_speed_velstd_21d_base_v031_signal,
    f02cs_f02_crash_speed_velstd_63d_base_v032_signal,
    f02cs_f02_crash_speed_velxvol_21d_base_v033_signal,
    f02cs_f02_crash_speed_velxvol_63d_base_v034_signal,
    f02cs_f02_crash_speed_velxdv_252d_base_v035_signal,
    f02cs_f02_crash_speed_decelaccel_21d_base_v036_signal,
    f02cs_f02_crash_speed_decelaccel_63d_base_v037_signal,
    f02cs_f02_crash_speed_decelaccel_252d_base_v038_signal,
    f02cs_f02_crash_speed_velxatr_21d_base_v039_signal,
    f02cs_f02_crash_speed_velxatr_63d_base_v040_signal,
    f02cs_f02_crash_speed_velxatr_252d_base_v041_signal,
    f02cs_f02_crash_speed_velsq_21d_base_v042_signal,
    f02cs_f02_crash_speed_velsq_63d_base_v043_signal,
    f02cs_f02_crash_speed_velsq_252d_base_v044_signal,
    f02cs_f02_crash_speed_velocity_5d_base_v045_signal,
    f02cs_f02_crash_speed_velocity_10d_base_v046_signal,
    f02cs_f02_crash_speed_velocity_42d_base_v047_signal,
    f02cs_f02_crash_speed_velocity_189d_base_v048_signal,
    f02cs_f02_crash_speed_velocity_378d_base_v049_signal,
    f02cs_f02_crash_speed_velratio_21v63_base_v050_signal,
    f02cs_f02_crash_speed_velratio_63v252_base_v051_signal,
    f02cs_f02_crash_speed_velratio_252v504_base_v052_signal,
    f02cs_f02_crash_speed_veldiff_21m63_base_v053_signal,
    f02cs_f02_crash_speed_veldiff_63m252_base_v054_signal,
    f02cs_f02_crash_speed_veldiff_252m504_base_v055_signal,
    f02cs_f02_crash_speed_sloperatio_21v63_base_v056_signal,
    f02cs_f02_crash_speed_sloperatio_63v252_base_v057_signal,
    f02cs_f02_crash_speed_speedxdownvol_21d_base_v058_signal,
    f02cs_f02_crash_speed_speedxdownvol_63d_base_v059_signal,
    f02cs_f02_crash_speed_speedxdownvol_252d_base_v060_signal,
    f02cs_f02_crash_speed_slopexretvol_21d_base_v061_signal,
    f02cs_f02_crash_speed_slopexretvol_63d_base_v062_signal,
    f02cs_f02_crash_speed_slopexretvol_252d_base_v063_signal,
    f02cs_f02_crash_speed_slopexvolz_21d_base_v064_signal,
    f02cs_f02_crash_speed_slopexvolz_63d_base_v065_signal,
    f02cs_f02_crash_speed_velxskew_63d_base_v066_signal,
    f02cs_f02_crash_speed_velxskew_252d_base_v067_signal,
    f02cs_f02_crash_speed_velxkurt_63d_base_v068_signal,
    f02cs_f02_crash_speed_velxkurt_252d_base_v069_signal,
    f02cs_f02_crash_speed_velema_21d_base_v070_signal,
    f02cs_f02_crash_speed_velema_63d_base_v071_signal,
    f02cs_f02_crash_speed_velema_252d_base_v072_signal,
    f02cs_f02_crash_speed_velxcurdv_21d_base_v073_signal,
    f02cs_f02_crash_speed_velxcurdv_252d_base_v074_signal,
    f02cs_f02_crash_speed_velxrange_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_CRASH_SPEED_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f02_crash_speed_base_001_075_claude: {n_features} features pass")
