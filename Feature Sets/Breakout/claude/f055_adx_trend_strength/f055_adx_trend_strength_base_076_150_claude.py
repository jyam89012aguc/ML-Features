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
def _f055_dm_plus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    return dmp.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_dm_minus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    return dmn.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_adx(high, low, closeadj, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    dip = dmp.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    din = dmn.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    dx = (dip - din).abs() / (dip + din).replace(0, np.nan)
    return dx.rolling(w, min_periods=max(1, w // 2)).mean() * closeadj


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v076_signal(high, low, closeadj):
    result = _z(_f055_dm_plus(high, low, 5), 5) * _z(_f055_dm_plus(high, low, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v077_signal(high, low, closeadj):
    result = _mean(_f055_dm_plus(high, low, 10), 10) * _std(_f055_dm_plus(high, low, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v078_signal(high, low, closeadj):
    result = _mean(_f055_dm_plus(high, low, 21), 21) / _std(_f055_dm_plus(high, low, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v079_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 42)).ewm(span=42, adjust=False).mean() - _mean(_f055_dm_plus(high, low, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v080_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f055_dm_plus(high, low, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_base_v081_signal(high, low, closeadj):
    result = _mean((_f055_dm_plus(high, low, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_189d_base_v082_signal(high, low, closeadj):
    result = _std((_f055_dm_plus(high, low, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_base_v083_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_378d_base_v084_signal(high, low, closeadj):
    result = ((1.0 + (_f055_dm_plus(high, low, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_504d_base_v085_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v086_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f055_dm_plus(high, low, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v087_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f055_dm_plus(high, low, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v088_signal(high, low, closeadj):
    result = _z((_f055_dm_plus(high, low, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v089_signal(high, low, closeadj):
    result = (_mean(_f055_dm_plus(high, low, 42), 42) - _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v090_signal(high, low, closeadj):
    result = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 2)) / _mean(_f055_dm_plus(high, low, 63), 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_base_v091_signal(high, low, closeadj):
    result = np.sign(_f055_dm_plus(high, low, 126)) * (_f055_dm_plus(high, low, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_189d_base_v092_signal(high, low, closeadj):
    result = np.sign(_f055_dm_plus(high, low, 189)) * np.log1p((_f055_dm_plus(high, low, 189)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_base_v093_signal(high, low, closeadj):
    result = _std(_f055_dm_plus(high, low, 252), 252) / _mean(_f055_dm_plus(high, low, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_378d_base_v094_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f055_dm_plus(high, low, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_504d_base_v095_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 504)) - (_f055_dm_plus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_5d_base_v096_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_10d_base_v097_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_base_v098_signal(high, low, closeadj):
    result = (_f055_dm_plus(high, low, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_base_v099_signal(high, low, closeadj):
    result = (((_f055_dm_plus(high, low, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_base_v100_signal(high, low, closeadj):
    result = ((_f055_dm_plus(high, low, 63)).ewm(span=63, adjust=False).mean() - (_f055_dm_plus(high, low, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v101_signal(high, low, closeadj):
    result = _z(_f055_dm_minus(high, low, 5), 5) * _z(_f055_dm_minus(high, low, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v102_signal(high, low, closeadj):
    result = _mean(_f055_dm_minus(high, low, 10), 10) * _std(_f055_dm_minus(high, low, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v103_signal(high, low, closeadj):
    result = _mean(_f055_dm_minus(high, low, 21), 21) / _std(_f055_dm_minus(high, low, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v104_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 42)).ewm(span=42, adjust=False).mean() - _mean(_f055_dm_minus(high, low, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v105_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f055_dm_minus(high, low, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_base_v106_signal(high, low, closeadj):
    result = _mean((_f055_dm_minus(high, low, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_189d_base_v107_signal(high, low, closeadj):
    result = _std((_f055_dm_minus(high, low, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_base_v108_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_378d_base_v109_signal(high, low, closeadj):
    result = ((1.0 + (_f055_dm_minus(high, low, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_504d_base_v110_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v111_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f055_dm_minus(high, low, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v112_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f055_dm_minus(high, low, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v113_signal(high, low, closeadj):
    result = _z((_f055_dm_minus(high, low, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v114_signal(high, low, closeadj):
    result = (_mean(_f055_dm_minus(high, low, 42), 42) - _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v115_signal(high, low, closeadj):
    result = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 2)) / _mean(_f055_dm_minus(high, low, 63), 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_base_v116_signal(high, low, closeadj):
    result = np.sign(_f055_dm_minus(high, low, 126)) * (_f055_dm_minus(high, low, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_189d_base_v117_signal(high, low, closeadj):
    result = np.sign(_f055_dm_minus(high, low, 189)) * np.log1p((_f055_dm_minus(high, low, 189)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_base_v118_signal(high, low, closeadj):
    result = _std(_f055_dm_minus(high, low, 252), 252) / _mean(_f055_dm_minus(high, low, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_378d_base_v119_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f055_dm_minus(high, low, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_504d_base_v120_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 504)) - (_f055_dm_minus(high, low, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_5d_base_v121_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_10d_base_v122_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_base_v123_signal(high, low, closeadj):
    result = (_f055_dm_minus(high, low, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_base_v124_signal(high, low, closeadj):
    result = (((_f055_dm_minus(high, low, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_base_v125_signal(high, low, closeadj):
    result = ((_f055_dm_minus(high, low, 63)).ewm(span=63, adjust=False).mean() - (_f055_dm_minus(high, low, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v126_signal(high, low, closeadj):
    result = _z(_f055_adx(high, low, closeadj, 5), 5) * _z(_f055_adx(high, low, closeadj, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v127_signal(high, low, closeadj):
    result = _mean(_f055_adx(high, low, closeadj, 10), 10) * _std(_f055_adx(high, low, closeadj, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v128_signal(high, low, closeadj):
    result = _mean(_f055_adx(high, low, closeadj, 21), 21) / _std(_f055_adx(high, low, closeadj, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v129_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 42)).ewm(span=42, adjust=False).mean() - _mean(_f055_adx(high, low, closeadj, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v130_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f055_adx(high, low, closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_base_v131_signal(high, low, closeadj):
    result = _mean((_f055_adx(high, low, closeadj, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_189d_base_v132_signal(high, low, closeadj):
    result = _std((_f055_adx(high, low, closeadj, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_base_v133_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_378d_base_v134_signal(high, low, closeadj):
    result = ((1.0 + (_f055_adx(high, low, closeadj, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_504d_base_v135_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v136_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f055_adx(high, low, closeadj, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v137_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f055_adx(high, low, closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v138_signal(high, low, closeadj):
    result = _z((_f055_adx(high, low, closeadj, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v139_signal(high, low, closeadj):
    result = (_mean(_f055_adx(high, low, closeadj, 42), 42) - _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v140_signal(high, low, closeadj):
    result = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 2)) / _mean(_f055_adx(high, low, closeadj, 63), 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_base_v141_signal(high, low, closeadj):
    result = np.sign(_f055_adx(high, low, closeadj, 126)) * (_f055_adx(high, low, closeadj, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_189d_base_v142_signal(high, low, closeadj):
    result = np.sign(_f055_adx(high, low, closeadj, 189)) * np.log1p((_f055_adx(high, low, closeadj, 189)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_base_v143_signal(high, low, closeadj):
    result = _std(_f055_adx(high, low, closeadj, 252), 252) / _mean(_f055_adx(high, low, closeadj, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_378d_base_v144_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f055_adx(high, low, closeadj, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_504d_base_v145_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 504)) - (_f055_adx(high, low, closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_5d_base_v146_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_10d_base_v147_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_base_v148_signal(high, low, closeadj):
    result = (_f055_adx(high, low, closeadj, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_base_v149_signal(high, low, closeadj):
    result = (((_f055_adx(high, low, closeadj, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_base_v150_signal(high, low, closeadj):
    result = ((_f055_adx(high, low, closeadj, 63)).ewm(span=63, adjust=False).mean() - (_f055_adx(high, low, closeadj, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v076_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v077_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v078_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v079_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v080_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_base_v081_signal,
    f055ats_f055_adx_trend_strength_dm_plus_189d_base_v082_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_base_v083_signal,
    f055ats_f055_adx_trend_strength_dm_plus_378d_base_v084_signal,
    f055ats_f055_adx_trend_strength_dm_plus_504d_base_v085_signal,
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v086_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v087_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v088_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v089_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v090_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_base_v091_signal,
    f055ats_f055_adx_trend_strength_dm_plus_189d_base_v092_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_base_v093_signal,
    f055ats_f055_adx_trend_strength_dm_plus_378d_base_v094_signal,
    f055ats_f055_adx_trend_strength_dm_plus_504d_base_v095_signal,
    f055ats_f055_adx_trend_strength_dm_plus_5d_base_v096_signal,
    f055ats_f055_adx_trend_strength_dm_plus_10d_base_v097_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_base_v098_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_base_v099_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_base_v100_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v101_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v102_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v103_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v104_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v105_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_base_v106_signal,
    f055ats_f055_adx_trend_strength_dm_minus_189d_base_v107_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_base_v108_signal,
    f055ats_f055_adx_trend_strength_dm_minus_378d_base_v109_signal,
    f055ats_f055_adx_trend_strength_dm_minus_504d_base_v110_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v111_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v112_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v113_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v114_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v115_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_base_v116_signal,
    f055ats_f055_adx_trend_strength_dm_minus_189d_base_v117_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_base_v118_signal,
    f055ats_f055_adx_trend_strength_dm_minus_378d_base_v119_signal,
    f055ats_f055_adx_trend_strength_dm_minus_504d_base_v120_signal,
    f055ats_f055_adx_trend_strength_dm_minus_5d_base_v121_signal,
    f055ats_f055_adx_trend_strength_dm_minus_10d_base_v122_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_base_v123_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_base_v124_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_base_v125_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v126_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v127_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v128_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v129_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v130_signal,
    f055ats_f055_adx_trend_strength_adx_126d_base_v131_signal,
    f055ats_f055_adx_trend_strength_adx_189d_base_v132_signal,
    f055ats_f055_adx_trend_strength_adx_252d_base_v133_signal,
    f055ats_f055_adx_trend_strength_adx_378d_base_v134_signal,
    f055ats_f055_adx_trend_strength_adx_504d_base_v135_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v136_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v137_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v138_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v139_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v140_signal,
    f055ats_f055_adx_trend_strength_adx_126d_base_v141_signal,
    f055ats_f055_adx_trend_strength_adx_189d_base_v142_signal,
    f055ats_f055_adx_trend_strength_adx_252d_base_v143_signal,
    f055ats_f055_adx_trend_strength_adx_378d_base_v144_signal,
    f055ats_f055_adx_trend_strength_adx_504d_base_v145_signal,
    f055ats_f055_adx_trend_strength_adx_5d_base_v146_signal,
    f055ats_f055_adx_trend_strength_adx_10d_base_v147_signal,
    f055ats_f055_adx_trend_strength_adx_21d_base_v148_signal,
    f055ats_f055_adx_trend_strength_adx_42d_base_v149_signal,
    f055ats_f055_adx_trend_strength_adx_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F055_ADX_TREND_STRENGTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    cols = {"closeadj": closeadj, "high": high, "low": low}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f055_dm_plus', '_f055_dm_minus', '_f055_adx')
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
    print(f"OK f055_adx_trend_strength_base_076_150_claude: {n_features} features pass")
