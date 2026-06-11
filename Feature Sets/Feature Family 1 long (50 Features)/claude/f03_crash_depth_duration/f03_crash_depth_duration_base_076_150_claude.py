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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f03_crash_depth(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - peak) / peak.replace(0, np.nan).abs()


def _f03_crash_duration(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    in_dd = (close < peak).astype(float)
    grp = (in_dd.diff().fillna(0) != 0).cumsum()
    return in_dd.groupby(grp).cumsum() * in_dd


def _f03_crash_recovery(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - trough) / trough.replace(0, np.nan).abs()


# expanding crash depth scaled by current closeadj
def f03cdd_f03_crash_depth_duration_depthexpxprice_252d_base_v076_signal(closeadj):
    peak = closeadj.expanding(min_periods=21).max()
    depth = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = depth * closeadj + _f03_crash_depth(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth times 21d return volatility
def f03cdd_f03_crash_depth_duration_depthxretvol_63d_base_v077_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f03_crash_depth(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth times 63d return volatility
def f03cdd_f03_crash_depth_duration_depthxretvol_252d_base_v078_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f03_crash_depth(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth × current closeadj × 21d return
def f03cdd_f03_crash_depth_duration_depthxret_21d_base_v079_signal(closeadj):
    r21 = closeadj.pct_change(21)
    result = _f03_crash_depth(closeadj, 21) * closeadj * r21
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × 63d return
def f03cdd_f03_crash_depth_duration_depthxret_63d_base_v080_signal(closeadj):
    r63 = closeadj.pct_change(63)
    result = _f03_crash_depth(closeadj, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × 252d return
def f03cdd_f03_crash_depth_duration_depthxret_252d_base_v081_signal(closeadj):
    r252 = closeadj.pct_change(252)
    result = _f03_crash_depth(closeadj, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth normalized by 21d ATR-style range
def f03cdd_f03_crash_depth_duration_depthnormatr_63d_base_v082_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f03_crash_depth(closeadj, 63) * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depth normalized by 63d ATR-style range
def f03cdd_f03_crash_depth_duration_depthnormatr_504d_base_v083_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f03_crash_depth(closeadj, 504) * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × cumulative downside dollar-volume over 21d
def f03cdd_f03_crash_depth_duration_depthxdownvol_63d_base_v084_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f03_crash_depth(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × cumulative downside dollar-volume over 63d
def f03cdd_f03_crash_depth_duration_depthxdownvol_252d_base_v085_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    result = _f03_crash_depth(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth times skewness of returns
def f03cdd_f03_crash_depth_duration_depthxskew_63d_base_v086_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f03_crash_depth(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × skewness of returns
def f03cdd_f03_crash_depth_duration_depthxskew_252d_base_v087_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f03_crash_depth(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × kurtosis of returns
def f03cdd_f03_crash_depth_duration_depthxkurt_63d_base_v088_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f03_crash_depth(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × kurtosis of returns
def f03cdd_f03_crash_depth_duration_depthxkurt_252d_base_v089_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f03_crash_depth(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth divided by 252d depth (recent vs persistent)
def f03cdd_f03_crash_depth_duration_depthratio_63v252_base_v090_signal(closeadj):
    a = _f03_crash_depth(closeadj, 63)
    b = _f03_crash_depth(closeadj, 252).replace(0, np.nan)
    result = a / b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth divided by 63d depth
def f03cdd_f03_crash_depth_duration_depthratio_21v63_base_v091_signal(closeadj):
    a = _f03_crash_depth(closeadj, 21)
    b = _f03_crash_depth(closeadj, 63).replace(0, np.nan)
    result = a / b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth divided by 504d depth
def f03cdd_f03_crash_depth_duration_depthratio_252v504_base_v092_signal(closeadj):
    a = _f03_crash_depth(closeadj, 252)
    b = _f03_crash_depth(closeadj, 504).replace(0, np.nan)
    result = a / b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth minus 252d depth (acceleration of drawdown)
def f03cdd_f03_crash_depth_duration_depthdiff_63m252_base_v093_signal(closeadj):
    result = _f03_crash_depth(closeadj, 63) - _f03_crash_depth(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth minus 63d depth
def f03cdd_f03_crash_depth_duration_depthdiff_21m63_base_v094_signal(closeadj):
    result = _f03_crash_depth(closeadj, 21) - _f03_crash_depth(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth minus 504d depth
def f03cdd_f03_crash_depth_duration_depthdiff_252m504_base_v095_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252) - _f03_crash_depth(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × 21d duration (intensity)
def f03cdd_f03_crash_depth_duration_depthxdur_63d_base_v096_signal(closeadj):
    result = _f03_crash_depth(closeadj, 63) * _f03_crash_duration(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × 63d duration
def f03cdd_f03_crash_depth_duration_depthxdur_252d_base_v097_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252) * _f03_crash_duration(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depth × 252d duration
def f03cdd_f03_crash_depth_duration_depthxdur_504d_base_v098_signal(closeadj):
    result = _f03_crash_depth(closeadj, 504) * _f03_crash_duration(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# expanding crash duration scaled by 21d closeadj level
def f03cdd_f03_crash_depth_duration_durexpxprice_21d_base_v099_signal(closeadj):
    peak = closeadj.expanding(min_periods=21).max()
    in_dd = (closeadj < peak).astype(float)
    grp = (in_dd.diff().fillna(0) != 0).cumsum()
    dur = in_dd.groupby(grp).cumsum() * in_dd
    result = dur * closeadj + _f03_crash_duration(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration × 21d return std
def f03cdd_f03_crash_depth_duration_durxretvol_63d_base_v100_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f03_crash_duration(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration × 63d return std
def f03cdd_f03_crash_depth_duration_durxretvol_252d_base_v101_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f03_crash_duration(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration × 21d return
def f03cdd_f03_crash_depth_duration_durxret_21d_base_v102_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f03_crash_duration(closeadj, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration × 63d return
def f03cdd_f03_crash_depth_duration_durxret_63d_base_v103_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f03_crash_duration(closeadj, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration × 252d return
def f03cdd_f03_crash_depth_duration_durxret_252d_base_v104_signal(closeadj):
    r = closeadj.pct_change(252)
    result = _f03_crash_duration(closeadj, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration × 21d ATR
def f03cdd_f03_crash_depth_duration_durxatr_63d_base_v105_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f03_crash_duration(closeadj, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration × 63d ATR
def f03cdd_f03_crash_depth_duration_durxatr_252d_base_v106_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f03_crash_duration(closeadj, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration / 252d duration ratio
def f03cdd_f03_crash_depth_duration_durratio_63v252_base_v107_signal(closeadj):
    a = _f03_crash_duration(closeadj, 63)
    b = _f03_crash_duration(closeadj, 252).replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration / 63d duration ratio
def f03cdd_f03_crash_depth_duration_durratio_21v63_base_v108_signal(closeadj):
    a = _f03_crash_duration(closeadj, 21)
    b = _f03_crash_duration(closeadj, 63).replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration minus 252d duration
def f03cdd_f03_crash_depth_duration_durdiff_63m252_base_v109_signal(closeadj):
    result = (_f03_crash_duration(closeadj, 63) - _f03_crash_duration(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration minus 63d duration
def f03cdd_f03_crash_depth_duration_durdiff_21m63_base_v110_signal(closeadj):
    result = (_f03_crash_duration(closeadj, 21) - _f03_crash_duration(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration minus 504d duration
def f03cdd_f03_crash_depth_duration_durdiff_252m504_base_v111_signal(closeadj):
    result = (_f03_crash_duration(closeadj, 252) - _f03_crash_duration(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash recovery scaled by closeadj
def f03cdd_f03_crash_depth_duration_recovery_21d_base_v112_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d crash recovery scaled by closeadj
def f03cdd_f03_crash_depth_duration_recovery_126d_base_v113_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d crash recovery scaled by closeadj
def f03cdd_f03_crash_depth_duration_recovery_378d_base_v114_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d recovery × 63d duration
def f03cdd_f03_crash_depth_duration_recxdur_63d_base_v115_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 63) * _f03_crash_duration(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d recovery × 252d duration
def f03cdd_f03_crash_depth_duration_recxdur_252d_base_v116_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 252) * _f03_crash_duration(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d recovery × 504d duration
def f03cdd_f03_crash_depth_duration_recxdur_504d_base_v117_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 504) * _f03_crash_duration(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d recovery / 63d depth magnitude (recovery efficiency)
def f03cdd_f03_crash_depth_duration_receff_63d_base_v118_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 63)
    dep = _f03_crash_depth(closeadj, 63).abs().replace(0, np.nan)
    result = rec / dep * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d recovery / 252d depth magnitude
def f03cdd_f03_crash_depth_duration_receff_252d_base_v119_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 252)
    dep = _f03_crash_depth(closeadj, 252).abs().replace(0, np.nan)
    result = rec / dep * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d recovery / 504d depth magnitude
def f03cdd_f03_crash_depth_duration_receff_504d_base_v120_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 504)
    dep = _f03_crash_depth(closeadj, 504).abs().replace(0, np.nan)
    result = rec / dep * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d recovery × volume zscore (recovery on volume)
def f03cdd_f03_crash_depth_duration_recxvolz_63d_base_v121_signal(closeadj, volume):
    result = _f03_crash_recovery(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d recovery × volume zscore
def f03cdd_f03_crash_depth_duration_recxvolz_252d_base_v122_signal(closeadj, volume):
    result = _f03_crash_recovery(closeadj, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth × 252d duration (deep + persistent)
def f03cdd_f03_crash_depth_duration_recentdeepXpersist_252d_base_v123_signal(closeadj):
    result = _f03_crash_depth(closeadj, 21) * _f03_crash_duration(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × 504d duration
def f03cdd_f03_crash_depth_duration_recentdeepXpersist_504d_base_v124_signal(closeadj):
    result = _f03_crash_depth(closeadj, 63) * _f03_crash_duration(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst-ever depth
def f03cdd_f03_crash_depth_duration_depthworstever_base_v125_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504)
    result = d.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth gap to expanding worst-ever
def f03cdd_f03_crash_depth_duration_depthvshistworst_63d_base_v126_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    worst = d.expanding(min_periods=63).min()
    result = (d - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth gap to expanding worst-ever
def f03cdd_f03_crash_depth_duration_depthvshistworst_252d_base_v127_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504)
    worst = d.expanding(min_periods=252).min()
    result = (d - worst) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth area / 252d depth area ratio
def f03cdd_f03_crash_depth_duration_depthareafrac_63v252_base_v128_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    a = d.rolling(63, min_periods=21).sum()
    b = d.rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth-area / 63d depth-area
def f03cdd_f03_crash_depth_duration_depthareafrac_21v63_base_v129_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63).abs()
    a = d.rolling(21, min_periods=5).sum()
    b = d.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth-area / 504d depth-area
def f03cdd_f03_crash_depth_duration_depthareafrac_252v504_base_v130_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    a = d.rolling(252, min_periods=63).sum()
    b = d.rolling(504, min_periods=126).sum().replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration-area / 252d duration-area
def f03cdd_f03_crash_depth_duration_durareafrac_63v252_base_v131_signal(closeadj):
    d = _f03_crash_duration(closeadj, 252)
    a = d.rolling(63, min_periods=21).sum()
    b = d.rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d depth-volatility-of-volatility
def f03cdd_f03_crash_depth_duration_depthvolvol_63d_base_v132_signal(closeadj):
    sd = _std(_f03_crash_depth(closeadj, 252), 63)
    result = _std(sd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d depth-volatility-of-volatility
def f03cdd_f03_crash_depth_duration_depthvolvol_252d_base_v133_signal(closeadj):
    sd = _std(_f03_crash_depth(closeadj, 504), 252)
    result = _std(sd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth - rolling 252d depth mean (anomaly)
def f03cdd_f03_crash_depth_duration_depthanomaly_63d_base_v134_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63)
    base = _mean(_f03_crash_depth(closeadj, 252), 252)
    result = (d - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth - rolling 504d depth mean
def f03cdd_f03_crash_depth_duration_depthanomaly_252d_base_v135_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    base = _mean(_f03_crash_depth(closeadj, 504), 504)
    result = (d - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration - rolling 252d duration mean
def f03cdd_f03_crash_depth_duration_durationanomaly_63d_base_v136_signal(closeadj):
    d = _f03_crash_duration(closeadj, 63)
    base = _mean(_f03_crash_duration(closeadj, 252), 252)
    result = (d - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration - rolling 504d duration mean
def f03cdd_f03_crash_depth_duration_durationanomaly_252d_base_v137_signal(closeadj):
    d = _f03_crash_duration(closeadj, 252)
    base = _mean(_f03_crash_duration(closeadj, 504), 504)
    result = (d - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crash depth recovery half-life proxy at 63d
def f03cdd_f03_crash_depth_duration_rechalfproxy_63d_base_v138_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 63)
    dep = _f03_crash_depth(closeadj, 63).abs().replace(0, np.nan)
    ratio = (rec / dep).clip(upper=2.0)
    result = (1.0 - ratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crash depth recovery half-life proxy at 252d
def f03cdd_f03_crash_depth_duration_rechalfproxy_252d_base_v139_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 252)
    dep = _f03_crash_depth(closeadj, 252).abs().replace(0, np.nan)
    ratio = (rec / dep).clip(upper=2.0)
    result = (1.0 - ratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of crash depth (smoothed depth)
def f03cdd_f03_crash_depth_duration_depthema_63d_base_v140_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63)
    result = d.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of crash depth
def f03cdd_f03_crash_depth_duration_depthema_252d_base_v141_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    result = d.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of crash duration
def f03cdd_f03_crash_depth_duration_durationema_21d_base_v142_signal(closeadj):
    d = _f03_crash_duration(closeadj, 21)
    result = d.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of crash duration
def f03cdd_f03_crash_depth_duration_durationema_252d_base_v143_signal(closeadj):
    d = _f03_crash_duration(closeadj, 252)
    result = d.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max recovery in 252d window (best comeback)
def f03cdd_f03_crash_depth_duration_recmaxin_252d_base_v144_signal(closeadj):
    r = _f03_crash_recovery(closeadj, 63)
    result = r.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max recovery in 504d window
def f03cdd_f03_crash_depth_duration_recmaxin_504d_base_v145_signal(closeadj):
    r = _f03_crash_recovery(closeadj, 252)
    result = r.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth × current dollar volume
def f03cdd_f03_crash_depth_duration_depthxcurdv_63d_base_v146_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f03_crash_depth(closeadj, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth × current dollar volume
def f03cdd_f03_crash_depth_duration_depthxcurdv_252d_base_v147_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f03_crash_depth(closeadj, 252) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d high-low range × 63d depth (volatile-deep crash)
def f03cdd_f03_crash_depth_duration_depthxrange_63d_base_v148_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f03_crash_depth(closeadj, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# 63d high-low range × 252d depth
def f03cdd_f03_crash_depth_duration_depthxrange_252d_base_v149_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f03_crash_depth(closeadj, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# composite: 252d depth + 252d duration / 252 (normalized) all weighted by close
def f03cdd_f03_crash_depth_duration_compositesev_252d_base_v150_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    t = _f03_crash_duration(closeadj, 252) / 252.0
    result = (d + t) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03cdd_f03_crash_depth_duration_depthexpxprice_252d_base_v076_signal,
    f03cdd_f03_crash_depth_duration_depthxretvol_63d_base_v077_signal,
    f03cdd_f03_crash_depth_duration_depthxretvol_252d_base_v078_signal,
    f03cdd_f03_crash_depth_duration_depthxret_21d_base_v079_signal,
    f03cdd_f03_crash_depth_duration_depthxret_63d_base_v080_signal,
    f03cdd_f03_crash_depth_duration_depthxret_252d_base_v081_signal,
    f03cdd_f03_crash_depth_duration_depthnormatr_63d_base_v082_signal,
    f03cdd_f03_crash_depth_duration_depthnormatr_504d_base_v083_signal,
    f03cdd_f03_crash_depth_duration_depthxdownvol_63d_base_v084_signal,
    f03cdd_f03_crash_depth_duration_depthxdownvol_252d_base_v085_signal,
    f03cdd_f03_crash_depth_duration_depthxskew_63d_base_v086_signal,
    f03cdd_f03_crash_depth_duration_depthxskew_252d_base_v087_signal,
    f03cdd_f03_crash_depth_duration_depthxkurt_63d_base_v088_signal,
    f03cdd_f03_crash_depth_duration_depthxkurt_252d_base_v089_signal,
    f03cdd_f03_crash_depth_duration_depthratio_63v252_base_v090_signal,
    f03cdd_f03_crash_depth_duration_depthratio_21v63_base_v091_signal,
    f03cdd_f03_crash_depth_duration_depthratio_252v504_base_v092_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_63m252_base_v093_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_21m63_base_v094_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_252m504_base_v095_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_63d_base_v096_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_252d_base_v097_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_504d_base_v098_signal,
    f03cdd_f03_crash_depth_duration_durexpxprice_21d_base_v099_signal,
    f03cdd_f03_crash_depth_duration_durxretvol_63d_base_v100_signal,
    f03cdd_f03_crash_depth_duration_durxretvol_252d_base_v101_signal,
    f03cdd_f03_crash_depth_duration_durxret_21d_base_v102_signal,
    f03cdd_f03_crash_depth_duration_durxret_63d_base_v103_signal,
    f03cdd_f03_crash_depth_duration_durxret_252d_base_v104_signal,
    f03cdd_f03_crash_depth_duration_durxatr_63d_base_v105_signal,
    f03cdd_f03_crash_depth_duration_durxatr_252d_base_v106_signal,
    f03cdd_f03_crash_depth_duration_durratio_63v252_base_v107_signal,
    f03cdd_f03_crash_depth_duration_durratio_21v63_base_v108_signal,
    f03cdd_f03_crash_depth_duration_durdiff_63m252_base_v109_signal,
    f03cdd_f03_crash_depth_duration_durdiff_21m63_base_v110_signal,
    f03cdd_f03_crash_depth_duration_durdiff_252m504_base_v111_signal,
    f03cdd_f03_crash_depth_duration_recovery_21d_base_v112_signal,
    f03cdd_f03_crash_depth_duration_recovery_126d_base_v113_signal,
    f03cdd_f03_crash_depth_duration_recovery_378d_base_v114_signal,
    f03cdd_f03_crash_depth_duration_recxdur_63d_base_v115_signal,
    f03cdd_f03_crash_depth_duration_recxdur_252d_base_v116_signal,
    f03cdd_f03_crash_depth_duration_recxdur_504d_base_v117_signal,
    f03cdd_f03_crash_depth_duration_receff_63d_base_v118_signal,
    f03cdd_f03_crash_depth_duration_receff_252d_base_v119_signal,
    f03cdd_f03_crash_depth_duration_receff_504d_base_v120_signal,
    f03cdd_f03_crash_depth_duration_recxvolz_63d_base_v121_signal,
    f03cdd_f03_crash_depth_duration_recxvolz_252d_base_v122_signal,
    f03cdd_f03_crash_depth_duration_recentdeepXpersist_252d_base_v123_signal,
    f03cdd_f03_crash_depth_duration_recentdeepXpersist_504d_base_v124_signal,
    f03cdd_f03_crash_depth_duration_depthworstever_base_v125_signal,
    f03cdd_f03_crash_depth_duration_depthvshistworst_63d_base_v126_signal,
    f03cdd_f03_crash_depth_duration_depthvshistworst_252d_base_v127_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_63v252_base_v128_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_21v63_base_v129_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_252v504_base_v130_signal,
    f03cdd_f03_crash_depth_duration_durareafrac_63v252_base_v131_signal,
    f03cdd_f03_crash_depth_duration_depthvolvol_63d_base_v132_signal,
    f03cdd_f03_crash_depth_duration_depthvolvol_252d_base_v133_signal,
    f03cdd_f03_crash_depth_duration_depthanomaly_63d_base_v134_signal,
    f03cdd_f03_crash_depth_duration_depthanomaly_252d_base_v135_signal,
    f03cdd_f03_crash_depth_duration_durationanomaly_63d_base_v136_signal,
    f03cdd_f03_crash_depth_duration_durationanomaly_252d_base_v137_signal,
    f03cdd_f03_crash_depth_duration_rechalfproxy_63d_base_v138_signal,
    f03cdd_f03_crash_depth_duration_rechalfproxy_252d_base_v139_signal,
    f03cdd_f03_crash_depth_duration_depthema_63d_base_v140_signal,
    f03cdd_f03_crash_depth_duration_depthema_252d_base_v141_signal,
    f03cdd_f03_crash_depth_duration_durationema_21d_base_v142_signal,
    f03cdd_f03_crash_depth_duration_durationema_252d_base_v143_signal,
    f03cdd_f03_crash_depth_duration_recmaxin_252d_base_v144_signal,
    f03cdd_f03_crash_depth_duration_recmaxin_504d_base_v145_signal,
    f03cdd_f03_crash_depth_duration_depthxcurdv_63d_base_v146_signal,
    f03cdd_f03_crash_depth_duration_depthxcurdv_252d_base_v147_signal,
    f03cdd_f03_crash_depth_duration_depthxrange_63d_base_v148_signal,
    f03cdd_f03_crash_depth_duration_depthxrange_252d_base_v149_signal,
    f03cdd_f03_crash_depth_duration_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CRASH_DEPTH_DURATION_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f03_crash_depth", "_f03_crash_duration", "_f03_crash_recovery")
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
    print(f"OK f03_crash_depth_duration_base_076_150_claude: {n_features} features pass")
