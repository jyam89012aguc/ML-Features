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


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan).shift(w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f29_revenue_accel(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    return _diff(g, w)


def _f29_revenue_growth(revenue, w):
    return _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)


def _f29_revenue_jerk(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    a = _diff(g, w)
    return _diff(a, w)


# 5d jerk of 21d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_21d_jerk_v001_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_21d_jerk_v002_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v003_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v004_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v005_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_126d_jerk_v006_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_126d_jerk_v007_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_252d_jerk_v008_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_252d_jerk_v009_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_504d_jerk_v010_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d revenue accel × closeadj
def f29ra_f29_revenue_acceleration_revaccel_504d_jerk_v011_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel mean 21d × closeadj
def f29ra_f29_revenue_acceleration_revaccelmean_21d_jerk_v012_signal(revenue, closeadj):
    base = _mean(_f29_revenue_accel(revenue, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel mean 63d × closeadj
def f29ra_f29_revenue_acceleration_revaccelmean_63d_jerk_v013_signal(revenue, closeadj):
    base = _mean(_f29_revenue_accel(revenue, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel mean 126d × closeadj
def f29ra_f29_revenue_acceleration_revaccelmean_252d_jerk_v014_signal(revenue, closeadj):
    base = _mean(_f29_revenue_accel(revenue, 252), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel z 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelz_252d_jerk_v015_signal(revenue, closeadj):
    base = _z(_f29_revenue_accel(revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel z 504d × closeadj
def f29ra_f29_revenue_acceleration_revaccelz_504d_jerk_v016_signal(revenue, closeadj):
    base = _z(_f29_revenue_accel(revenue, 252), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel × revlevel 21d × closeadj
def f29ra_f29_revenue_acceleration_revaccelxlvl_21d_jerk_v017_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 21) * _mean(revenue, 21) / 1e8 * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × revlevel 63d × closeadj
def f29ra_f29_revenue_acceleration_revaccelxlvl_63d_jerk_v018_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63) * _mean(revenue, 63) / 1e8 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × revlevel 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelxlvl_252d_jerk_v019_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × revlevel 504d × closeadj
def f29ra_f29_revenue_acceleration_revaccelxlvl_504d_jerk_v020_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252) * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel sq 21d × closeadj
def f29ra_f29_revenue_acceleration_revaccelsq_21d_jerk_v021_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a * a.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel sq 63d × closeadj
def f29ra_f29_revenue_acceleration_revaccelsq_63d_jerk_v022_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a * a.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel sq 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelsq_252d_jerk_v023_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * a.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel up cnt 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelupcnt_252d_jerk_v024_signal(revenue, closeadj):
    flag = (_f29_revenue_accel(revenue, 21) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel down cnt 504d × closeadj
def f29ra_f29_revenue_acceleration_revacceldowncnt_504d_jerk_v025_signal(revenue, closeadj):
    flag = (_f29_revenue_accel(revenue, 63) < 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel abs 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelabs_252d_jerk_v026_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel abs 504d × closeadj
def f29ra_f29_revenue_acceleration_revaccelabs_504d_jerk_v027_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel ema 21d × closeadj
def f29ra_f29_revenue_acceleration_revaccelema_21d_jerk_v028_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 21).ewm(span=21, adjust=False, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel ema 63d × closeadj
def f29ra_f29_revenue_acceleration_revaccelema_63d_jerk_v029_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel ema 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelema_252d_jerk_v030_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252).ewm(span=252, adjust=False, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel std 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelstd_252d_jerk_v031_signal(revenue, closeadj):
    base = _std(_f29_revenue_accel(revenue, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel std 504d × closeadj
def f29ra_f29_revenue_acceleration_revaccelstd_504d_jerk_v032_signal(revenue, closeadj):
    base = _std(_f29_revenue_accel(revenue, 63), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel sign sum 252d × closeadj
def f29ra_f29_revenue_acceleration_revaccelsign_252d_jerk_v033_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel sign sum 504d × closeadj
def f29ra_f29_revenue_acceleration_revaccelsign_504d_jerk_v034_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel ultra 5d × closeadj
def f29ra_f29_revenue_acceleration_revaccelultra_5d_jerk_v035_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel 10d × closeadj
def f29ra_f29_revenue_acceleration_revaccelshrt_10d_jerk_v036_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel 42d × closeadj
def f29ra_f29_revenue_acceleration_revaccelmed_42d_jerk_v037_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel 189d × closeadj
def f29ra_f29_revenue_acceleration_revaccellong_189d_jerk_v038_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel 378d × closeadj
def f29ra_f29_revenue_acceleration_revaccelvlong_378d_jerk_v039_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × growth 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxgrow_252d_jerk_v040_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = a * g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × growth 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxgrow_504d_jerk_v041_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = a * g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel/growth 252d × closeadj
def f29ra_f29_revenue_acceleration_accelvsgrow_252d_jerk_v042_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252).replace(0, np.nan)
    base = (a / g) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel/growth 504d × closeadj
def f29ra_f29_revenue_acceleration_accelvsgrow_504d_jerk_v043_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252).replace(0, np.nan)
    base = (a / g) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue jerk 252d × closeadj
def f29ra_f29_revenue_acceleration_revjerk_252d_jerk_v044_signal(revenue, closeadj):
    base = _f29_revenue_jerk(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of revenue jerk 504d × closeadj
def f29ra_f29_revenue_acceleration_revjerk_504d_jerk_v045_signal(revenue, closeadj):
    base = _f29_revenue_jerk(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ni 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxni_252d_jerk_v046_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(netinc, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ni 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxni_504d_jerk_v047_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(netinc, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × fcf 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxfcf_252d_jerk_v048_signal(revenue, fcf, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(fcf, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × fcf 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxfcf_504d_jerk_v049_signal(revenue, fcf, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(fcf, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ebitda 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxebitda_252d_jerk_v050_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(ebitda, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ebitda 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxebitda_504d_jerk_v051_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(ebitda, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × gp 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxgp_252d_jerk_v052_signal(revenue, gp, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(gp, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × gp 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxgp_504d_jerk_v053_signal(revenue, gp, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(gp, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel/sharesbas 21d × closeadj
def f29ra_f29_revenue_acceleration_accelpershare_21d_jerk_v054_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a * _safe_div(_mean(revenue, 21), _mean(sharesbas, 21)) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel/sharesbas 63d × closeadj
def f29ra_f29_revenue_acceleration_accelpershare_63d_jerk_v055_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a * _safe_div(_mean(revenue, 63), _mean(sharesbas, 63)) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel/sharesbas 252d × closeadj
def f29ra_f29_revenue_acceleration_accelpershare_252d_jerk_v056_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _safe_div(_mean(revenue, 252), _mean(sharesbas, 252)) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel ratio 63v252 × closeadj
def f29ra_f29_revenue_acceleration_accelratio_63v252_jerk_v057_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 63)
    la = _f29_revenue_accel(revenue, 252).replace(0, np.nan)
    base = (sa / la) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel ratio 21v63 × closeadj
def f29ra_f29_revenue_acceleration_accelratio_21v63_jerk_v058_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 21)
    la = _f29_revenue_accel(revenue, 63).replace(0, np.nan)
    base = (sa / la) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel ratio 252v504 × closeadj
def f29ra_f29_revenue_acceleration_accelratio_252v504_jerk_v059_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 252)
    la = _f29_revenue_accel(revenue, 252).replace(0, np.nan)
    base = (sa / la) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel sum abs 252d × closeadj
def f29ra_f29_revenue_acceleration_accelsumabs_252d_jerk_v060_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21).abs()
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel sum abs 504d × closeadj
def f29ra_f29_revenue_acceleration_accelsumabs_504d_jerk_v061_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63).abs()
    base = a.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel cum 252d × closeadj
def f29ra_f29_revenue_acceleration_accelcum_252d_jerk_v062_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel cum 504d × closeadj
def f29ra_f29_revenue_acceleration_accelcum_504d_jerk_v063_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel cv 252d × closeadj
def f29ra_f29_revenue_acceleration_accelcv_252d_jerk_v064_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = _safe_div(_std(a, 252), _mean(a.abs(), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel cv 504d × closeadj
def f29ra_f29_revenue_acceleration_accelcv_504d_jerk_v065_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = _safe_div(_std(a, 504), _mean(a.abs(), 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel skew 252d × closeadj
def f29ra_f29_revenue_acceleration_accelskew_252d_jerk_v066_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel skew 504d × closeadj
def f29ra_f29_revenue_acceleration_accelskew_504d_jerk_v067_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(504, min_periods=126).skew() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel kurt 252d × closeadj
def f29ra_f29_revenue_acceleration_accelkurt_252d_jerk_v068_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel kurt 504d × closeadj
def f29ra_f29_revenue_acceleration_accelkurt_504d_jerk_v069_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(504, min_periods=126).kurt() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ncfo 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfo_252d_jerk_v070_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(ncfo, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ncfo 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfo_504d_jerk_v071_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(ncfo, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × opinc 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxopinc_252d_jerk_v072_signal(revenue, opinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(opinc, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × opinc 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxopinc_504d_jerk_v073_signal(revenue, opinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(opinc, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × revsq 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxrevsq_252d_jerk_v074_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rev = _mean(revenue, 252) / 1e8
    base = a * rev * rev * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × revsq 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxrevsq_504d_jerk_v075_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rev = _mean(revenue, 252) / 1e8
    base = a * rev * rev * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel xmom 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxmom_21d_jerk_v076_signal(revenue, closeadj):
    mom = closeadj.pct_change(21)
    base = _f29_revenue_accel(revenue, 21) * (1.0 + mom) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel xmom 63d × closeadj
def f29ra_f29_revenue_acceleration_accelxmom_63d_jerk_v077_signal(revenue, closeadj):
    mom = closeadj.pct_change(63)
    base = _f29_revenue_accel(revenue, 63) * (1.0 + mom) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel xmom 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxmom_252d_jerk_v078_signal(revenue, closeadj):
    mom = closeadj.pct_change(252)
    base = _f29_revenue_accel(revenue, 252) * (1.0 + mom) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel + grow 252d × closeadj
def f29ra_f29_revenue_acceleration_accelplusgrow_252d_jerk_v079_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = (a + g) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel + grow 504d × closeadj
def f29ra_f29_revenue_acceleration_accelplusgrow_504d_jerk_v080_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = (a + g) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × log mcap 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxmcap_252d_jerk_v081_signal(revenue, marketcap, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × log mcap 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxmcap_504d_jerk_v082_signal(revenue, marketcap, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel - grow 252d × closeadj
def f29ra_f29_revenue_acceleration_accelminusgrow_252d_jerk_v083_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = (a - g) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel - grow 504d × closeadj
def f29ra_f29_revenue_acceleration_accelminusgrow_504d_jerk_v084_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = (a - g) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel × revlvl 21d × closeadj
def f29ra_f29_revenue_acceleration_accelrevlvl_21d_jerk_v085_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a * _mean(revenue, 21) / 1e8 * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × revlvl 63d × closeadj
def f29ra_f29_revenue_acceleration_accelrevlvl_63d_jerk_v086_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a * _mean(revenue, 63) / 1e8 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × revlvl 252d × closeadj
def f29ra_f29_revenue_acceleration_accelrevlvl_252d_jerk_v087_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × revlvl 504d × closeadj
def f29ra_f29_revenue_acceleration_accelrevlvl_504d_jerk_v088_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × rat rev2ni 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxratrev2ni_252d_jerk_v089_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(netinc, 252))
    base = a * rat * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × rat rev2ni 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxratrev2ni_504d_jerk_v090_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(netinc, 504))
    base = a * rat * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × at 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxat_252d_jerk_v091_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(assets, 252))
    base = a * rat * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × at 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxat_504d_jerk_v092_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(assets, 504))
    base = a * rat * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × eq 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxeq_252d_jerk_v093_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(equity, 252))
    base = a * rat * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × eq 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxeq_504d_jerk_v094_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(equity, 504))
    base = a * rat * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of comp accel 252d × closeadj
def f29ra_f29_revenue_acceleration_compaccel_252d_jerk_v095_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    j = _f29_revenue_jerk(revenue, 252)
    base = (0.5 * a + 0.5 * g + 0.25 * j) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of comp accel 504d × closeadj
def f29ra_f29_revenue_acceleration_compaccel_504d_jerk_v096_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    j = _f29_revenue_jerk(revenue, 126)
    base = (a + g + j) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × vol 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxvol_21d_jerk_v097_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 21)
    base = _f29_revenue_accel(revenue, 21) * (1.0 + sd) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × vol 63d × closeadj
def f29ra_f29_revenue_acceleration_accelxvol_63d_jerk_v098_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 63)
    base = _f29_revenue_accel(revenue, 63) * (1.0 + sd) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × vol 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxvol_252d_jerk_v099_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 252)
    base = _f29_revenue_accel(revenue, 252) * (1.0 + sd) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ret cum 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxretcum_252d_jerk_v100_signal(revenue, closeadj):
    cret = closeadj / closeadj.shift(252).replace(0, np.nan)
    base = _f29_revenue_accel(revenue, 252) * cret * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ret cum 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxretcum_504d_jerk_v101_signal(revenue, closeadj):
    cret = closeadj / closeadj.shift(504).replace(0, np.nan)
    base = _f29_revenue_accel(revenue, 252) * cret * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × eb margin 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxebmargin_252d_jerk_v102_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ebitda, 252), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × eb margin 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxebmargin_504d_jerk_v103_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ebitda, 504), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel × revpershare 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxrevpershare_21d_jerk_v104_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    rps = _safe_div(_mean(revenue, 21), _mean(sharesbas, 21))
    base = a * rps * closeadj / 10.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × revpershare 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxrevpershare_252d_jerk_v105_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rps = _safe_div(_mean(revenue, 252), _mean(sharesbas, 252))
    base = a * rps * closeadj / 10.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel area 252d × closeadj
def f29ra_f29_revenue_acceleration_accelarea_252d_jerk_v106_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(252, min_periods=63).sum() / 252.0 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel area 504d × closeadj
def f29ra_f29_revenue_acceleration_accelarea_504d_jerk_v107_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(504, min_periods=126).sum() / 504.0 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel vs mean 252d × closeadj
def f29ra_f29_revenue_acceleration_accelvsmean_252d_jerk_v108_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = (a - _mean(a, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel vs mean 504d × closeadj
def f29ra_f29_revenue_acceleration_accelvsmean_504d_jerk_v109_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = (a - _mean(a, 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ni margin 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxnimargin_252d_jerk_v110_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(netinc, 252), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ni margin 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxnimargin_504d_jerk_v111_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(netinc, 504), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ncfo margin 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfomargin_252d_jerk_v112_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ncfo, 252), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ncfo margin 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfomargin_504d_jerk_v113_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ncfo, 504), _mean(revenue, 252))
    base = a * margin * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × leverage 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxleverage_252d_jerk_v114_signal(revenue, debt, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    lev = _safe_div(_mean(debt, 252), _mean(equity, 252))
    base = a * (1.0 + lev) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × leverage 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxleverage_504d_jerk_v115_signal(revenue, debt, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    lev = _safe_div(_mean(debt, 504), _mean(equity, 504))
    base = a * (1.0 + lev) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × cap int 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxcapint_252d_jerk_v116_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    intensity = _safe_div(_mean(capex, 252), _mean(revenue, 252))
    base = a * intensity * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × cap int 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxcapint_504d_jerk_v117_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    intensity = _safe_div(_mean(capex, 504), _mean(revenue, 252))
    base = a * intensity * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel sum 21d × closeadj
def f29ra_f29_revenue_acceleration_accelsum_21d_jerk_v118_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel sum 63d × closeadj
def f29ra_f29_revenue_acceleration_accelsum_63d_jerk_v119_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(126, min_periods=42).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel sum × rev 252d × closeadj
def f29ra_f29_revenue_acceleration_accelsumxrev_252d_jerk_v120_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(252, min_periods=63).sum() * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel sum × rev 504d × closeadj
def f29ra_f29_revenue_acceleration_accelsumxrev_504d_jerk_v121_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(504, min_periods=126).sum() * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × growstd 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxgrowstd_252d_jerk_v122_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g_std = _std(_f29_revenue_growth(revenue, 21), 252)
    base = a * (1.0 + g_std) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × growstd 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxgrowstd_504d_jerk_v123_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g_std = _std(_f29_revenue_growth(revenue, 63), 504)
    base = a * (1.0 + g_std) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel × ncfo lvl 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfolvl_21d_jerk_v124_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a * _mean(ncfo, 21) / 1e8 * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × ncfo lvl 63d × closeadj
def f29ra_f29_revenue_acceleration_accelxncfolvl_63d_jerk_v125_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a * _mean(ncfo, 63) / 1e8 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accel × ebitda lvl 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxebitdalvl_21d_jerk_v126_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a * _mean(ebitda, 21) / 1e8 * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × ebitda lvl 63d × closeadj
def f29ra_f29_revenue_acceleration_accelxebitdalvl_63d_jerk_v127_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a * _mean(ebitda, 63) / 1e8 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × log assets 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxlogassets_252d_jerk_v128_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(assets, 252).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × log assets 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxlogassets_504d_jerk_v129_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(assets, 504).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × log eq 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxlogeq_252d_jerk_v130_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(equity, 252).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × log eq 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxlogeq_504d_jerk_v131_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * np.log(_mean(equity, 504).replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × rev2debt 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxrev2debt_252d_jerk_v132_signal(revenue, debt, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(debt, 252))
    base = a * rat * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × rev2debt 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxrev2debt_504d_jerk_v133_signal(revenue, debt, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(debt, 504))
    base = a * rat * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel cum sign 252d × closeadj
def f29ra_f29_revenue_acceleration_accelcumsign_252d_jerk_v134_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(252, min_periods=63).sum() * _mean(revenue, 252) / 1e9 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel cum sign 504d × closeadj
def f29ra_f29_revenue_acceleration_accelcumsign_504d_jerk_v135_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(504, min_periods=126).sum() * _mean(revenue, 252) / 1e9 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel volvol 21d × closeadj
def f29ra_f29_revenue_acceleration_accelvolvol_21d_jerk_v136_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = _std(_std(a, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel volvol 63d × closeadj
def f29ra_f29_revenue_acceleration_accelvolvol_63d_jerk_v137_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = _std(_std(a, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × rev2cap 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxrev2cap_252d_jerk_v138_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(capex, 252))
    base = a * rat * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × rev2cap 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxrev2cap_504d_jerk_v139_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(capex, 504))
    base = a * rat * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel exp 252d × closeadj
def f29ra_f29_revenue_acceleration_accelexp_252d_jerk_v140_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = np.sign(a) * np.log1p(a.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel exp 504d × closeadj
def f29ra_f29_revenue_acceleration_accelexp_504d_jerk_v141_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = np.sign(a) * np.log1p(a.abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ni stab 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxnistab_252d_jerk_v142_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    nistab = _safe_div(_mean(netinc.abs(), 252), _std(netinc, 252))
    base = a * nistab * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × ni stab 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxnistab_504d_jerk_v143_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    nistab = _safe_div(_mean(netinc.abs(), 504), _std(netinc, 504))
    base = a * nistab * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × activity 21d × closeadj
def f29ra_f29_revenue_acceleration_accelxactivity_21d_jerk_v144_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    activity = _diff(_mean(capex, 21), 21) / _mean(capex.abs(), 21).replace(0, np.nan)
    base = a * (1.0 + activity) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × activity 63d × closeadj
def f29ra_f29_revenue_acceleration_accelxactivity_63d_jerk_v145_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    activity = _diff(_mean(capex, 63), 63) / _mean(capex.abs(), 63).replace(0, np.nan)
    base = a * (1.0 + activity) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × at alt 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxat_alt_252d_jerk_v146_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    at = _safe_div(_mean(revenue, 252), _mean(assets, 252))
    base = a * at * 100.0 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × at alt 504d × closeadj
def f29ra_f29_revenue_acceleration_accelxat_alt_504d_jerk_v147_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    at = _safe_div(_mean(revenue, 252), _mean(assets, 504))
    base = a * at * 100.0 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × cap lvl 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxcaplvl_252d_jerk_v148_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = a * _mean(capex, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × growsq 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxgrowsq_252d_jerk_v149_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    base = a * g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × ema 252d × closeadj
def f29ra_f29_revenue_acceleration_accelxema_252d_jerk_v150_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    ema = a.ewm(span=63, adjust=False, min_periods=21).mean()
    base = a * ema * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29ra_f29_revenue_acceleration_revaccel_21d_jerk_v001_signal,
    f29ra_f29_revenue_acceleration_revaccel_21d_jerk_v002_signal,
    f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v003_signal,
    f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v004_signal,
    f29ra_f29_revenue_acceleration_revaccel_63d_jerk_v005_signal,
    f29ra_f29_revenue_acceleration_revaccel_126d_jerk_v006_signal,
    f29ra_f29_revenue_acceleration_revaccel_126d_jerk_v007_signal,
    f29ra_f29_revenue_acceleration_revaccel_252d_jerk_v008_signal,
    f29ra_f29_revenue_acceleration_revaccel_252d_jerk_v009_signal,
    f29ra_f29_revenue_acceleration_revaccel_504d_jerk_v010_signal,
    f29ra_f29_revenue_acceleration_revaccel_504d_jerk_v011_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_21d_jerk_v012_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_63d_jerk_v013_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_252d_jerk_v014_signal,
    f29ra_f29_revenue_acceleration_revaccelz_252d_jerk_v015_signal,
    f29ra_f29_revenue_acceleration_revaccelz_504d_jerk_v016_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_21d_jerk_v017_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_63d_jerk_v018_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_252d_jerk_v019_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_504d_jerk_v020_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_21d_jerk_v021_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_63d_jerk_v022_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_252d_jerk_v023_signal,
    f29ra_f29_revenue_acceleration_revaccelupcnt_252d_jerk_v024_signal,
    f29ra_f29_revenue_acceleration_revacceldowncnt_504d_jerk_v025_signal,
    f29ra_f29_revenue_acceleration_revaccelabs_252d_jerk_v026_signal,
    f29ra_f29_revenue_acceleration_revaccelabs_504d_jerk_v027_signal,
    f29ra_f29_revenue_acceleration_revaccelema_21d_jerk_v028_signal,
    f29ra_f29_revenue_acceleration_revaccelema_63d_jerk_v029_signal,
    f29ra_f29_revenue_acceleration_revaccelema_252d_jerk_v030_signal,
    f29ra_f29_revenue_acceleration_revaccelstd_252d_jerk_v031_signal,
    f29ra_f29_revenue_acceleration_revaccelstd_504d_jerk_v032_signal,
    f29ra_f29_revenue_acceleration_revaccelsign_252d_jerk_v033_signal,
    f29ra_f29_revenue_acceleration_revaccelsign_504d_jerk_v034_signal,
    f29ra_f29_revenue_acceleration_revaccelultra_5d_jerk_v035_signal,
    f29ra_f29_revenue_acceleration_revaccelshrt_10d_jerk_v036_signal,
    f29ra_f29_revenue_acceleration_revaccelmed_42d_jerk_v037_signal,
    f29ra_f29_revenue_acceleration_revaccellong_189d_jerk_v038_signal,
    f29ra_f29_revenue_acceleration_revaccelvlong_378d_jerk_v039_signal,
    f29ra_f29_revenue_acceleration_accelxgrow_252d_jerk_v040_signal,
    f29ra_f29_revenue_acceleration_accelxgrow_504d_jerk_v041_signal,
    f29ra_f29_revenue_acceleration_accelvsgrow_252d_jerk_v042_signal,
    f29ra_f29_revenue_acceleration_accelvsgrow_504d_jerk_v043_signal,
    f29ra_f29_revenue_acceleration_revjerk_252d_jerk_v044_signal,
    f29ra_f29_revenue_acceleration_revjerk_504d_jerk_v045_signal,
    f29ra_f29_revenue_acceleration_accelxni_252d_jerk_v046_signal,
    f29ra_f29_revenue_acceleration_accelxni_504d_jerk_v047_signal,
    f29ra_f29_revenue_acceleration_accelxfcf_252d_jerk_v048_signal,
    f29ra_f29_revenue_acceleration_accelxfcf_504d_jerk_v049_signal,
    f29ra_f29_revenue_acceleration_accelxebitda_252d_jerk_v050_signal,
    f29ra_f29_revenue_acceleration_accelxebitda_504d_jerk_v051_signal,
    f29ra_f29_revenue_acceleration_accelxgp_252d_jerk_v052_signal,
    f29ra_f29_revenue_acceleration_accelxgp_504d_jerk_v053_signal,
    f29ra_f29_revenue_acceleration_accelpershare_21d_jerk_v054_signal,
    f29ra_f29_revenue_acceleration_accelpershare_63d_jerk_v055_signal,
    f29ra_f29_revenue_acceleration_accelpershare_252d_jerk_v056_signal,
    f29ra_f29_revenue_acceleration_accelratio_63v252_jerk_v057_signal,
    f29ra_f29_revenue_acceleration_accelratio_21v63_jerk_v058_signal,
    f29ra_f29_revenue_acceleration_accelratio_252v504_jerk_v059_signal,
    f29ra_f29_revenue_acceleration_accelsumabs_252d_jerk_v060_signal,
    f29ra_f29_revenue_acceleration_accelsumabs_504d_jerk_v061_signal,
    f29ra_f29_revenue_acceleration_accelcum_252d_jerk_v062_signal,
    f29ra_f29_revenue_acceleration_accelcum_504d_jerk_v063_signal,
    f29ra_f29_revenue_acceleration_accelcv_252d_jerk_v064_signal,
    f29ra_f29_revenue_acceleration_accelcv_504d_jerk_v065_signal,
    f29ra_f29_revenue_acceleration_accelskew_252d_jerk_v066_signal,
    f29ra_f29_revenue_acceleration_accelskew_504d_jerk_v067_signal,
    f29ra_f29_revenue_acceleration_accelkurt_252d_jerk_v068_signal,
    f29ra_f29_revenue_acceleration_accelkurt_504d_jerk_v069_signal,
    f29ra_f29_revenue_acceleration_accelxncfo_252d_jerk_v070_signal,
    f29ra_f29_revenue_acceleration_accelxncfo_504d_jerk_v071_signal,
    f29ra_f29_revenue_acceleration_accelxopinc_252d_jerk_v072_signal,
    f29ra_f29_revenue_acceleration_accelxopinc_504d_jerk_v073_signal,
    f29ra_f29_revenue_acceleration_accelxrevsq_252d_jerk_v074_signal,
    f29ra_f29_revenue_acceleration_accelxrevsq_504d_jerk_v075_signal,
    f29ra_f29_revenue_acceleration_accelxmom_21d_jerk_v076_signal,
    f29ra_f29_revenue_acceleration_accelxmom_63d_jerk_v077_signal,
    f29ra_f29_revenue_acceleration_accelxmom_252d_jerk_v078_signal,
    f29ra_f29_revenue_acceleration_accelplusgrow_252d_jerk_v079_signal,
    f29ra_f29_revenue_acceleration_accelplusgrow_504d_jerk_v080_signal,
    f29ra_f29_revenue_acceleration_accelxmcap_252d_jerk_v081_signal,
    f29ra_f29_revenue_acceleration_accelxmcap_504d_jerk_v082_signal,
    f29ra_f29_revenue_acceleration_accelminusgrow_252d_jerk_v083_signal,
    f29ra_f29_revenue_acceleration_accelminusgrow_504d_jerk_v084_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_21d_jerk_v085_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_63d_jerk_v086_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_252d_jerk_v087_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_504d_jerk_v088_signal,
    f29ra_f29_revenue_acceleration_accelxratrev2ni_252d_jerk_v089_signal,
    f29ra_f29_revenue_acceleration_accelxratrev2ni_504d_jerk_v090_signal,
    f29ra_f29_revenue_acceleration_accelxat_252d_jerk_v091_signal,
    f29ra_f29_revenue_acceleration_accelxat_504d_jerk_v092_signal,
    f29ra_f29_revenue_acceleration_accelxeq_252d_jerk_v093_signal,
    f29ra_f29_revenue_acceleration_accelxeq_504d_jerk_v094_signal,
    f29ra_f29_revenue_acceleration_compaccel_252d_jerk_v095_signal,
    f29ra_f29_revenue_acceleration_compaccel_504d_jerk_v096_signal,
    f29ra_f29_revenue_acceleration_accelxvol_21d_jerk_v097_signal,
    f29ra_f29_revenue_acceleration_accelxvol_63d_jerk_v098_signal,
    f29ra_f29_revenue_acceleration_accelxvol_252d_jerk_v099_signal,
    f29ra_f29_revenue_acceleration_accelxretcum_252d_jerk_v100_signal,
    f29ra_f29_revenue_acceleration_accelxretcum_504d_jerk_v101_signal,
    f29ra_f29_revenue_acceleration_accelxebmargin_252d_jerk_v102_signal,
    f29ra_f29_revenue_acceleration_accelxebmargin_504d_jerk_v103_signal,
    f29ra_f29_revenue_acceleration_accelxrevpershare_21d_jerk_v104_signal,
    f29ra_f29_revenue_acceleration_accelxrevpershare_252d_jerk_v105_signal,
    f29ra_f29_revenue_acceleration_accelarea_252d_jerk_v106_signal,
    f29ra_f29_revenue_acceleration_accelarea_504d_jerk_v107_signal,
    f29ra_f29_revenue_acceleration_accelvsmean_252d_jerk_v108_signal,
    f29ra_f29_revenue_acceleration_accelvsmean_504d_jerk_v109_signal,
    f29ra_f29_revenue_acceleration_accelxnimargin_252d_jerk_v110_signal,
    f29ra_f29_revenue_acceleration_accelxnimargin_504d_jerk_v111_signal,
    f29ra_f29_revenue_acceleration_accelxncfomargin_252d_jerk_v112_signal,
    f29ra_f29_revenue_acceleration_accelxncfomargin_504d_jerk_v113_signal,
    f29ra_f29_revenue_acceleration_accelxleverage_252d_jerk_v114_signal,
    f29ra_f29_revenue_acceleration_accelxleverage_504d_jerk_v115_signal,
    f29ra_f29_revenue_acceleration_accelxcapint_252d_jerk_v116_signal,
    f29ra_f29_revenue_acceleration_accelxcapint_504d_jerk_v117_signal,
    f29ra_f29_revenue_acceleration_accelsum_21d_jerk_v118_signal,
    f29ra_f29_revenue_acceleration_accelsum_63d_jerk_v119_signal,
    f29ra_f29_revenue_acceleration_accelsumxrev_252d_jerk_v120_signal,
    f29ra_f29_revenue_acceleration_accelsumxrev_504d_jerk_v121_signal,
    f29ra_f29_revenue_acceleration_accelxgrowstd_252d_jerk_v122_signal,
    f29ra_f29_revenue_acceleration_accelxgrowstd_504d_jerk_v123_signal,
    f29ra_f29_revenue_acceleration_accelxncfolvl_21d_jerk_v124_signal,
    f29ra_f29_revenue_acceleration_accelxncfolvl_63d_jerk_v125_signal,
    f29ra_f29_revenue_acceleration_accelxebitdalvl_21d_jerk_v126_signal,
    f29ra_f29_revenue_acceleration_accelxebitdalvl_63d_jerk_v127_signal,
    f29ra_f29_revenue_acceleration_accelxlogassets_252d_jerk_v128_signal,
    f29ra_f29_revenue_acceleration_accelxlogassets_504d_jerk_v129_signal,
    f29ra_f29_revenue_acceleration_accelxlogeq_252d_jerk_v130_signal,
    f29ra_f29_revenue_acceleration_accelxlogeq_504d_jerk_v131_signal,
    f29ra_f29_revenue_acceleration_accelxrev2debt_252d_jerk_v132_signal,
    f29ra_f29_revenue_acceleration_accelxrev2debt_504d_jerk_v133_signal,
    f29ra_f29_revenue_acceleration_accelcumsign_252d_jerk_v134_signal,
    f29ra_f29_revenue_acceleration_accelcumsign_504d_jerk_v135_signal,
    f29ra_f29_revenue_acceleration_accelvolvol_21d_jerk_v136_signal,
    f29ra_f29_revenue_acceleration_accelvolvol_63d_jerk_v137_signal,
    f29ra_f29_revenue_acceleration_accelxrev2cap_252d_jerk_v138_signal,
    f29ra_f29_revenue_acceleration_accelxrev2cap_504d_jerk_v139_signal,
    f29ra_f29_revenue_acceleration_accelexp_252d_jerk_v140_signal,
    f29ra_f29_revenue_acceleration_accelexp_504d_jerk_v141_signal,
    f29ra_f29_revenue_acceleration_accelxnistab_252d_jerk_v142_signal,
    f29ra_f29_revenue_acceleration_accelxnistab_504d_jerk_v143_signal,
    f29ra_f29_revenue_acceleration_accelxactivity_21d_jerk_v144_signal,
    f29ra_f29_revenue_acceleration_accelxactivity_63d_jerk_v145_signal,
    f29ra_f29_revenue_acceleration_accelxat_alt_252d_jerk_v146_signal,
    f29ra_f29_revenue_acceleration_accelxat_alt_504d_jerk_v147_signal,
    f29ra_f29_revenue_acceleration_accelxcaplvl_252d_jerk_v148_signal,
    f29ra_f29_revenue_acceleration_accelxgrowsq_252d_jerk_v149_signal,
    f29ra_f29_revenue_acceleration_accelxema_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_REVENUE_ACCELERATION_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_revenue_accel", "_f29_revenue_growth", "_f29_revenue_jerk")
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
    print(f"OK f29_revenue_acceleration_3rd_derivatives_001_150_claude: {n_features} features pass")
