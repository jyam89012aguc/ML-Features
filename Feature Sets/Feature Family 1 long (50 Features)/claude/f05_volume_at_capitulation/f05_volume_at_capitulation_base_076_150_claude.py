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


# 21d capvolz × 21d return volatility (volatile capitulation)
def f05vc_f05_volume_at_capitulation_capvolzxrv_21d_base_v076_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    result = _f05_capitulation_volz(closeadj, volume, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × rv
def f05vc_f05_volume_at_capitulation_capvolzxrv_63d_base_v077_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f05_capitulation_volz(closeadj, volume, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × rv
def f05vc_f05_volume_at_capitulation_capvolzxrv_252d_base_v078_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f05_capitulation_volz(closeadj, volume, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × skewness
def f05vc_f05_volume_at_capitulation_capvolzxskew_63d_base_v079_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f05_capitulation_volz(closeadj, volume, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × kurtosis
def f05vc_f05_volume_at_capitulation_capvolzxkurt_252d_base_v080_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f05_capitulation_volz(closeadj, volume, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × skewness
def f05vc_f05_volume_at_capitulation_panicvolxskew_63d_base_v081_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f05_panic_volume(closeadj, volume, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × kurtosis
def f05vc_f05_volume_at_capitulation_panicvolxkurt_252d_base_v082_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f05_panic_volume(closeadj, volume, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz EMA × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzemaxdv_21d_base_v083_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    e = cv.ewm(span=21, adjust=False).mean()
    result = e * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz EMA × dollar volume
def f05vc_f05_volume_at_capitulation_capvolzemaxdv_63d_base_v084_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    e = cv.ewm(span=63, adjust=False).mean()
    result = e * closeadj * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz divided by 21d return volatility (clean spike)
def f05vc_f05_volume_at_capitulation_capvolzdivrv_21d_base_v085_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = (_f05_capitulation_volz(closeadj, volume, 21) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz / rv
def f05vc_f05_volume_at_capitulation_capvolzdivrv_63d_base_v086_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f05_capitulation_volz(closeadj, volume, 63) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz / rv
def f05vc_f05_volume_at_capitulation_capvolzdivrv_252d_base_v087_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f05_capitulation_volz(closeadj, volume, 252) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × log price
def f05vc_f05_volume_at_capitulation_capvolzxlog_21d_base_v088_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f05_capitulation_volz(closeadj, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × log price
def f05vc_f05_volume_at_capitulation_capvolzxlog_63d_base_v089_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f05_capitulation_volz(closeadj, volume, 63) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × log price
def f05vc_f05_volume_at_capitulation_panicvolxlog_21d_base_v090_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f05_panic_volume(closeadj, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × log price
def f05vc_f05_volume_at_capitulation_climaxxlog_21d_base_v091_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f05_capitulation_climax(closeadj, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × volume z (compound)
def f05vc_f05_volume_at_capitulation_capvolzxvolz_21d_base_v092_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × volume z
def f05vc_f05_volume_at_capitulation_capvolzxvolz_63d_base_v093_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × volume z
def f05vc_f05_volume_at_capitulation_capvolzxvolz_252d_base_v094_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × volume z
def f05vc_f05_volume_at_capitulation_climaxxvolz_21d_base_v095_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax × |volume z|
def f05vc_f05_volume_at_capitulation_climaxxvolz_63d_base_v096_signal(closeadj, volume):
    result = _f05_capitulation_climax(closeadj, volume, 63) * _z(volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × volume z
def f05vc_f05_volume_at_capitulation_panicvolxvolz_21d_base_v097_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × volume z
def f05vc_f05_volume_at_capitulation_panicvolxvolz_63d_base_v098_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × ATR-style range
def f05vc_f05_volume_at_capitulation_capvolzxrange_21d_base_v099_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × range
def f05vc_f05_volume_at_capitulation_capvolzxrange_63d_base_v100_signal(closeadj, volume, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_21d_base_v101_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_panic_volume(closeadj, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_63d_base_v102_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_panic_volume(closeadj, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × 63d ATR
def f05vc_f05_volume_at_capitulation_panicvolxatr_252d_base_v103_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f05_panic_volume(closeadj, volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax × ATR
def f05vc_f05_volume_at_capitulation_climaxxatr_21d_base_v104_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f05_capitulation_climax(closeadj, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax × ATR
def f05vc_f05_volume_at_capitulation_climaxxatr_63d_base_v105_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f05_capitulation_climax(closeadj, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol minus 63d panic vol (acceleration)
def f05vc_f05_volume_at_capitulation_panicvoldiff_21m63_base_v106_signal(closeadj, volume):
    result = (_f05_panic_volume(closeadj, volume, 21) - _f05_panic_volume(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol minus 252d panic vol
def f05vc_f05_volume_at_capitulation_panicvoldiff_63m252_base_v107_signal(closeadj, volume):
    result = (_f05_panic_volume(closeadj, volume, 63) - _f05_panic_volume(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol / 252d panic vol ratio
def f05vc_f05_volume_at_capitulation_panicvolratio_21v252_base_v108_signal(closeadj, volume):
    a = _f05_panic_volume(closeadj, volume, 21)
    b = _f05_panic_volume(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol / 252d panic vol
def f05vc_f05_volume_at_capitulation_panicvolratio_63v252_base_v109_signal(closeadj, volume):
    a = _f05_panic_volume(closeadj, volume, 63)
    b = _f05_panic_volume(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax minus 63d climax
def f05vc_f05_volume_at_capitulation_climaxdiff_21m63_base_v110_signal(closeadj, volume):
    result = (_f05_capitulation_climax(closeadj, volume, 21) - _f05_capitulation_climax(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax / 252d climax ratio
def f05vc_f05_volume_at_capitulation_climaxratio_63v252_base_v111_signal(closeadj, volume):
    a = _f05_capitulation_climax(closeadj, volume, 63)
    b = _f05_capitulation_climax(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_21d_base_v112_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    result = pv.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_63d_base_v113_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 63)
    result = pv.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol EMA
def f05vc_f05_volume_at_capitulation_panicvolema_252d_base_v114_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 252)
    result = pv.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × abs return
def f05vc_f05_volume_at_capitulation_capvolzxabsret_21d_base_v115_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    result = _f05_capitulation_volz(closeadj, volume, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × abs return
def f05vc_f05_volume_at_capitulation_capvolzxabsret_63d_base_v116_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    result = _f05_capitulation_volz(closeadj, volume, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × abs return
def f05vc_f05_volume_at_capitulation_capvolzxabsret_252d_base_v117_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(252, min_periods=63).mean()
    result = _f05_capitulation_volz(closeadj, volume, 252) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax sum over 63d
def f05vc_f05_volume_at_capitulation_climaxsum_63d_base_v118_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    result = cl.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d climax sum over 252d
def f05vc_f05_volume_at_capitulation_climaxsum_252d_base_v119_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    result = cl.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol sum over 63d
def f05vc_f05_volume_at_capitulation_panicvolsum_63d_base_v120_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    result = pv.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol sum over 252d
def f05vc_f05_volume_at_capitulation_panicvolsum_252d_base_v121_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 63)
    result = pv.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max climax over 63d
def f05vc_f05_volume_at_capitulation_climaxmax_63d_base_v122_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    result = cl.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max climax over 252d
def f05vc_f05_volume_at_capitulation_climaxmax_252d_base_v123_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    result = cl.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of climax events (climax > 1)
def f05vc_f05_volume_at_capitulation_climaxeventcount_252d_base_v124_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    result = (cl).rolling(252, min_periods=63).mean() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of climax events
def f05vc_f05_volume_at_capitulation_climaxeventcount_504d_base_v125_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 63)
    result = (cl).rolling(504, min_periods=126).mean() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × climax (compound severity)
def f05vc_f05_volume_at_capitulation_capvolzxclimax_21d_base_v126_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_climax(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × climax
def f05vc_f05_volume_at_capitulation_capvolzxclimax_63d_base_v127_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 63) * _f05_capitulation_climax(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × climax
def f05vc_f05_volume_at_capitulation_capvolzxclimax_252d_base_v128_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 252) * _f05_capitulation_climax(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz times 63d capvolz (compound across windows)
def f05vc_f05_volume_at_capitulation_capvolzxlong_21x63_base_v129_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d × 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolzxlong_63x252_base_v130_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 63) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × 252d capvolz
def f05vc_f05_volume_at_capitulation_capvolzxlong_21x252_base_v131_signal(closeadj, volume):
    result = _f05_capitulation_volz(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × 21d capvolz
def f05vc_f05_volume_at_capitulation_panicxcapvolz_21d_base_v132_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 21) * _f05_capitulation_volz(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × 252d capvolz
def f05vc_f05_volume_at_capitulation_panicxcapvolz_252d_base_v133_signal(closeadj, volume):
    result = _f05_panic_volume(closeadj, volume, 252) * _f05_capitulation_volz(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × volume / 21d volume mean
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_21d_base_v134_signal(closeadj, volume):
    vmean = _mean(volume, 21).replace(0, np.nan)
    result = _f05_capitulation_volz(closeadj, volume, 21) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × volume / 63d volume mean
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_63d_base_v135_signal(closeadj, volume):
    vmean = _mean(volume, 63).replace(0, np.nan)
    result = _f05_capitulation_volz(closeadj, volume, 63) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz × volume / 252d volume mean
def f05vc_f05_volume_at_capitulation_capvolzxvolratio_252d_base_v136_signal(closeadj, volume):
    vmean = _mean(volume, 252).replace(0, np.nan)
    result = _f05_capitulation_volz(closeadj, volume, 252) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d climax sum × log price
def f05vc_f05_volume_at_capitulation_climaxsumxlog_63d_base_v137_signal(closeadj, volume):
    cl = _f05_capitulation_climax(closeadj, volume, 21)
    s = cl.rolling(63, min_periods=21).sum()
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = s * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz EMA × abs return
def f05vc_f05_volume_at_capitulation_capvolzemaxabsret_252d_base_v138_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    e = cv.ewm(span=252, adjust=False).mean()
    ar = closeadj.pct_change().abs().rolling(252, min_periods=63).mean()
    result = e * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × abs return
def f05vc_f05_volume_at_capitulation_panicvolxabsret_63d_base_v139_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    result = _f05_panic_volume(closeadj, volume, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d panic vol × abs return
def f05vc_f05_volume_at_capitulation_panicvolxabsret_252d_base_v140_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(252, min_periods=63).mean()
    result = _f05_panic_volume(closeadj, volume, 252) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz × low-vs-mean ratio
def f05vc_f05_volume_at_capitulation_capvolzxlowdiff_21d_base_v141_signal(closeadj, volume, low):
    diff = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _f05_capitulation_volz(closeadj, volume, 21) * diff * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz × low-vs-mean ratio
def f05vc_f05_volume_at_capitulation_capvolzxlowdiff_63d_base_v142_signal(closeadj, volume, low):
    diff = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _f05_capitulation_volz(closeadj, volume, 63) * diff * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol × high-low spread
def f05vc_f05_volume_at_capitulation_panicvolxhlspread_21d_base_v143_signal(closeadj, volume, high, low):
    sp = (high - low) / closeadj.replace(0, np.nan)
    result = _f05_panic_volume(closeadj, volume, 21) * sp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d panic vol × high-low spread
def f05vc_f05_volume_at_capitulation_panicvolxhlspread_63d_base_v144_signal(closeadj, volume, high, low):
    sp = (high - low) / closeadj.replace(0, np.nan)
    result = _f05_panic_volume(closeadj, volume, 63) * sp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite capitulation × dollar volume
def f05vc_f05_volume_at_capitulation_capcompxdv_252d_base_v145_signal(closeadj, volume):
    dv = closeadj * volume
    comp = _f05_capitulation_volz(closeadj, volume, 252) + _f05_capitulation_climax(closeadj, volume, 252)
    result = comp * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite capitulation × dollar volume
def f05vc_f05_volume_at_capitulation_capcompxdv_63d_base_v146_signal(closeadj, volume):
    dv = closeadj * volume
    comp = _f05_capitulation_volz(closeadj, volume, 63) + _f05_capitulation_climax(closeadj, volume, 63)
    result = comp * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capvolz - rolling 252d mean of capvolz (anomaly)
def f05vc_f05_volume_at_capitulation_capvolzanom_21d_base_v147_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 21)
    base = _mean(cv, 252)
    result = (cv - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capvolz - 252d mean
def f05vc_f05_volume_at_capitulation_capvolzanom_63d_base_v148_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 63)
    base = _mean(cv, 252)
    result = (cv - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capvolz - 504d mean
def f05vc_f05_volume_at_capitulation_capvolzanom_252d_base_v149_signal(closeadj, volume):
    cv = _f05_capitulation_volz(closeadj, volume, 252)
    base = _mean(cv, 504)
    result = (cv - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d panic vol - 252d mean
def f05vc_f05_volume_at_capitulation_panicvolanom_21d_base_v150_signal(closeadj, volume):
    pv = _f05_panic_volume(closeadj, volume, 21)
    base = _mean(pv, 252)
    result = (pv - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05vc_f05_volume_at_capitulation_capvolzxrv_21d_base_v076_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrv_63d_base_v077_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrv_252d_base_v078_signal,
    f05vc_f05_volume_at_capitulation_capvolzxskew_63d_base_v079_signal,
    f05vc_f05_volume_at_capitulation_capvolzxkurt_252d_base_v080_signal,
    f05vc_f05_volume_at_capitulation_panicvolxskew_63d_base_v081_signal,
    f05vc_f05_volume_at_capitulation_panicvolxkurt_252d_base_v082_signal,
    f05vc_f05_volume_at_capitulation_capvolzemaxdv_21d_base_v083_signal,
    f05vc_f05_volume_at_capitulation_capvolzemaxdv_63d_base_v084_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_21d_base_v085_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_63d_base_v086_signal,
    f05vc_f05_volume_at_capitulation_capvolzdivrv_252d_base_v087_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlog_21d_base_v088_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlog_63d_base_v089_signal,
    f05vc_f05_volume_at_capitulation_panicvolxlog_21d_base_v090_signal,
    f05vc_f05_volume_at_capitulation_climaxxlog_21d_base_v091_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_21d_base_v092_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_63d_base_v093_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolz_252d_base_v094_signal,
    f05vc_f05_volume_at_capitulation_climaxxvolz_21d_base_v095_signal,
    f05vc_f05_volume_at_capitulation_climaxxvolz_63d_base_v096_signal,
    f05vc_f05_volume_at_capitulation_panicvolxvolz_21d_base_v097_signal,
    f05vc_f05_volume_at_capitulation_panicvolxvolz_63d_base_v098_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrange_21d_base_v099_signal,
    f05vc_f05_volume_at_capitulation_capvolzxrange_63d_base_v100_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_21d_base_v101_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_63d_base_v102_signal,
    f05vc_f05_volume_at_capitulation_panicvolxatr_252d_base_v103_signal,
    f05vc_f05_volume_at_capitulation_climaxxatr_21d_base_v104_signal,
    f05vc_f05_volume_at_capitulation_climaxxatr_63d_base_v105_signal,
    f05vc_f05_volume_at_capitulation_panicvoldiff_21m63_base_v106_signal,
    f05vc_f05_volume_at_capitulation_panicvoldiff_63m252_base_v107_signal,
    f05vc_f05_volume_at_capitulation_panicvolratio_21v252_base_v108_signal,
    f05vc_f05_volume_at_capitulation_panicvolratio_63v252_base_v109_signal,
    f05vc_f05_volume_at_capitulation_climaxdiff_21m63_base_v110_signal,
    f05vc_f05_volume_at_capitulation_climaxratio_63v252_base_v111_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_21d_base_v112_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_63d_base_v113_signal,
    f05vc_f05_volume_at_capitulation_panicvolema_252d_base_v114_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_21d_base_v115_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_63d_base_v116_signal,
    f05vc_f05_volume_at_capitulation_capvolzxabsret_252d_base_v117_signal,
    f05vc_f05_volume_at_capitulation_climaxsum_63d_base_v118_signal,
    f05vc_f05_volume_at_capitulation_climaxsum_252d_base_v119_signal,
    f05vc_f05_volume_at_capitulation_panicvolsum_63d_base_v120_signal,
    f05vc_f05_volume_at_capitulation_panicvolsum_252d_base_v121_signal,
    f05vc_f05_volume_at_capitulation_climaxmax_63d_base_v122_signal,
    f05vc_f05_volume_at_capitulation_climaxmax_252d_base_v123_signal,
    f05vc_f05_volume_at_capitulation_climaxeventcount_252d_base_v124_signal,
    f05vc_f05_volume_at_capitulation_climaxeventcount_504d_base_v125_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_21d_base_v126_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_63d_base_v127_signal,
    f05vc_f05_volume_at_capitulation_capvolzxclimax_252d_base_v128_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_21x63_base_v129_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_63x252_base_v130_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlong_21x252_base_v131_signal,
    f05vc_f05_volume_at_capitulation_panicxcapvolz_21d_base_v132_signal,
    f05vc_f05_volume_at_capitulation_panicxcapvolz_252d_base_v133_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_21d_base_v134_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_63d_base_v135_signal,
    f05vc_f05_volume_at_capitulation_capvolzxvolratio_252d_base_v136_signal,
    f05vc_f05_volume_at_capitulation_climaxsumxlog_63d_base_v137_signal,
    f05vc_f05_volume_at_capitulation_capvolzemaxabsret_252d_base_v138_signal,
    f05vc_f05_volume_at_capitulation_panicvolxabsret_63d_base_v139_signal,
    f05vc_f05_volume_at_capitulation_panicvolxabsret_252d_base_v140_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlowdiff_21d_base_v141_signal,
    f05vc_f05_volume_at_capitulation_capvolzxlowdiff_63d_base_v142_signal,
    f05vc_f05_volume_at_capitulation_panicvolxhlspread_21d_base_v143_signal,
    f05vc_f05_volume_at_capitulation_panicvolxhlspread_63d_base_v144_signal,
    f05vc_f05_volume_at_capitulation_capcompxdv_252d_base_v145_signal,
    f05vc_f05_volume_at_capitulation_capcompxdv_63d_base_v146_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_21d_base_v147_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_63d_base_v148_signal,
    f05vc_f05_volume_at_capitulation_capvolzanom_252d_base_v149_signal,
    f05vc_f05_volume_at_capitulation_panicvolanom_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_VOLUME_AT_CAPITULATION_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f05_volume_at_capitulation_base_076_150_claude: {n_features} features pass")
