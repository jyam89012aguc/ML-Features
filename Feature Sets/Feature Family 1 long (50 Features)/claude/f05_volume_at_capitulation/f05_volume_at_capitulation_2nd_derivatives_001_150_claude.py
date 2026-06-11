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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f05_capitulation_volz(close, volume, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    depth = (close - peak) / peak.replace(0, np.nan).abs()
    vz = _z(volume, w)
    return vz * depth.abs()


def _f05_panic_volume(close, volume, w):
    r = close.pct_change()
    down = (r < 0).astype(float)
    return (volume * down).rolling(w, min_periods=max(1, w // 2)).sum() / volume.rolling(w, min_periods=max(1, w // 2)).sum().replace(0, np.nan)


def _f05_capitulation_climax(close, volume, w):
    rmin = close.rolling(w, min_periods=max(1, w // 2)).min()
    proximity = rmin / close.replace(0, np.nan).abs()
    vz = _z(volume, w)
    return vz * proximity * (close - rmin) / rmin.replace(0, np.nan).abs()


# 5d slope of 21d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_21d_slope_v001_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_21d_slope_v002_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v003_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v004_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v005_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_126d_slope_v006_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_126d_slope_v007_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_252d_slope_v008_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_252d_slope_v009_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_504d_slope_v010_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_504d_slope_v011_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_5d_slope_v012_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_10d_slope_v013_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_42d_slope_v014_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_189d_slope_v015_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d capvolz
def f05vc_f05_volume_at_capitulation_capvolz_378d_slope_v016_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz squared
def f05vc_f05_volume_at_capitulation_capvolzsq_21d_slope_v017_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    base = cv * cv.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz squared
def f05vc_f05_volume_at_capitulation_capvolzsq_63d_slope_v018_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv * cv.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz squared
def f05vc_f05_volume_at_capitulation_capvolzsq_252d_slope_v019_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = cv * cv.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz EMA
def f05vc_f05_volume_at_capitulation_capvolzema_21d_slope_v020_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    base = cv.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz EMA
def f05vc_f05_volume_at_capitulation_capvolzema_63d_slope_v021_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz EMA
def f05vc_f05_volume_at_capitulation_capvolzema_252d_slope_v022_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = cv.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz sum
def f05vc_f05_volume_at_capitulation_capvolzsum_21d_slope_v023_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv.rolling(21, min_periods=5).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz sum
def f05vc_f05_volume_at_capitulation_capvolzsum_63d_slope_v024_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz sum
def f05vc_f05_volume_at_capitulation_capvolzsum_252d_slope_v025_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = cv.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz max
def f05vc_f05_volume_at_capitulation_capvolzmax_63d_slope_v026_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv.rolling(21, min_periods=5).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz max
def f05vc_f05_volume_at_capitulation_capvolzmax_252d_slope_v027_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = cv.rolling(63, min_periods=21).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_21d_slope_v028_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_21d_slope_v029_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_63d_slope_v030_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_63d_slope_v031_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_252d_slope_v032_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_504d_slope_v033_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_5d_slope_v034_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_10d_slope_v035_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d panic vol
def f05vc_f05_volume_at_capitulation_panicvolfrac_126d_slope_v036_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol × rv
def f05vc_f05_volume_at_capitulation_panicvolxrv_21d_slope_v037_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    base = _f05_panic_volume(closeadj, volume, 21) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol × rv
def f05vc_f05_volume_at_capitulation_panicvolxrv_63d_slope_v038_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f05_panic_volume(closeadj, volume, 63) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol × rv
def f05vc_f05_volume_at_capitulation_panicvolxrv_252d_slope_v039_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f05_panic_volume(closeadj, volume, 252) * rv * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol z
def f05vc_f05_volume_at_capitulation_panicvolz_21d_slope_v040_signal(closeadj, volume):
    base = _z(_f05_panic_volume(closeadj, volume, 21), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol z
def f05vc_f05_volume_at_capitulation_panicvolz_63d_slope_v041_signal(closeadj, volume):
    base = _z(_f05_panic_volume(closeadj, volume, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol z
def f05vc_f05_volume_at_capitulation_panicvolz_252d_slope_v042_signal(closeadj, volume):
    base = _z(_f05_panic_volume(closeadj, volume, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d climax
def f05vc_f05_volume_at_capitulation_climax_21d_slope_v043_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax
def f05vc_f05_volume_at_capitulation_climax_63d_slope_v044_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d climax
def f05vc_f05_volume_at_capitulation_climax_126d_slope_v045_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d climax
def f05vc_f05_volume_at_capitulation_climax_252d_slope_v046_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d climax
def f05vc_f05_volume_at_capitulation_climax_504d_slope_v047_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_21d_slope_v048_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_climax(closeadj, volume, 21) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_63d_slope_v049_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_climax(closeadj, volume, 63) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_252d_slope_v050_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_climax(closeadj, volume, 252) * dv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax EMA
def f05vc_f05_volume_at_capitulation_climaxema_21d_slope_v051_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    base = cl.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax EMA
def f05vc_f05_volume_at_capitulation_climaxema_63d_slope_v052_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    base = cl.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d climax EMA
def f05vc_f05_volume_at_capitulation_climaxema_252d_slope_v053_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 252)
    base = cl.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capitulation event mean × close
def f05vc_f05_volume_at_capitulation_capeventcount_252d_slope_v054_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = cv.rolling(252, min_periods=63).mean() * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d cap event count
def f05vc_f05_volume_at_capitulation_capeventcount_504d_slope_v055_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = (cv).rolling(504, min_periods=126).mean() * (1.0 + closeadj * 0.001)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d panic event count
def f05vc_f05_volume_at_capitulation_paniceventcount_252d_slope_v056_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = (pv).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic event count 70
def f05vc_f05_volume_at_capitulation_paniceventcount_70_slope_v057_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = (pv).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzxdv_21d_slope_v058_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_volz(closeadj, volume, 21) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × dv
def f05vc_f05_volume_at_capitulation_capvolzxdv_63d_slope_v059_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_volz(closeadj, volume, 63) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × dv
def f05vc_f05_volume_at_capitulation_capvolzxdv_252d_slope_v060_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_capitulation_volz(closeadj, volume, 252) * dv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × ret
def f05vc_f05_volume_at_capitulation_capvolzxret_21d_slope_v061_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    base = _f05_capitulation_volz(closeadj, volume, 21) * r21 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × ret
def f05vc_f05_volume_at_capitulation_capvolzxret_63d_slope_v062_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    base = _f05_capitulation_volz(closeadj, volume, 63) * r63 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × ret
def f05vc_f05_volume_at_capitulation_capvolzxret_252d_slope_v063_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    base = _f05_capitulation_volz(closeadj, volume, 252) * r252 * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol × dollar volume
def f05vc_f05_volume_at_capitulation_panicvolxdv_21d_slope_v064_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_panic_volume(closeadj, volume, 21) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol × dv
def f05vc_f05_volume_at_capitulation_panicvolxdv_63d_slope_v065_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f05_panic_volume(closeadj, volume, 63) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol × ret
def f05vc_f05_volume_at_capitulation_panicvolxret_21d_slope_v066_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    base = _f05_panic_volume(closeadj, volume, 21) * r21 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol × ret
def f05vc_f05_volume_at_capitulation_panicvolxret_63d_slope_v067_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    base = _f05_panic_volume(closeadj, volume, 63) * r63 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol × ret
def f05vc_f05_volume_at_capitulation_panicvolxret_252d_slope_v068_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    base = _f05_panic_volume(closeadj, volume, 252) * r252 * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capvolz diff (21-63)
def f05vc_f05_volume_at_capitulation_capvolzdiff_21m63_slope_v069_signal(closeadj, volume):
    base = (_f05_capitulation_volz(closeadj, volume, 21) - _f05_capitulation_volz(closeadj, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capvolz diff (63-252)
def f05vc_f05_volume_at_capitulation_capvolzdiff_63m252_slope_v070_signal(closeadj, volume):
    base = (_f05_capitulation_volz(closeadj, volume, 63) - _f05_capitulation_volz(closeadj, volume, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capvolz ratio (21v252)
def f05vc_f05_volume_at_capitulation_capvolzratio_21v252_slope_v071_signal(closeadj, volume):
    a = _f05_capitulation_volz(closeadj, volume, 21)
    b = _f05_capitulation_volz(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capvolz ratio (63v252)
def f05vc_f05_volume_at_capitulation_capvolzratio_63v252_slope_v072_signal(closeadj, volume):
    a = _f05_capitulation_volz(closeadj, volume, 63)
    b = _f05_capitulation_volz(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × ATR
def f05vc_f05_volume_at_capitulation_capvolzxatr_21d_slope_v073_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × ATR
def f05vc_f05_volume_at_capitulation_capvolzxatr_63d_slope_v074_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × ATR
def f05vc_f05_volume_at_capitulation_capvolzxatr_252d_slope_v075_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_capitulation_volz(closeadj, volume, 252) * atr
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × panic
def f05vc_f05_volume_at_capitulation_capvolzxpanic_21d_slope_v076_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * _f05_panic_volume(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × panic
def f05vc_f05_volume_at_capitulation_capvolzxpanic_63d_slope_v077_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * _f05_panic_volume(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × panic
def f05vc_f05_volume_at_capitulation_capvolzxpanic_252d_slope_v078_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 252) * _f05_panic_volume(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax × panic
def f05vc_f05_volume_at_capitulation_climaxxpanic_21d_slope_v079_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 21) * _f05_panic_volume(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax × panic
def f05vc_f05_volume_at_capitulation_climaxxpanic_63d_slope_v080_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 63) * _f05_panic_volume(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite cap
def f05vc_f05_volume_at_capitulation_capcomposite_252d_slope_v081_signal(closeadj, volume):
    base = (_f05_capitulation_volz(closeadj, volume, 252) + _f05_capitulation_climax(closeadj, volume, 252) + _f05_panic_volume(closeadj, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d composite cap
def f05vc_f05_volume_at_capitulation_capcomposite_21d_slope_v082_signal(closeadj, volume):
    base = (_f05_capitulation_volz(closeadj, volume, 21) + _f05_capitulation_climax(closeadj, volume, 21) + _f05_panic_volume(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × hl-range
def f05vc_f05_volume_at_capitulation_capvolzxhlrange_21d_slope_v083_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 21) * rng * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × rv
def f05vc_f05_volume_at_capitulation_capvolzxrv_21d_slope_v084_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    base = _f05_capitulation_volz(closeadj, volume, 21) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × rv
def f05vc_f05_volume_at_capitulation_capvolzxrv_63d_slope_v085_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f05_capitulation_volz(closeadj, volume, 63) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × rv
def f05vc_f05_volume_at_capitulation_capvolzxrv_252d_slope_v086_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f05_capitulation_volz(closeadj, volume, 252) * rv * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × skew
def f05vc_f05_volume_at_capitulation_capvolzxskew_63d_slope_v087_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f05_capitulation_volz(closeadj, volume, 21) * sk * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capvolz × kurt
def f05vc_f05_volume_at_capitulation_capvolzxkurt_252d_slope_v088_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f05_capitulation_volz(closeadj, volume, 63) * kt * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol × skew
def f05vc_f05_volume_at_capitulation_panicvolxskew_63d_slope_v089_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f05_panic_volume(closeadj, volume, 21) * sk * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol × kurt
def f05vc_f05_volume_at_capitulation_panicvolxkurt_252d_slope_v090_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f05_panic_volume(closeadj, volume, 252) * kt * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz EMA × dv
def f05vc_f05_volume_at_capitulation_capvolzemaxdv_21d_slope_v091_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    e = cv.ewm(span=21, adjust=False).mean()
    base = e * closeadj * volume
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz EMA × dv
def f05vc_f05_volume_at_capitulation_capvolzemaxdv_63d_slope_v092_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    e = cv.ewm(span=63, adjust=False).mean()
    base = e * closeadj * volume
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz / rv
def f05vc_f05_volume_at_capitulation_capvolzdivrv_21d_slope_v093_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = (_f05_capitulation_volz(closeadj, volume, 21) / rv) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz / rv
def f05vc_f05_volume_at_capitulation_capvolzdivrv_63d_slope_v094_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f05_capitulation_volz(closeadj, volume, 63) / rv) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz / rv
def f05vc_f05_volume_at_capitulation_capvolzdivrv_252d_slope_v095_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f05_capitulation_volz(closeadj, volume, 252) / rv) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × log
def f05vc_f05_volume_at_capitulation_capvolzxlog_21d_slope_v096_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f05_capitulation_volz(closeadj, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × log
def f05vc_f05_volume_at_capitulation_capvolzxlog_63d_slope_v097_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f05_capitulation_volz(closeadj, volume, 63) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic × log
def f05vc_f05_volume_at_capitulation_panicvolxlog_21d_slope_v098_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f05_panic_volume(closeadj, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax × log
def f05vc_f05_volume_at_capitulation_climaxxlog_21d_slope_v099_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f05_capitulation_climax(closeadj, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × volz
def f05vc_f05_volume_at_capitulation_capvolzxvolz_21d_slope_v100_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × volz
def f05vc_f05_volume_at_capitulation_capvolzxvolz_63d_slope_v101_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × volz
def f05vc_f05_volume_at_capitulation_capvolzxvolz_252d_slope_v102_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 252) * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax × volz
def f05vc_f05_volume_at_capitulation_climaxxvolz_21d_slope_v103_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax × volz
def f05vc_f05_volume_at_capitulation_climaxxvolz_63d_slope_v104_signal(closeadj, volume):
    base = _f05_capitulation_climax(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic × volz
def f05vc_f05_volume_at_capitulation_panicvolxvolz_21d_slope_v105_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic × volz
def f05vc_f05_volume_at_capitulation_panicvolxvolz_63d_slope_v106_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × range
def f05vc_f05_volume_at_capitulation_capvolzxrange_21d_slope_v107_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 21) * rng
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × range
def f05vc_f05_volume_at_capitulation_capvolzxrange_63d_slope_v108_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 63) * rng
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic × ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_21d_slope_v109_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_panic_volume(closeadj, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic × ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_63d_slope_v110_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_panic_volume(closeadj, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic × ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_252d_slope_v111_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_panic_volume(closeadj, volume, 252) * atr
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d climax × ATR
def f05vc_f05_volume_at_capitulation_climaxxatr_21d_slope_v112_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_capitulation_climax(closeadj, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax × ATR
def f05vc_f05_volume_at_capitulation_climaxxatr_63d_slope_v113_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_capitulation_climax(closeadj, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic vol diff (21-63)
def f05vc_f05_volume_at_capitulation_panicvoldiff_21m63_slope_v114_signal(closeadj, volume):
    base = (_f05_panic_volume(closeadj, volume, 21) - _f05_panic_volume(closeadj, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic vol diff (63-252)
def f05vc_f05_volume_at_capitulation_panicvoldiff_63m252_slope_v115_signal(closeadj, volume):
    base = (_f05_panic_volume(closeadj, volume, 63) - _f05_panic_volume(closeadj, volume, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic vol ratio 21v252
def f05vc_f05_volume_at_capitulation_panicvolratio_21v252_slope_v116_signal(closeadj, volume):
    a = _f05_panic_volume(closeadj, volume, 21)
    b = _f05_panic_volume(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic vol ratio 63v252
def f05vc_f05_volume_at_capitulation_panicvolratio_63v252_slope_v117_signal(closeadj, volume):
    a = _f05_panic_volume(closeadj, volume, 63)
    b = _f05_panic_volume(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of climax diff (21-63)
def f05vc_f05_volume_at_capitulation_climaxdiff_21m63_slope_v118_signal(closeadj, volume):
    base = (_f05_capitulation_climax(closeadj, volume, 21) - _f05_capitulation_climax(closeadj, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of climax ratio 63v252
def f05vc_f05_volume_at_capitulation_climaxratio_63v252_slope_v119_signal(closeadj, volume):
    a = _f05_capitulation_climax(closeadj, volume, 63)
    b = _f05_capitulation_climax(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_21d_slope_v120_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = pv.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_63d_slope_v121_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 63)
    base = pv.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_252d_slope_v122_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 252)
    base = pv.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × abs ret
def f05vc_f05_volume_at_capitulation_capvolzxabsret_21d_slope_v123_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    base = _f05_capitulation_volz(closeadj, volume, 21) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × abs ret
def f05vc_f05_volume_at_capitulation_capvolzxabsret_63d_slope_v124_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    base = _f05_capitulation_volz(closeadj, volume, 63) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × abs ret
def f05vc_f05_volume_at_capitulation_capvolzxabsret_252d_slope_v125_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(252, min_periods=63).mean()
    base = _f05_capitulation_volz(closeadj, volume, 252) * ar * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax sum
def f05vc_f05_volume_at_capitulation_climaxsum_63d_slope_v126_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    base = cl.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d climax sum
def f05vc_f05_volume_at_capitulation_climaxsum_252d_slope_v127_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    base = cl.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d panic vol sum
def f05vc_f05_volume_at_capitulation_panicvolsum_63d_slope_v128_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = pv.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic vol sum
def f05vc_f05_volume_at_capitulation_panicvolsum_252d_slope_v129_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 63)
    base = pv.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d climax max
def f05vc_f05_volume_at_capitulation_climaxmax_63d_slope_v130_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    base = cl.rolling(63, min_periods=21).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d climax max
def f05vc_f05_volume_at_capitulation_climaxmax_252d_slope_v131_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    base = cl.rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d climax event count
def f05vc_f05_volume_at_capitulation_climaxeventcount_252d_slope_v132_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    base = (cl).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d climax event count
def f05vc_f05_volume_at_capitulation_climaxeventcount_504d_slope_v133_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    base = (cl).rolling(504, min_periods=126).mean() * (1.0 + closeadj * 0.001)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × climax
def f05vc_f05_volume_at_capitulation_capvolzxclimax_21d_slope_v134_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_climax(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × climax
def f05vc_f05_volume_at_capitulation_capvolzxclimax_63d_slope_v135_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * _f05_capitulation_climax(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × climax
def f05vc_f05_volume_at_capitulation_capvolzxclimax_252d_slope_v136_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 252) * _f05_capitulation_climax(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d×63d capvolz product
def f05vc_f05_volume_at_capitulation_capvolzxlong_21x63_slope_v137_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d×252d capvolz product
def f05vc_f05_volume_at_capitulation_capvolzxlong_63x252_slope_v138_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 63) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d×252d capvolz product
def f05vc_f05_volume_at_capitulation_capvolzxlong_21x252_slope_v139_signal(closeadj, volume):
    base = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic × capvolz
def f05vc_f05_volume_at_capitulation_panicxcapvolz_21d_slope_v140_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d panic × capvolz
def f05vc_f05_volume_at_capitulation_panicxcapvolz_252d_slope_v141_signal(closeadj, volume):
    base = _f05_panic_volume(closeadj, volume, 252) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × volume ratio
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_21d_slope_v142_signal(closeadj, volume):
    vmean = _mean(volume, 21).replace(0, np.nan)
    base = _f05_capitulation_volz(closeadj, volume, 21) * (volume / vmean) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz × volume ratio
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_63d_slope_v143_signal(closeadj, volume):
    vmean = _mean(volume, 63).replace(0, np.nan)
    base = _f05_capitulation_volz(closeadj, volume, 63) * (volume / vmean) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz × volume ratio
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_252d_slope_v144_signal(closeadj, volume):
    vmean = _mean(volume, 252).replace(0, np.nan)
    base = _f05_capitulation_volz(closeadj, volume, 252) * (volume / vmean) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz anom
def f05vc_f05_volume_at_capitulation_capvolzanom_21d_slope_v145_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    base = (cv - _mean(cv, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capvolz anom
def f05vc_f05_volume_at_capitulation_capvolzanom_63d_slope_v146_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = (cv - _mean(cv, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capvolz anom
def f05vc_f05_volume_at_capitulation_capvolzanom_252d_slope_v147_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = (cv - _mean(cv, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of panic vol anom
def f05vc_f05_volume_at_capitulation_panicvolanom_21d_slope_v148_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = (pv - _mean(pv, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capvolz × low diff
def f05vc_f05_volume_at_capitulation_capvolzxlowdiff_21d_slope_v149_signal(closeadj, volume, low):
    diff = (closeadj - low) / closeadj.replace(0, np.nan)
    base = _f05_capitulation_volz(closeadj, volume, 21) * diff * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d panic × hl spread
def f05vc_f05_volume_at_capitulation_panicvolxhlspread_21d_slope_v150_signal(closeadj, volume, high, low):
    sp = (high - low) / closeadj.replace(0, np.nan)
    base = _f05_panic_volume(closeadj, volume, 21) * sp * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05vc_f05_volume_at_capitulation_capvolz_21d_slope_v001_signal,
    f05vc_f05_volume_at_capitulation_capvolz_21d_slope_v002_signal,
    f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v003_signal,
    f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v004_signal,
    f05vc_f05_volume_at_capitulation_capvolz_63d_slope_v005_signal,
    f05vc_f05_volume_at_capitulation_capvolz_126d_slope_v006_signal,
    f05vc_f05_volume_at_capitulation_capvolz_126d_slope_v007_signal,
    f05vc_f05_volume_at_capitulation_capvolz_252d_slope_v008_signal,
    f05vc_f05_volume_at_capitulation_capvolz_252d_slope_v009_signal,
    f05vc_f05_volume_at_capitulation_capvolz_504d_slope_v010_signal,
    f05vc_f05_volume_at_capitulation_capvolz_504d_slope_v011_signal,
    f05vc_f05_volume_at_capitulation_capvolz_5d_slope_v012_signal,
    f05vc_f05_volume_at_capitulation_capvolz_10d_slope_v013_signal,
    f05vc_f05_volume_at_capitulation_capvolz_42d_slope_v014_signal,
    f05vc_f05_volume_at_capitulation_capvolz_189d_slope_v015_signal,
    f05vc_f05_volume_at_capitulation_capvolz_378d_slope_v016_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_21d_slope_v017_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_63d_slope_v018_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_252d_slope_v019_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_21d_slope_v020_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_63d_slope_v021_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_252d_slope_v022_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_21d_slope_v023_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_63d_slope_v024_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_252d_slope_v025_signal,
    f05vc_f05_volume_at_capitulation_capvolzmax_63d_slope_v026_signal,
    f05vc_f05_volume_at_capitulation_capvolzmax_252d_slope_v027_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_21d_slope_v028_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_21d_slope_v029_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_63d_slope_v030_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_63d_slope_v031_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_252d_slope_v032_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_504d_slope_v033_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_5d_slope_v034_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_10d_slope_v035_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_126d_slope_v036_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_21d_slope_v037_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_63d_slope_v038_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_252d_slope_v039_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_21d_slope_v040_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_63d_slope_v041_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_252d_slope_v042_signal,
    f05vc_f05_volume_at_capitulation_climax_21d_slope_v043_signal,
    f05vc_f05_volume_at_capitulation_climax_63d_slope_v044_signal,
    f05vc_f05_volume_at_capitulation_climax_126d_slope_v045_signal,
    f05vc_f05_volume_at_capitulation_climax_252d_slope_v046_signal,
    f05vc_f05_volume_at_capitulation_climax_504d_slope_v047_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_21d_slope_v048_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_63d_slope_v049_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_252d_slope_v050_signal,
    f05vc_f05_volume_at_capitulation_climaxema_21d_slope_v051_signal,
    f05vc_f05_volume_at_capitulation_climaxema_63d_slope_v052_signal,
    f05vc_f05_volume_at_capitulation_climaxema_252d_slope_v053_signal,
    f05vc_f05_volume_at_capitulation_capeventcount_252d_slope_v054_signal,
    f05vc_f05_volume_at_capitulation_capeventcount_504d_slope_v055_signal,
    f05vc_f05_volume_at_capitulation_paniceventcount_252d_slope_v056_signal,
    f05vc_f05_volume_at_capitulation_paniceventcount_70_slope_v057_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_21d_slope_v058_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_63d_slope_v059_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_252d_slope_v060_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_21d_slope_v061_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_63d_slope_v062_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_252d_slope_v063_signal,
    f05vc_f05_volume_at_capitulation_panicvolxdv_21d_slope_v064_signal,
    f05vc_f05_volume_at_capitulation_panicvolxdv_63d_slope_v065_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_21d_slope_v066_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_63d_slope_v067_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_252d_slope_v068_signal,
    f05vc_f05_volume_at_capitulation_capvolzdiff_21m63_slope_v069_signal,
    f05vc_f05_volume_at_capitulation_capvolzdiff_63m252_slope_v070_signal,
    f05vc_f05_volume_at_capitulation_capvolzratio_21v252_slope_v071_signal,
    f05vc_f05_volume_at_capitulation_capvolzratio_63v252_slope_v072_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_21d_slope_v073_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_63d_slope_v074_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_252d_slope_v075_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_21d_slope_v076_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_63d_slope_v077_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_252d_slope_v078_signal,
    f05vc_f05_volume_at_capitulation_climaxxpanic_21d_slope_v079_signal,
    f05vc_f05_volume_at_capitulation_climaxxpanic_63d_slope_v080_signal,
    f05vc_f05_volume_at_capitulation_capcomposite_252d_slope_v081_signal,
    f05vc_f05_volume_at_capitulation_capcomposite_21d_slope_v082_signal,
    f05vc_f05_volume_at_capitulation_capvolzxhlrange_21d_slope_v083_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrv_21d_slope_v084_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrv_63d_slope_v085_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrv_252d_slope_v086_signal,
    f05vc_f05_volume_at_capitulation_capvolzxskew_63d_slope_v087_signal,
    f05vc_f05_volume_at_capitulation_capvolzxkurt_252d_slope_v088_signal,
    f05vc_f05_volume_at_capitulation_panicvolxskew_63d_slope_v089_signal,
    f05vc_f05_volume_at_capitulation_panicvolxkurt_252d_slope_v090_signal,
    f05vc_f05_volume_at_capitulation_capvolzemaxdv_21d_slope_v091_signal,
    f05vc_f05_volume_at_capitulation_capvolzemaxdv_63d_slope_v092_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_21d_slope_v093_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_63d_slope_v094_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_252d_slope_v095_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlog_21d_slope_v096_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlog_63d_slope_v097_signal,
    f05vc_f05_volume_at_capitulation_panicvolxlog_21d_slope_v098_signal,
    f05vc_f05_volume_at_capitulation_climaxxlog_21d_slope_v099_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_21d_slope_v100_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_63d_slope_v101_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_252d_slope_v102_signal,
    f05vc_f05_volume_at_capitulation_climaxxvolz_21d_slope_v103_signal,
    f05vc_f05_volume_at_capitulation_climaxxvolz_63d_slope_v104_signal,
    f05vc_f05_volume_at_capitulation_panicvolxvolz_21d_slope_v105_signal,
    f05vc_f05_volume_at_capitulation_panicvolxvolz_63d_slope_v106_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrange_21d_slope_v107_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrange_63d_slope_v108_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_21d_slope_v109_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_63d_slope_v110_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_252d_slope_v111_signal,
    f05vc_f05_volume_at_capitulation_climaxxatr_21d_slope_v112_signal,
    f05vc_f05_volume_at_capitulation_climaxxatr_63d_slope_v113_signal,
    f05vc_f05_volume_at_capitulation_panicvoldiff_21m63_slope_v114_signal,
    f05vc_f05_volume_at_capitulation_panicvoldiff_63m252_slope_v115_signal,
    f05vc_f05_volume_at_capitulation_panicvolratio_21v252_slope_v116_signal,
    f05vc_f05_volume_at_capitulation_panicvolratio_63v252_slope_v117_signal,
    f05vc_f05_volume_at_capitulation_climaxdiff_21m63_slope_v118_signal,
    f05vc_f05_volume_at_capitulation_climaxratio_63v252_slope_v119_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_21d_slope_v120_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_63d_slope_v121_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_252d_slope_v122_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_21d_slope_v123_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_63d_slope_v124_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_252d_slope_v125_signal,
    f05vc_f05_volume_at_capitulation_climaxsum_63d_slope_v126_signal,
    f05vc_f05_volume_at_capitulation_climaxsum_252d_slope_v127_signal,
    f05vc_f05_volume_at_capitulation_panicvolsum_63d_slope_v128_signal,
    f05vc_f05_volume_at_capitulation_panicvolsum_252d_slope_v129_signal,
    f05vc_f05_volume_at_capitulation_climaxmax_63d_slope_v130_signal,
    f05vc_f05_volume_at_capitulation_climaxmax_252d_slope_v131_signal,
    f05vc_f05_volume_at_capitulation_climaxeventcount_252d_slope_v132_signal,
    f05vc_f05_volume_at_capitulation_climaxeventcount_504d_slope_v133_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_21d_slope_v134_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_63d_slope_v135_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_252d_slope_v136_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_21x63_slope_v137_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_63x252_slope_v138_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_21x252_slope_v139_signal,
    f05vc_f05_volume_at_capitulation_panicxcapvolz_21d_slope_v140_signal,
    f05vc_f05_volume_at_capitulation_panicxcapvolz_252d_slope_v141_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_21d_slope_v142_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_63d_slope_v143_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_252d_slope_v144_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_21d_slope_v145_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_63d_slope_v146_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_252d_slope_v147_signal,
    f05vc_f05_volume_at_capitulation_panicvolanom_21d_slope_v148_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlowdiff_21d_slope_v149_signal,
    f05vc_f05_volume_at_capitulation_panicvolxhlspread_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_VOLUME_AT_CAPITULATION_REGISTRY_SLOPE = REGISTRY


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
    domain_primitives = ("_f05_capitulation_volz", "_f05_panic_volume", "_f05_capitulation_climax")
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
    print(f"OK f05_volume_at_capitulation_2nd_derivatives_001_150_claude: {n_features} features pass")
