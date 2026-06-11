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
def _f01_peak_level(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).max()


def _f01_drawdown_from_peak(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - peak) / peak.replace(0, np.nan).abs()


def _f01_crash_intensity(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = (close - peak) / peak.replace(0, np.nan).abs()
    rng = (close.rolling(w, min_periods=max(1, w // 2)).max()
           - close.rolling(w, min_periods=max(1, w // 2)).min())
    return dd * close / rng.replace(0, np.nan)


# 21d EMA of drawdown × close
def f01pc_f01_peak_and_crash_ddema_21d_base_v076_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    result = d.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of drawdown × close
def f01pc_f01_peak_and_crash_ddema_63d_base_v077_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    result = d.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of drawdown × close
def f01pc_f01_peak_and_crash_ddema_252d_base_v078_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    result = d.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak level EMA × close
def f01pc_f01_peak_and_crash_peakema_21d_base_v079_signal(closeadj):
    pk = _f01_peak_level(closeadj, 21)
    result = pk.ewm(span=21, adjust=False).mean() - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak level EMA × close
def f01pc_f01_peak_and_crash_peakema_63d_base_v080_signal(closeadj):
    pk = _f01_peak_level(closeadj, 63)
    result = pk.ewm(span=63, adjust=False).mean() - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak level EMA × close
def f01pc_f01_peak_and_crash_peakema_252d_base_v081_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    result = pk.ewm(span=252, adjust=False).mean() - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d minimum drawdown over 63d window (worst-recent crash)
def f01pc_f01_peak_and_crash_worstdd_63d_base_v082_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    result = d.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minimum drawdown over 252d window
def f01pc_f01_peak_and_crash_worstdd_252d_base_v083_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    result = d.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d minimum drawdown over 504d window
def f01pc_f01_peak_and_crash_worstdd_504d_base_v084_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    result = d.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown × 21d return-volatility
def f01pc_f01_peak_and_crash_ddxretvol_21d_base_v085_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f01_drawdown_from_peak(closeadj, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown × 21d return-volatility
def f01pc_f01_peak_and_crash_ddxretvol_63d_base_v086_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f01_drawdown_from_peak(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × 63d return-volatility
def f01pc_f01_peak_and_crash_ddxretvol_252d_base_v087_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f01_drawdown_from_peak(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown × skew of returns
def f01pc_f01_peak_and_crash_ddxskew_63d_base_v088_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f01_drawdown_from_peak(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × skew of returns
def f01pc_f01_peak_and_crash_ddxskew_252d_base_v089_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f01_drawdown_from_peak(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown × kurt of returns
def f01pc_f01_peak_and_crash_ddxkurt_63d_base_v090_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f01_drawdown_from_peak(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × kurt of returns
def f01pc_f01_peak_and_crash_ddxkurt_252d_base_v091_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f01_drawdown_from_peak(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown ratio: 63d / 252d
def f01pc_f01_peak_and_crash_ddratio_63v252_base_v092_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 63)
    b = _f01_drawdown_from_peak(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown ratio: 21d / 63d
def f01pc_f01_peak_and_crash_ddratio_21v63_base_v093_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 21)
    b = _f01_drawdown_from_peak(closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown ratio: 252d / 504d
def f01pc_f01_peak_and_crash_ddratio_252v504_base_v094_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 252)
    b = _f01_drawdown_from_peak(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown minus 252d drawdown (acceleration)
def f01pc_f01_peak_and_crash_dddiff_63m252_base_v095_signal(closeadj):
    result = (_f01_drawdown_from_peak(closeadj, 63) - _f01_drawdown_from_peak(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown minus 63d drawdown
def f01pc_f01_peak_and_crash_dddiff_21m63_base_v096_signal(closeadj):
    result = (_f01_drawdown_from_peak(closeadj, 21) - _f01_drawdown_from_peak(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown minus 504d drawdown
def f01pc_f01_peak_and_crash_dddiff_252m504_base_v097_signal(closeadj):
    result = (_f01_drawdown_from_peak(closeadj, 252) - _f01_drawdown_from_peak(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak level diff: peak 63d - peak 252d (peak erosion gap)
def f01pc_f01_peak_and_crash_peakdiff_63m252_base_v098_signal(closeadj):
    result = (_f01_peak_level(closeadj, 63) - _f01_peak_level(closeadj, 252)) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak level diff: peak 252d - peak 504d
def f01pc_f01_peak_and_crash_peakdiff_252m504_base_v099_signal(closeadj):
    result = (_f01_peak_level(closeadj, 252) - _f01_peak_level(closeadj, 504)) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d post-crash drift count: days remaining below recent peak
def f01pc_f01_peak_and_crash_belowpeak_21d_base_v100_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    flag = (closeadj < peak).astype(float)
    result = flag.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d post-crash drift count
def f01pc_f01_peak_and_crash_belowpeak_63d_base_v101_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    flag = (closeadj < peak).astype(float)
    result = flag.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d post-crash drift count
def f01pc_f01_peak_and_crash_belowpeak_252d_base_v102_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    flag = (closeadj < peak).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d post-crash drift count
def f01pc_f01_peak_and_crash_belowpeak_504d_base_v103_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    flag = (closeadj < peak).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of deeply-below-peak days (below -10%)
def f01pc_f01_peak_and_crash_deepbelowpeak_252d_base_v104_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 252) < -0.10).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of deeply-below-peak days (below -20%)
def f01pc_f01_peak_and_crash_deepbelowpeak_504d_base_v105_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 252) < -0.20).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of mini-crashes (below -5%)
def f01pc_f01_peak_and_crash_deepbelowpeak_63d_base_v106_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 63) < -0.05).astype(float)
    result = flag.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash intensity × 5d return (sentiment after crash)
def f01pc_f01_peak_and_crash_intensxret_21d_base_v107_signal(closeadj):
    r = closeadj.pct_change(5)
    result = _f01_crash_intensity(closeadj, 21) * r
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash intensity × 21d return
def f01pc_f01_peak_and_crash_intensxret_63d_base_v108_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f01_crash_intensity(closeadj, 63) * r
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash intensity × 63d return
def f01pc_f01_peak_and_crash_intensxret_252d_base_v109_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f01_crash_intensity(closeadj, 252) * r
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak-distance: 21d peak ÷ close × close
def f01pc_f01_peak_and_crash_peakdist_21d_base_v110_signal(closeadj):
    pk = _f01_peak_level(closeadj, 21)
    result = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak-distance × peak
def f01pc_f01_peak_and_crash_peakdist_63d_base_v111_signal(closeadj):
    pk = _f01_peak_level(closeadj, 63)
    result = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak-distance × peak
def f01pc_f01_peak_and_crash_peakdist_252d_base_v112_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    result = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d peak-distance × peak
def f01pc_f01_peak_and_crash_peakdist_504d_base_v113_signal(closeadj):
    pk = _f01_peak_level(closeadj, 504)
    result = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_21d_base_v114_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f01_crash_intensity(closeadj, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_63d_base_v115_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f01_crash_intensity(closeadj, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_252d_base_v116_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f01_crash_intensity(closeadj, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash intensity × downside dollar volume
def f01pc_f01_peak_and_crash_intensxdownvol_21d_base_v117_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f01_crash_intensity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash intensity × downside dollar volume
def f01pc_f01_peak_and_crash_intensxdownvol_63d_base_v118_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f01_crash_intensity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash intensity × downside dollar volume
def f01pc_f01_peak_and_crash_intensxdownvol_252d_base_v119_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f01_crash_intensity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst-ever drawdown × close
def f01pc_f01_peak_and_crash_ddworstever_base_v120_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 504)
    result = d.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown gap to expanding worst-ever
def f01pc_f01_peak_and_crash_ddvshistworst_252d_base_v121_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    worst = d.expanding(min_periods=63).min()
    result = (d - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown gap to expanding worst-ever
def f01pc_f01_peak_and_crash_ddvshistworst_504d_base_v122_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 504)
    worst = d.expanding(min_periods=252).min()
    result = (d - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash count × peak-age (severity-time)
def f01pc_f01_peak_and_crash_crashcountxage_252d_base_v123_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    cnt = cross.rolling(252, min_periods=63).sum()
    result = (cnt + 1.0) * age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash event area: sum of below-peak deficit
def f01pc_f01_peak_and_crash_crasharea_63d_base_v124_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 63)).clip(lower=0)
    result = deficit.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash event area
def f01pc_f01_peak_and_crash_crasharea_252d_base_v125_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 252)).clip(lower=0)
    result = deficit.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash event area
def f01pc_f01_peak_and_crash_crasharea_504d_base_v126_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 504)).clip(lower=0)
    result = deficit.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d high vs 252d peak gap
def f01pc_f01_peak_and_crash_localpeakgap_21d_base_v127_signal(closeadj, high):
    local_pk = high.rolling(21, min_periods=5).max()
    big_pk = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    result = (local_pk - big_pk) * closeadj / big_pk.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d high vs 504d peak gap
def f01pc_f01_peak_and_crash_localpeakgap_63d_base_v128_signal(closeadj, high):
    local_pk = high.rolling(63, min_periods=21).max()
    big_pk = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    result = (local_pk - big_pk) * closeadj / big_pk.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d low vs 252d peak (depth from peak via low)
def f01pc_f01_peak_and_crash_lowdistpeak_21d_base_v129_signal(closeadj, low):
    big_pk = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    local_lo = low.rolling(21, min_periods=5).min()
    result = (local_lo - big_pk) * closeadj / big_pk.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d low vs 504d peak
def f01pc_f01_peak_and_crash_lowdistpeak_63d_base_v130_signal(closeadj, low):
    big_pk = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    local_lo = low.rolling(63, min_periods=21).min()
    result = (local_lo - big_pk) * closeadj / big_pk.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash sharpness × volume z (panic-event)
def f01pc_f01_peak_and_crash_sharpxvolz_21d_base_v131_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 21).abs()
    peak = _f01_peak_level(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash sharpness × volume z
def f01pc_f01_peak_and_crash_sharpxvolz_63d_base_v132_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 63).abs()
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d new-peak count × close (peak-frequency)
def f01pc_f01_peak_and_crash_newpeakfreq_21d_base_v133_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    new_peak = (closeadj >= peak).astype(float)
    result = new_peak.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d new-peak count
def f01pc_f01_peak_and_crash_newpeakfreq_504d_base_v134_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    result = new_peak.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d new-peak ratio: count / window
def f01pc_f01_peak_and_crash_newpeakrate_63d_base_v135_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    new_peak = (closeadj >= peak).astype(float)
    result = (new_peak.rolling(63, min_periods=21).sum() / 63.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d new-peak ratio
def f01pc_f01_peak_and_crash_newpeakrate_252d_base_v136_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    result = (new_peak.rolling(252, min_periods=63).sum() / 252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATH proximity × volume z
def f01pc_f01_peak_and_crash_athproxxvolz_21d_base_v137_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    prox = closeadj / ath
    result = prox * _z(volume, 21) * closeadj + _f01_peak_level(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATH proximity × volume z
def f01pc_f01_peak_and_crash_athproxxvolz_63d_base_v138_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    prox = closeadj / ath
    result = prox * _z(volume, 63) * closeadj + _f01_peak_level(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × range (volatile-deep crash)
def f01pc_f01_peak_and_crash_ddxrange_252d_base_v139_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f01_drawdown_from_peak(closeadj, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown × range
def f01pc_f01_peak_and_crash_ddxrange_63d_base_v140_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f01_drawdown_from_peak(closeadj, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash sharpness × dollar volume
def f01pc_f01_peak_and_crash_sharpxdv_252d_base_v141_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    dv = closeadj * volume
    result = (dd / age) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d post-peak retreat: 63d forward return weighted by proximity-to-peak
def f01pc_f01_peak_and_crash_postpeakdrop_63d_base_v142_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    proximity = closeadj / peak.replace(0, np.nan).abs()
    fwd = closeadj.shift(-63) / closeadj - 1.0
    result = proximity * fwd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d post-peak retreat: 126d forward return weighted by proximity-to-peak
def f01pc_f01_peak_and_crash_postpeakdrop_252d_base_v143_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    proximity = closeadj / peak.replace(0, np.nan).abs()
    fwd = closeadj.shift(-126) / closeadj - 1.0
    result = proximity * fwd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash count × volume
def f01pc_f01_peak_and_crash_crashcountxvol_252d_base_v144_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    cnt = cross.rolling(252, min_periods=63).sum()
    result = (cnt + 1.0) * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash count × dollar volume
def f01pc_f01_peak_and_crash_crashcountxdv_504d_base_v145_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 252)
    cross = ((dd < -0.15) & (dd.shift(1) >= -0.15)).astype(float)
    cnt = cross.rolling(504, min_periods=126).sum()
    result = (cnt + 1.0) * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown × current dollar-volume (crash-pressure)
def f01pc_f01_peak_and_crash_ddxcurdv_21d_base_v146_signal(closeadj, volume):
    result = _f01_drawdown_from_peak(closeadj, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × current dollar-volume
def f01pc_f01_peak_and_crash_ddxcurdv_252d_base_v147_signal(closeadj, volume):
    result = _f01_drawdown_from_peak(closeadj, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# composite peak-and-crash severity at 252d
def f01pc_f01_peak_and_crash_compositesev_252d_base_v148_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= pk).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    result = (dd + age / 252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite peak-and-crash severity at 504d
def f01pc_f01_peak_and_crash_compositesev_504d_base_v149_signal(closeadj):
    pk = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= pk).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 504).abs()
    result = (dd + age / 504.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite peak-and-crash intensity-area
def f01pc_f01_peak_and_crash_intensarea_252d_base_v150_signal(closeadj):
    inten = _f01_crash_intensity(closeadj, 63).abs()
    result = inten.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01pc_f01_peak_and_crash_ddema_21d_base_v076_signal,
    f01pc_f01_peak_and_crash_ddema_63d_base_v077_signal,
    f01pc_f01_peak_and_crash_ddema_252d_base_v078_signal,
    f01pc_f01_peak_and_crash_peakema_21d_base_v079_signal,
    f01pc_f01_peak_and_crash_peakema_63d_base_v080_signal,
    f01pc_f01_peak_and_crash_peakema_252d_base_v081_signal,
    f01pc_f01_peak_and_crash_worstdd_63d_base_v082_signal,
    f01pc_f01_peak_and_crash_worstdd_252d_base_v083_signal,
    f01pc_f01_peak_and_crash_worstdd_504d_base_v084_signal,
    f01pc_f01_peak_and_crash_ddxretvol_21d_base_v085_signal,
    f01pc_f01_peak_and_crash_ddxretvol_63d_base_v086_signal,
    f01pc_f01_peak_and_crash_ddxretvol_252d_base_v087_signal,
    f01pc_f01_peak_and_crash_ddxskew_63d_base_v088_signal,
    f01pc_f01_peak_and_crash_ddxskew_252d_base_v089_signal,
    f01pc_f01_peak_and_crash_ddxkurt_63d_base_v090_signal,
    f01pc_f01_peak_and_crash_ddxkurt_252d_base_v091_signal,
    f01pc_f01_peak_and_crash_ddratio_63v252_base_v092_signal,
    f01pc_f01_peak_and_crash_ddratio_21v63_base_v093_signal,
    f01pc_f01_peak_and_crash_ddratio_252v504_base_v094_signal,
    f01pc_f01_peak_and_crash_dddiff_63m252_base_v095_signal,
    f01pc_f01_peak_and_crash_dddiff_21m63_base_v096_signal,
    f01pc_f01_peak_and_crash_dddiff_252m504_base_v097_signal,
    f01pc_f01_peak_and_crash_peakdiff_63m252_base_v098_signal,
    f01pc_f01_peak_and_crash_peakdiff_252m504_base_v099_signal,
    f01pc_f01_peak_and_crash_belowpeak_21d_base_v100_signal,
    f01pc_f01_peak_and_crash_belowpeak_63d_base_v101_signal,
    f01pc_f01_peak_and_crash_belowpeak_252d_base_v102_signal,
    f01pc_f01_peak_and_crash_belowpeak_504d_base_v103_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_252d_base_v104_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_504d_base_v105_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_63d_base_v106_signal,
    f01pc_f01_peak_and_crash_intensxret_21d_base_v107_signal,
    f01pc_f01_peak_and_crash_intensxret_63d_base_v108_signal,
    f01pc_f01_peak_and_crash_intensxret_252d_base_v109_signal,
    f01pc_f01_peak_and_crash_peakdist_21d_base_v110_signal,
    f01pc_f01_peak_and_crash_peakdist_63d_base_v111_signal,
    f01pc_f01_peak_and_crash_peakdist_252d_base_v112_signal,
    f01pc_f01_peak_and_crash_peakdist_504d_base_v113_signal,
    f01pc_f01_peak_and_crash_intensxatr_21d_base_v114_signal,
    f01pc_f01_peak_and_crash_intensxatr_63d_base_v115_signal,
    f01pc_f01_peak_and_crash_intensxatr_252d_base_v116_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_21d_base_v117_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_63d_base_v118_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_252d_base_v119_signal,
    f01pc_f01_peak_and_crash_ddworstever_base_v120_signal,
    f01pc_f01_peak_and_crash_ddvshistworst_252d_base_v121_signal,
    f01pc_f01_peak_and_crash_ddvshistworst_504d_base_v122_signal,
    f01pc_f01_peak_and_crash_crashcountxage_252d_base_v123_signal,
    f01pc_f01_peak_and_crash_crasharea_63d_base_v124_signal,
    f01pc_f01_peak_and_crash_crasharea_252d_base_v125_signal,
    f01pc_f01_peak_and_crash_crasharea_504d_base_v126_signal,
    f01pc_f01_peak_and_crash_localpeakgap_21d_base_v127_signal,
    f01pc_f01_peak_and_crash_localpeakgap_63d_base_v128_signal,
    f01pc_f01_peak_and_crash_lowdistpeak_21d_base_v129_signal,
    f01pc_f01_peak_and_crash_lowdistpeak_63d_base_v130_signal,
    f01pc_f01_peak_and_crash_sharpxvolz_21d_base_v131_signal,
    f01pc_f01_peak_and_crash_sharpxvolz_63d_base_v132_signal,
    f01pc_f01_peak_and_crash_newpeakfreq_21d_base_v133_signal,
    f01pc_f01_peak_and_crash_newpeakfreq_504d_base_v134_signal,
    f01pc_f01_peak_and_crash_newpeakrate_63d_base_v135_signal,
    f01pc_f01_peak_and_crash_newpeakrate_252d_base_v136_signal,
    f01pc_f01_peak_and_crash_athproxxvolz_21d_base_v137_signal,
    f01pc_f01_peak_and_crash_athproxxvolz_63d_base_v138_signal,
    f01pc_f01_peak_and_crash_ddxrange_252d_base_v139_signal,
    f01pc_f01_peak_and_crash_ddxrange_63d_base_v140_signal,
    f01pc_f01_peak_and_crash_sharpxdv_252d_base_v141_signal,
    f01pc_f01_peak_and_crash_postpeakdrop_63d_base_v142_signal,
    f01pc_f01_peak_and_crash_postpeakdrop_252d_base_v143_signal,
    f01pc_f01_peak_and_crash_crashcountxvol_252d_base_v144_signal,
    f01pc_f01_peak_and_crash_crashcountxdv_504d_base_v145_signal,
    f01pc_f01_peak_and_crash_ddxcurdv_21d_base_v146_signal,
    f01pc_f01_peak_and_crash_ddxcurdv_252d_base_v147_signal,
    f01pc_f01_peak_and_crash_compositesev_252d_base_v148_signal,
    f01pc_f01_peak_and_crash_compositesev_504d_base_v149_signal,
    f01pc_f01_peak_and_crash_intensarea_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_PEAK_AND_CRASH_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f01_peak_level", "_f01_drawdown_from_peak", "_f01_crash_intensity")
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
    print(f"OK f01_peak_and_crash_base_076_150_claude: {n_features} features pass")
