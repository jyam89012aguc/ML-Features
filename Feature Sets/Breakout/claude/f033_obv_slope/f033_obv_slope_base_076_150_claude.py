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
def _f033_obv(closeadj, volume):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    return (sign * volume).cumsum()


def _f033_obv_slope(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    return obv.diff(w) / obv.abs().replace(0, np.nan)


def _f033_obv_trend(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    m = obv.rolling(w, min_periods=max(1, w // 2)).mean()
    return (obv - m) / obv.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


def f033obs_f033_obv_slope_obvslopexsign_126d_base_v076_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_189d_base_v077_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    ret = closeadj.pct_change(47)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_252d_base_v078_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_378d_base_v079_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    ret = closeadj.pct_change(94)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexsign_504d_base_v080_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    ret = closeadj.pct_change(126)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_5d_base_v081_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=5, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_10d_base_v082_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=10, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_21d_base_v083_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=21, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_42d_base_v084_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=42, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_63d_base_v085_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=63, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(63, min_periods=15).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_126d_base_v086_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=126, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(126, min_periods=31).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_189d_base_v087_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=189, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(189, min_periods=47).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_252d_base_v088_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=252, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_378d_base_v089_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=378, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(378, min_periods=94).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_emaobv_504d_base_v090_signal(closeadj, volume):
    o = _f033_obv(closeadj, volume)
    ema = o.ewm(span=504, adjust=False).mean()
    result = (o - ema) / o.abs().replace(0, np.nan).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_5d_base_v091_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_10d_base_v092_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_21d_base_v093_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_42d_base_v094_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    result = _std(sl, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_63d_base_v095_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    result = _std(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_126d_base_v096_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    result = _std(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_189d_base_v097_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    result = _std(sl, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_252d_base_v098_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    result = _std(sl, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_378d_base_v099_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    result = _std(sl, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_stdobvslope_504d_base_v100_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    result = _std(sl, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_5d_base_v101_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_10d_base_v102_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_21d_base_v103_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_42d_base_v104_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_63d_base_v105_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_126d_base_v106_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_189d_base_v107_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_252d_base_v108_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_378d_base_v109_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_sqobvslope_504d_base_v110_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_5d_base_v111_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    tr = _f033_obv_trend(closeadj, volume, 5)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_10d_base_v112_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    tr = _f033_obv_trend(closeadj, volume, 10)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_21d_base_v113_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    tr = _f033_obv_trend(closeadj, volume, 21)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_42d_base_v114_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    tr = _f033_obv_trend(closeadj, volume, 42)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_63d_base_v115_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    tr = _f033_obv_trend(closeadj, volume, 63)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_126d_base_v116_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    tr = _f033_obv_trend(closeadj, volume, 126)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_189d_base_v117_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    tr = _f033_obv_trend(closeadj, volume, 189)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_252d_base_v118_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    tr = _f033_obv_trend(closeadj, volume, 252)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_378d_base_v119_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    tr = _f033_obv_trend(closeadj, volume, 378)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvgap_504d_base_v120_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    tr = _f033_obv_trend(closeadj, volume, 504)
    result = (sl - tr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_5d_base_v121_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    vavg = _mean(volume, 21)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_10d_base_v122_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    vavg = _mean(volume, 21)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_21d_base_v123_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    vavg = _mean(volume, 21)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_42d_base_v124_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    vavg = _mean(volume, 42)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_63d_base_v125_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    vavg = _mean(volume, 63)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_126d_base_v126_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    vavg = _mean(volume, 126)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_189d_base_v127_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    vavg = _mean(volume, 189)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_252d_base_v128_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    vavg = _mean(volume, 252)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_378d_base_v129_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    vavg = _mean(volume, 378)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_obvslopexvol_504d_base_v130_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    vavg = _mean(volume, 504)
    result = sl * vavg / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_5d_base_v131_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 5)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_10d_base_v132_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 10)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_21d_base_v133_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 21)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_42d_base_v134_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 42)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_63d_base_v135_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 63)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_126d_base_v136_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 126)
    result = _z(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_189d_base_v137_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 189)
    result = _z(t, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_252d_base_v138_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 252)
    result = _z(t, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_378d_base_v139_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 378)
    result = _z(t, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_zobvtrend_504d_base_v140_signal(closeadj, volume):
    t = _f033_obv_trend(closeadj, volume, 504)
    result = _z(t, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_5d_base_v141_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 5)
    result = sl.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_10d_base_v142_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 10)
    result = sl.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_21d_base_v143_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 21)
    result = sl.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_42d_base_v144_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 42)
    result = sl.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_63d_base_v145_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 63)
    result = sl.diff(15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_126d_base_v146_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 126)
    result = sl.diff(31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_189d_base_v147_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 189)
    result = sl.diff(47) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_252d_base_v148_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 252)
    result = sl.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_378d_base_v149_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 378)
    result = sl.diff(94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f033obs_f033_obv_slope_diffobvslope_504d_base_v150_signal(closeadj, volume):
    sl = _f033_obv_slope(closeadj, volume, 504)
    result = sl.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f033obs_f033_obv_slope_obvslopexsign_126d_base_v076_signal,
    f033obs_f033_obv_slope_obvslopexsign_189d_base_v077_signal,
    f033obs_f033_obv_slope_obvslopexsign_252d_base_v078_signal,
    f033obs_f033_obv_slope_obvslopexsign_378d_base_v079_signal,
    f033obs_f033_obv_slope_obvslopexsign_504d_base_v080_signal,
    f033obs_f033_obv_slope_emaobv_5d_base_v081_signal,
    f033obs_f033_obv_slope_emaobv_10d_base_v082_signal,
    f033obs_f033_obv_slope_emaobv_21d_base_v083_signal,
    f033obs_f033_obv_slope_emaobv_42d_base_v084_signal,
    f033obs_f033_obv_slope_emaobv_63d_base_v085_signal,
    f033obs_f033_obv_slope_emaobv_126d_base_v086_signal,
    f033obs_f033_obv_slope_emaobv_189d_base_v087_signal,
    f033obs_f033_obv_slope_emaobv_252d_base_v088_signal,
    f033obs_f033_obv_slope_emaobv_378d_base_v089_signal,
    f033obs_f033_obv_slope_emaobv_504d_base_v090_signal,
    f033obs_f033_obv_slope_stdobvslope_5d_base_v091_signal,
    f033obs_f033_obv_slope_stdobvslope_10d_base_v092_signal,
    f033obs_f033_obv_slope_stdobvslope_21d_base_v093_signal,
    f033obs_f033_obv_slope_stdobvslope_42d_base_v094_signal,
    f033obs_f033_obv_slope_stdobvslope_63d_base_v095_signal,
    f033obs_f033_obv_slope_stdobvslope_126d_base_v096_signal,
    f033obs_f033_obv_slope_stdobvslope_189d_base_v097_signal,
    f033obs_f033_obv_slope_stdobvslope_252d_base_v098_signal,
    f033obs_f033_obv_slope_stdobvslope_378d_base_v099_signal,
    f033obs_f033_obv_slope_stdobvslope_504d_base_v100_signal,
    f033obs_f033_obv_slope_sqobvslope_5d_base_v101_signal,
    f033obs_f033_obv_slope_sqobvslope_10d_base_v102_signal,
    f033obs_f033_obv_slope_sqobvslope_21d_base_v103_signal,
    f033obs_f033_obv_slope_sqobvslope_42d_base_v104_signal,
    f033obs_f033_obv_slope_sqobvslope_63d_base_v105_signal,
    f033obs_f033_obv_slope_sqobvslope_126d_base_v106_signal,
    f033obs_f033_obv_slope_sqobvslope_189d_base_v107_signal,
    f033obs_f033_obv_slope_sqobvslope_252d_base_v108_signal,
    f033obs_f033_obv_slope_sqobvslope_378d_base_v109_signal,
    f033obs_f033_obv_slope_sqobvslope_504d_base_v110_signal,
    f033obs_f033_obv_slope_obvgap_5d_base_v111_signal,
    f033obs_f033_obv_slope_obvgap_10d_base_v112_signal,
    f033obs_f033_obv_slope_obvgap_21d_base_v113_signal,
    f033obs_f033_obv_slope_obvgap_42d_base_v114_signal,
    f033obs_f033_obv_slope_obvgap_63d_base_v115_signal,
    f033obs_f033_obv_slope_obvgap_126d_base_v116_signal,
    f033obs_f033_obv_slope_obvgap_189d_base_v117_signal,
    f033obs_f033_obv_slope_obvgap_252d_base_v118_signal,
    f033obs_f033_obv_slope_obvgap_378d_base_v119_signal,
    f033obs_f033_obv_slope_obvgap_504d_base_v120_signal,
    f033obs_f033_obv_slope_obvslopexvol_5d_base_v121_signal,
    f033obs_f033_obv_slope_obvslopexvol_10d_base_v122_signal,
    f033obs_f033_obv_slope_obvslopexvol_21d_base_v123_signal,
    f033obs_f033_obv_slope_obvslopexvol_42d_base_v124_signal,
    f033obs_f033_obv_slope_obvslopexvol_63d_base_v125_signal,
    f033obs_f033_obv_slope_obvslopexvol_126d_base_v126_signal,
    f033obs_f033_obv_slope_obvslopexvol_189d_base_v127_signal,
    f033obs_f033_obv_slope_obvslopexvol_252d_base_v128_signal,
    f033obs_f033_obv_slope_obvslopexvol_378d_base_v129_signal,
    f033obs_f033_obv_slope_obvslopexvol_504d_base_v130_signal,
    f033obs_f033_obv_slope_zobvtrend_5d_base_v131_signal,
    f033obs_f033_obv_slope_zobvtrend_10d_base_v132_signal,
    f033obs_f033_obv_slope_zobvtrend_21d_base_v133_signal,
    f033obs_f033_obv_slope_zobvtrend_42d_base_v134_signal,
    f033obs_f033_obv_slope_zobvtrend_63d_base_v135_signal,
    f033obs_f033_obv_slope_zobvtrend_126d_base_v136_signal,
    f033obs_f033_obv_slope_zobvtrend_189d_base_v137_signal,
    f033obs_f033_obv_slope_zobvtrend_252d_base_v138_signal,
    f033obs_f033_obv_slope_zobvtrend_378d_base_v139_signal,
    f033obs_f033_obv_slope_zobvtrend_504d_base_v140_signal,
    f033obs_f033_obv_slope_diffobvslope_5d_base_v141_signal,
    f033obs_f033_obv_slope_diffobvslope_10d_base_v142_signal,
    f033obs_f033_obv_slope_diffobvslope_21d_base_v143_signal,
    f033obs_f033_obv_slope_diffobvslope_42d_base_v144_signal,
    f033obs_f033_obv_slope_diffobvslope_63d_base_v145_signal,
    f033obs_f033_obv_slope_diffobvslope_126d_base_v146_signal,
    f033obs_f033_obv_slope_diffobvslope_189d_base_v147_signal,
    f033obs_f033_obv_slope_diffobvslope_252d_base_v148_signal,
    f033obs_f033_obv_slope_diffobvslope_378d_base_v149_signal,
    f033obs_f033_obv_slope_diffobvslope_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F033_OBV_SLOPE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f033_obv', '_f033_obv_slope', '_f033_obv_trend')
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
    print(f"OK f033_obv_slope_base_076_150_claude: {n_features} features pass")
