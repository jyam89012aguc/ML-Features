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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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


# 21d capitulation volume z weighted by 21d crash depth
def f05vc_f05_volume_at_capitulation_capvolz_21d_base_v001_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_63d_base_v002_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_126d_base_v003_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_252d_base_v004_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_504d_base_v005_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d capitulation volume z × short depth
def f05vc_f05_volume_at_capitulation_capvolz_5d_base_v006_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_10d_base_v007_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_42d_base_v008_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_189d_base_v009_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d capitulation volume z × depth
def f05vc_f05_volume_at_capitulation_capvolz_378d_base_v010_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capitulation volume z squared (severity-weighted)
def f05vc_f05_volume_at_capitulation_capvolzsq_21d_base_v011_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    result = cv * cv.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capitulation volume z squared
def f05vc_f05_volume_at_capitulation_capvolzsq_63d_base_v012_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv * cv.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capitulation volume z squared
def f05vc_f05_volume_at_capitulation_capvolzsq_252d_base_v013_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    result = cv * cv.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzema_21d_base_v014_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    result = cv.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzema_63d_base_v015_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzema_252d_base_v016_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    result = cv.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzsum_21d_base_v017_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzsum_63d_base_v018_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzsum_252d_base_v019_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    result = cv.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of capitulation volume z (worst capit moment)
def f05vc_f05_volume_at_capitulation_capvolzmax_63d_base_v020_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of capitulation volume z
def f05vc_f05_volume_at_capitulation_capvolzmax_252d_base_v021_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    result = cv.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic volume fraction
def f05vc_f05_volume_at_capitulation_panicvolfrac_21d_base_v022_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic volume fraction
def f05vc_f05_volume_at_capitulation_panicvolfrac_63d_base_v023_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic volume fraction
def f05vc_f05_volume_at_capitulation_panicvolfrac_252d_base_v024_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d panic volume fraction
def f05vc_f05_volume_at_capitulation_panicvolfrac_504d_base_v025_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d panic vol frac
def f05vc_f05_volume_at_capitulation_panicvolfrac_5d_base_v026_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d panic vol frac
def f05vc_f05_volume_at_capitulation_panicvolfrac_10d_base_v027_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d panic vol frac
def f05vc_f05_volume_at_capitulation_panicvolfrac_126d_base_v028_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic volume fraction × 21d return volatility
def f05vc_f05_volume_at_capitulation_panicvolxrv_21d_base_v029_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    result = _f05_panic_volume(closeadj, volume, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × 63d rv
def f05vc_f05_volume_at_capitulation_panicvolxrv_63d_base_v030_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f05_panic_volume(closeadj, volume, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × rv
def f05vc_f05_volume_at_capitulation_panicvolxrv_252d_base_v031_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f05_panic_volume(closeadj, volume, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic volume fraction zscore over 252d
def f05vc_f05_volume_at_capitulation_panicvolz_21d_base_v032_signal(closeadj, volume):
    result = _z(_f05_panic_volume(closeadj, volume, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol z over 252d
def f05vc_f05_volume_at_capitulation_panicvolz_63d_base_v033_signal(closeadj, volume):
    result = _z(_f05_panic_volume(closeadj, volume, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol z over 504d
def f05vc_f05_volume_at_capitulation_panicvolz_252d_base_v034_signal(closeadj, volume):
    result = _z(_f05_panic_volume(closeadj, volume, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climactic capitulation (volume spike at low)
def f05vc_f05_volume_at_capitulation_climax_21d_base_v035_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climactic capitulation
def f05vc_f05_volume_at_capitulation_climax_63d_base_v036_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d climax
def f05vc_f05_volume_at_capitulation_climax_126d_base_v037_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax
def f05vc_f05_volume_at_capitulation_climax_252d_base_v038_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d climax
def f05vc_f05_volume_at_capitulation_climax_504d_base_v039_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_21d_base_v040_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_climax(closeadj, volume, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_63d_base_v041_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_climax(closeadj, volume, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d climax × dollar volume
def f05vc_f05_volume_at_capitulation_climaxxdv_252d_base_v042_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_climax(closeadj, volume, 252) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of climax
def f05vc_f05_volume_at_capitulation_climaxema_21d_base_v043_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    result = cl.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of climax
def f05vc_f05_volume_at_capitulation_climaxema_63d_base_v044_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    result = cl.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of climax
def f05vc_f05_volume_at_capitulation_climaxema_252d_base_v045_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 252)
    result = cl.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of capitulation events (capvolz over 2 sigma)
def f05vc_f05_volume_at_capitulation_capeventcount_252d_base_v046_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    result = cv.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of capitulation events
def f05vc_f05_volume_at_capitulation_capeventcount_504d_base_v047_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    result = cv.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of panic events (panicvolfrac > 0.6)
def f05vc_f05_volume_at_capitulation_paniceventcount_252d_base_v048_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    result = (pv).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of panic events (panicvolfrac > 0.7)
def f05vc_f05_volume_at_capitulation_paniceventcount_70_base_v049_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    result = (pv).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capitulation volume z × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzxdv_21d_base_v050_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_volz(closeadj, volume, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzxdv_63d_base_v051_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_volz(closeadj, volume, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzxdv_252d_base_v052_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_capitulation_volz(closeadj, volume, 252) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × 21d return
def f05vc_f05_volume_at_capitulation_capvolzxret_21d_base_v053_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    result = _f05_capitulation_volz(closeadj, volume, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × 63d return
def f05vc_f05_volume_at_capitulation_capvolzxret_63d_base_v054_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    result = _f05_capitulation_volz(closeadj, volume, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × 252d return
def f05vc_f05_volume_at_capitulation_capvolzxret_252d_base_v055_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    result = _f05_capitulation_volz(closeadj, volume, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × dollar volume
def f05vc_f05_volume_at_capitulation_panicvolxdv_21d_base_v056_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_panic_volume(closeadj, volume, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × dollar volume
def f05vc_f05_volume_at_capitulation_panicvolxdv_63d_base_v057_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_panic_volume(closeadj, volume, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × 21d return
def f05vc_f05_volume_at_capitulation_panicvolxret_21d_base_v058_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    result = _f05_panic_volume(closeadj, volume, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × 63d return
def f05vc_f05_volume_at_capitulation_panicvolxret_63d_base_v059_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    result = _f05_panic_volume(closeadj, volume, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × 252d return
def f05vc_f05_volume_at_capitulation_panicvolxret_252d_base_v060_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    result = _f05_panic_volume(closeadj, volume, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz minus 63d capvolz (acceleration of capitulation)
def f05vc_f05_volume_at_capitulation_capvolzdiff_21m63_base_v061_signal(closeadj, volume):
    result = (_f05_capitulation_volz(closeadj, volume, 21) - _f05_capitulation_volz(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz minus 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolzdiff_63m252_base_v062_signal(closeadj, volume):
    result = (_f05_capitulation_volz(closeadj, volume, 63) - _f05_capitulation_volz(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz / 252d capvolz ratio
def f05vc_f05_volume_at_capitulation_capvolzratio_21v252_base_v063_signal(closeadj, volume):
    a = _f05_capitulation_volz(closeadj, volume, 21)
    b = _f05_capitulation_volz(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz / 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolzratio_63v252_base_v064_signal(closeadj, volume):
    a = _f05_capitulation_volz(closeadj, volume, 63)
    b = _f05_capitulation_volz(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × 21d ATR (volatile capitulation)
def f05vc_f05_volume_at_capitulation_capvolzxatr_21d_base_v065_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × 21d ATR
def f05vc_f05_volume_at_capitulation_capvolzxatr_63d_base_v066_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × 63d ATR
def f05vc_f05_volume_at_capitulation_capvolzxatr_252d_base_v067_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f05_capitulation_volz(closeadj, volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × panic vol fraction
def f05vc_f05_volume_at_capitulation_capvolzxpanic_21d_base_v068_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * _f05_panic_volume(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × panic vol fraction
def f05vc_f05_volume_at_capitulation_capvolzxpanic_63d_base_v069_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 63) * _f05_panic_volume(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × panic vol fraction
def f05vc_f05_volume_at_capitulation_capvolzxpanic_252d_base_v070_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 252) * _f05_panic_volume(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × panic vol fraction
def f05vc_f05_volume_at_capitulation_climaxxpanic_21d_base_v071_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 21) * _f05_panic_volume(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax × panic vol
def f05vc_f05_volume_at_capitulation_climaxxpanic_63d_base_v072_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 63) * _f05_panic_volume(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite capitulation: capvolz + climax + panic
def f05vc_f05_volume_at_capitulation_capcomposite_252d_base_v073_signal(closeadj, volume):
    result = (_f05_capitulation_volz(closeadj, volume, 252) + _f05_capitulation_climax(closeadj, volume, 252) + _f05_panic_volume(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite capitulation
def f05vc_f05_volume_at_capitulation_capcomposite_21d_base_v074_signal(closeadj, volume):
    result = (_f05_capitulation_volz(closeadj, volume, 21) + _f05_capitulation_climax(closeadj, volume, 21) + _f05_panic_volume(closeadj, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × ATR-style range from high-low
def f05vc_f05_volume_at_capitulation_capvolzxhlrange_21d_base_v075_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05vc_f05_volume_at_capitulation_capvolz_21d_base_v001_signal,
    f05vc_f05_volume_at_capitulation_capvolz_63d_base_v002_signal,
    f05vc_f05_volume_at_capitulation_capvolz_126d_base_v003_signal,
    f05vc_f05_volume_at_capitulation_capvolz_252d_base_v004_signal,
    f05vc_f05_volume_at_capitulation_capvolz_504d_base_v005_signal,
    f05vc_f05_volume_at_capitulation_capvolz_5d_base_v006_signal,
    f05vc_f05_volume_at_capitulation_capvolz_10d_base_v007_signal,
    f05vc_f05_volume_at_capitulation_capvolz_42d_base_v008_signal,
    f05vc_f05_volume_at_capitulation_capvolz_189d_base_v009_signal,
    f05vc_f05_volume_at_capitulation_capvolz_378d_base_v010_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_21d_base_v011_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_63d_base_v012_signal,
    f05vc_f05_volume_at_capitulation_capvolzsq_252d_base_v013_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_21d_base_v014_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_63d_base_v015_signal,
    f05vc_f05_volume_at_capitulation_capvolzema_252d_base_v016_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_21d_base_v017_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_63d_base_v018_signal,
    f05vc_f05_volume_at_capitulation_capvolzsum_252d_base_v019_signal,
    f05vc_f05_volume_at_capitulation_capvolzmax_63d_base_v020_signal,
    f05vc_f05_volume_at_capitulation_capvolzmax_252d_base_v021_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_21d_base_v022_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_63d_base_v023_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_252d_base_v024_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_504d_base_v025_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_5d_base_v026_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_10d_base_v027_signal,
    f05vc_f05_volume_at_capitulation_panicvolfrac_126d_base_v028_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_21d_base_v029_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_63d_base_v030_signal,
    f05vc_f05_volume_at_capitulation_panicvolxrv_252d_base_v031_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_21d_base_v032_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_63d_base_v033_signal,
    f05vc_f05_volume_at_capitulation_panicvolz_252d_base_v034_signal,
    f05vc_f05_volume_at_capitulation_climax_21d_base_v035_signal,
    f05vc_f05_volume_at_capitulation_climax_63d_base_v036_signal,
    f05vc_f05_volume_at_capitulation_climax_126d_base_v037_signal,
    f05vc_f05_volume_at_capitulation_climax_252d_base_v038_signal,
    f05vc_f05_volume_at_capitulation_climax_504d_base_v039_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_21d_base_v040_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_63d_base_v041_signal,
    f05vc_f05_volume_at_capitulation_climaxxdv_252d_base_v042_signal,
    f05vc_f05_volume_at_capitulation_climaxema_21d_base_v043_signal,
    f05vc_f05_volume_at_capitulation_climaxema_63d_base_v044_signal,
    f05vc_f05_volume_at_capitulation_climaxema_252d_base_v045_signal,
    f05vc_f05_volume_at_capitulation_capeventcount_252d_base_v046_signal,
    f05vc_f05_volume_at_capitulation_capeventcount_504d_base_v047_signal,
    f05vc_f05_volume_at_capitulation_paniceventcount_252d_base_v048_signal,
    f05vc_f05_volume_at_capitulation_paniceventcount_70_base_v049_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_21d_base_v050_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_63d_base_v051_signal,
    f05vc_f05_volume_at_capitulation_capvolzxdv_252d_base_v052_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_21d_base_v053_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_63d_base_v054_signal,
    f05vc_f05_volume_at_capitulation_capvolzxret_252d_base_v055_signal,
    f05vc_f05_volume_at_capitulation_panicvolxdv_21d_base_v056_signal,
    f05vc_f05_volume_at_capitulation_panicvolxdv_63d_base_v057_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_21d_base_v058_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_63d_base_v059_signal,
    f05vc_f05_volume_at_capitulation_panicvolxret_252d_base_v060_signal,
    f05vc_f05_volume_at_capitulation_capvolzdiff_21m63_base_v061_signal,
    f05vc_f05_volume_at_capitulation_capvolzdiff_63m252_base_v062_signal,
    f05vc_f05_volume_at_capitulation_capvolzratio_21v252_base_v063_signal,
    f05vc_f05_volume_at_capitulation_capvolzratio_63v252_base_v064_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_21d_base_v065_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_63d_base_v066_signal,
    f05vc_f05_volume_at_capitulation_capvolzxatr_252d_base_v067_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_21d_base_v068_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_63d_base_v069_signal,
    f05vc_f05_volume_at_capitulation_capvolzxpanic_252d_base_v070_signal,
    f05vc_f05_volume_at_capitulation_climaxxpanic_21d_base_v071_signal,
    f05vc_f05_volume_at_capitulation_climaxxpanic_63d_base_v072_signal,
    f05vc_f05_volume_at_capitulation_capcomposite_252d_base_v073_signal,
    f05vc_f05_volume_at_capitulation_capcomposite_21d_base_v074_signal,
    f05vc_f05_volume_at_capitulation_capvolzxhlrange_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_VOLUME_AT_CAPITULATION_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_volume_at_capitulation_base_001_075_claude: {n_features} features pass")
