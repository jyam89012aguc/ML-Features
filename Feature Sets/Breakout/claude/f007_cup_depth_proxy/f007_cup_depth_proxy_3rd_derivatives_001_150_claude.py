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
def _f007_cup_drawdown(close, w):
    pk = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - pk) / pk.replace(0, np.nan).abs()


def _f007_cup_recovery(close, w):
    tr = close.rolling(w, min_periods=max(1, w // 2)).min()
    pk = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - tr) / (pk - tr).replace(0, np.nan).abs()


def _f007_cup_depth_score(close, w):
    pk = close.rolling(w, min_periods=max(1, w // 2)).max()
    tr = close.rolling(w, min_periods=max(1, w // 2)).min()
    depth = (pk - tr) / pk.replace(0, np.nan).abs()
    rec = (close - tr) / (pk - tr).replace(0, np.nan).abs()
    return depth * rec


# v001-v015: jerk of in-range count × close
def f007cdp_f007_cup_depth_proxy_inrange_21d_jerk_v001_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_21d_jerk_v002_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_42d_jerk_v003_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_42d_jerk_v004_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_63d_jerk_v005_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_63d_jerk_v006_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_126d_jerk_v007_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_126d_jerk_v008_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_252d_jerk_v009_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_252d_jerk_v010_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_504d_jerk_v011_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_504d_jerk_v012_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_189d_jerk_v013_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_378d_jerk_v014_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrange_378d_jerk_v015_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v030: jerk of base length × close
def f007cdp_f007_cup_depth_proxy_blen_21d_jerk_v016_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_21d_jerk_v017_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_42d_jerk_v018_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 42) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_42d_jerk_v019_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 42) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_63d_jerk_v020_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_63d_jerk_v021_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_126d_jerk_v022_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 126) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_126d_jerk_v023_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 126) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_252d_jerk_v024_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_252d_jerk_v025_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_504d_jerk_v026_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_504d_jerk_v027_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_189d_jerk_v028_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 189) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_378d_jerk_v029_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 378) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blen_378d_jerk_v030_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 378) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v045: jerk of consolidation × close
def f007cdp_f007_cup_depth_proxy_consdur_21d_jerk_v031_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_21d_jerk_v032_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_42d_jerk_v033_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 42) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_42d_jerk_v034_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 42) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_63d_jerk_v035_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_63d_jerk_v036_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_126d_jerk_v037_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 126) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_126d_jerk_v038_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 126) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_252d_jerk_v039_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_252d_jerk_v040_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_504d_jerk_v041_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_504d_jerk_v042_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_189d_jerk_v043_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 189) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_378d_jerk_v044_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 378) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consdur_378d_jerk_v045_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 378) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v060: jerk of in-range × volume
def f007cdp_f007_cup_depth_proxy_inrxvol_21d_jerk_v046_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 21) * volume
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_21d_jerk_v047_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 21) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_63d_jerk_v048_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 63) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_63d_jerk_v049_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 63) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_126d_jerk_v050_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 126) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_252d_jerk_v051_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 252) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_252d_jerk_v052_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 252) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_504d_jerk_v053_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 504) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxvol_504d_jerk_v054_signal(closeadj, volume):
    base = _f007_cup_drawdown(closeadj, 504) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_21d_jerk_v055_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 21) * _mean(dv, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_63d_jerk_v056_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 63) * _mean(dv, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_126d_jerk_v057_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 126) * _mean(dv, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_252d_jerk_v058_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 252) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_504d_jerk_v059_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 504) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxdv_504d_jerk_v060_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f007_cup_drawdown(closeadj, 504) * _mean(dv, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v075: jerk of base length × volume
def f007cdp_f007_cup_depth_proxy_blenxvol_21d_jerk_v061_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * volume
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_21d_jerk_v062_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_63d_jerk_v063_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_63d_jerk_v064_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_126d_jerk_v065_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 126) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_252d_jerk_v066_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_252d_jerk_v067_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_504d_jerk_v068_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxvol_504d_jerk_v069_signal(closeadj, volume):
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_21d_jerk_v070_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * _mean(dv, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_63d_jerk_v071_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * _mean(dv, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_126d_jerk_v072_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 126) + 1.0) * _mean(dv, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_252d_jerk_v073_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_504d_jerk_v074_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxdv_504d_jerk_v075_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_recovery(closeadj, 504) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v076-v090: jerk of consolidation × volume
def f007cdp_f007_cup_depth_proxy_consxvol_21d_jerk_v076_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * volume
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_21d_jerk_v077_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_63d_jerk_v078_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_63d_jerk_v079_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_126d_jerk_v080_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 126) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_252d_jerk_v081_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_252d_jerk_v082_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_504d_jerk_v083_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * volume
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxvol_504d_jerk_v084_signal(closeadj, volume):
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * volume
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_21d_jerk_v085_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * _mean(dv, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_63d_jerk_v086_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * _mean(dv, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_126d_jerk_v087_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 126) + 1.0) * _mean(dv, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_252d_jerk_v088_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_504d_jerk_v089_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxdv_504d_jerk_v090_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f007_cup_depth_score(closeadj, 504) + 1.0) * _mean(dv, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v105: jerk of in-range × HL range
def f007cdp_f007_cup_depth_proxy_inrxhlr_21d_jerk_v091_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f007_cup_drawdown(closeadj, 21) * rng
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_21d_jerk_v092_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f007_cup_drawdown(closeadj, 21) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_63d_jerk_v093_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f007_cup_drawdown(closeadj, 63) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_63d_jerk_v094_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f007_cup_drawdown(closeadj, 63) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_126d_jerk_v095_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f007_cup_drawdown(closeadj, 126) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_252d_jerk_v096_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f007_cup_drawdown(closeadj, 252) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrxhlr_252d_jerk_v097_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f007_cup_drawdown(closeadj, 252) * rng
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxhlr_21d_jerk_v098_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = (_f007_cup_recovery(closeadj, 21) + 1.0) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxhlr_63d_jerk_v099_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = (_f007_cup_recovery(closeadj, 63) + 1.0) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxhlr_126d_jerk_v100_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = (_f007_cup_recovery(closeadj, 126) + 1.0) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenxhlr_252d_jerk_v101_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = (_f007_cup_recovery(closeadj, 252) + 1.0) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxhlr_21d_jerk_v102_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = (_f007_cup_depth_score(closeadj, 21) + 1.0) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxhlr_63d_jerk_v103_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = (_f007_cup_depth_score(closeadj, 63) + 1.0) * rng
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxhlr_126d_jerk_v104_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = (_f007_cup_depth_score(closeadj, 126) + 1.0) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consxhlr_252d_jerk_v105_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = (_f007_cup_depth_score(closeadj, 252) + 1.0) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v120: jerk of log(1+...) × close
def f007cdp_f007_cup_depth_proxy_lninr_21d_jerk_v106_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 21)) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_21d_jerk_v107_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 21)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_63d_jerk_v108_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_63d_jerk_v109_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_126d_jerk_v110_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 126)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_252d_jerk_v111_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lninr_504d_jerk_v112_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_drawdown(closeadj, 504)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lnblen_21d_jerk_v113_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_recovery(closeadj, 21)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lnblen_63d_jerk_v114_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_recovery(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lnblen_126d_jerk_v115_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_recovery(closeadj, 126)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lnblen_252d_jerk_v116_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_recovery(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lncons_21d_jerk_v117_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_depth_score(closeadj, 21)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lncons_63d_jerk_v118_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_depth_score(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lncons_126d_jerk_v119_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_depth_score(closeadj, 126)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_lncons_252d_jerk_v120_signal(closeadj):
    base = np.log1p(np.abs(_f007_cup_depth_score(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v135: jerk of EMA-smoothed × close
def f007cdp_f007_cup_depth_proxy_inrema_21d_jerk_v121_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrema_21d_jerk_v122_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrema_63d_jerk_v123_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrema_126d_jerk_v124_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 126).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrema_252d_jerk_v125_signal(closeadj):
    base = _f007_cup_drawdown(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenema_21d_jerk_v126_signal(closeadj):
    base = _f007_cup_recovery(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenema_63d_jerk_v127_signal(closeadj):
    base = _f007_cup_recovery(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenema_126d_jerk_v128_signal(closeadj):
    base = _f007_cup_recovery(closeadj, 126).ewm(span=126, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenema_252d_jerk_v129_signal(closeadj):
    base = _f007_cup_recovery(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consema_21d_jerk_v130_signal(closeadj):
    base = _f007_cup_depth_score(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consema_63d_jerk_v131_signal(closeadj):
    base = _f007_cup_depth_score(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consema_126d_jerk_v132_signal(closeadj):
    base = _f007_cup_depth_score(closeadj, 126).ewm(span=126, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consema_252d_jerk_v133_signal(closeadj):
    base = _f007_cup_depth_score(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj + 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrmean_21d_jerk_v134_signal(closeadj):
    base = _mean(_f007_cup_drawdown(closeadj, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_inrmean_63d_jerk_v135_signal(closeadj):
    base = _mean(_f007_cup_drawdown(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v150: composite jerks
def f007cdp_f007_cup_depth_proxy_blenplusinr_63d_jerk_v136_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 63) + _f007_cup_drawdown(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenplusinr_126d_jerk_v137_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 126) + _f007_cup_drawdown(closeadj, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenplusinr_252d_jerk_v138_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 252) + _f007_cup_drawdown(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consplusinr_63d_jerk_v139_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 63) + _f007_cup_drawdown(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consplusinr_126d_jerk_v140_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 126) + _f007_cup_drawdown(closeadj, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_consplusinr_252d_jerk_v141_signal(closeadj):
    base = (_f007_cup_depth_score(closeadj, 252) + _f007_cup_drawdown(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenpluscons_63d_jerk_v142_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 63) + _f007_cup_depth_score(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenpluscons_126d_jerk_v143_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 126) + _f007_cup_depth_score(closeadj, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_blenpluscons_252d_jerk_v144_signal(closeadj):
    base = (_f007_cup_recovery(closeadj, 252) + _f007_cup_depth_score(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtinr_63d_jerk_v145_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_drawdown(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtinr_252d_jerk_v146_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_drawdown(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtblen_63d_jerk_v147_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_recovery(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtblen_252d_jerk_v148_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_recovery(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtcons_63d_jerk_v149_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_depth_score(closeadj, 63)) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f007cdp_f007_cup_depth_proxy_sqrtcons_252d_jerk_v150_signal(closeadj):
    base = np.sqrt(np.abs(_f007_cup_depth_score(closeadj, 252)) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f007cdp_f007_cup_depth_proxy_inrange_21d_jerk_v001_signal,
    f007cdp_f007_cup_depth_proxy_inrange_21d_jerk_v002_signal,
    f007cdp_f007_cup_depth_proxy_inrange_42d_jerk_v003_signal,
    f007cdp_f007_cup_depth_proxy_inrange_42d_jerk_v004_signal,
    f007cdp_f007_cup_depth_proxy_inrange_63d_jerk_v005_signal,
    f007cdp_f007_cup_depth_proxy_inrange_63d_jerk_v006_signal,
    f007cdp_f007_cup_depth_proxy_inrange_126d_jerk_v007_signal,
    f007cdp_f007_cup_depth_proxy_inrange_126d_jerk_v008_signal,
    f007cdp_f007_cup_depth_proxy_inrange_252d_jerk_v009_signal,
    f007cdp_f007_cup_depth_proxy_inrange_252d_jerk_v010_signal,
    f007cdp_f007_cup_depth_proxy_inrange_504d_jerk_v011_signal,
    f007cdp_f007_cup_depth_proxy_inrange_504d_jerk_v012_signal,
    f007cdp_f007_cup_depth_proxy_inrange_189d_jerk_v013_signal,
    f007cdp_f007_cup_depth_proxy_inrange_378d_jerk_v014_signal,
    f007cdp_f007_cup_depth_proxy_inrange_378d_jerk_v015_signal,
    f007cdp_f007_cup_depth_proxy_blen_21d_jerk_v016_signal,
    f007cdp_f007_cup_depth_proxy_blen_21d_jerk_v017_signal,
    f007cdp_f007_cup_depth_proxy_blen_42d_jerk_v018_signal,
    f007cdp_f007_cup_depth_proxy_blen_42d_jerk_v019_signal,
    f007cdp_f007_cup_depth_proxy_blen_63d_jerk_v020_signal,
    f007cdp_f007_cup_depth_proxy_blen_63d_jerk_v021_signal,
    f007cdp_f007_cup_depth_proxy_blen_126d_jerk_v022_signal,
    f007cdp_f007_cup_depth_proxy_blen_126d_jerk_v023_signal,
    f007cdp_f007_cup_depth_proxy_blen_252d_jerk_v024_signal,
    f007cdp_f007_cup_depth_proxy_blen_252d_jerk_v025_signal,
    f007cdp_f007_cup_depth_proxy_blen_504d_jerk_v026_signal,
    f007cdp_f007_cup_depth_proxy_blen_504d_jerk_v027_signal,
    f007cdp_f007_cup_depth_proxy_blen_189d_jerk_v028_signal,
    f007cdp_f007_cup_depth_proxy_blen_378d_jerk_v029_signal,
    f007cdp_f007_cup_depth_proxy_blen_378d_jerk_v030_signal,
    f007cdp_f007_cup_depth_proxy_consdur_21d_jerk_v031_signal,
    f007cdp_f007_cup_depth_proxy_consdur_21d_jerk_v032_signal,
    f007cdp_f007_cup_depth_proxy_consdur_42d_jerk_v033_signal,
    f007cdp_f007_cup_depth_proxy_consdur_42d_jerk_v034_signal,
    f007cdp_f007_cup_depth_proxy_consdur_63d_jerk_v035_signal,
    f007cdp_f007_cup_depth_proxy_consdur_63d_jerk_v036_signal,
    f007cdp_f007_cup_depth_proxy_consdur_126d_jerk_v037_signal,
    f007cdp_f007_cup_depth_proxy_consdur_126d_jerk_v038_signal,
    f007cdp_f007_cup_depth_proxy_consdur_252d_jerk_v039_signal,
    f007cdp_f007_cup_depth_proxy_consdur_252d_jerk_v040_signal,
    f007cdp_f007_cup_depth_proxy_consdur_504d_jerk_v041_signal,
    f007cdp_f007_cup_depth_proxy_consdur_504d_jerk_v042_signal,
    f007cdp_f007_cup_depth_proxy_consdur_189d_jerk_v043_signal,
    f007cdp_f007_cup_depth_proxy_consdur_378d_jerk_v044_signal,
    f007cdp_f007_cup_depth_proxy_consdur_378d_jerk_v045_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_21d_jerk_v046_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_21d_jerk_v047_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_63d_jerk_v048_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_63d_jerk_v049_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_126d_jerk_v050_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_252d_jerk_v051_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_252d_jerk_v052_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_504d_jerk_v053_signal,
    f007cdp_f007_cup_depth_proxy_inrxvol_504d_jerk_v054_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_21d_jerk_v055_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_63d_jerk_v056_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_126d_jerk_v057_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_252d_jerk_v058_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_504d_jerk_v059_signal,
    f007cdp_f007_cup_depth_proxy_inrxdv_504d_jerk_v060_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_21d_jerk_v061_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_21d_jerk_v062_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_63d_jerk_v063_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_63d_jerk_v064_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_126d_jerk_v065_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_252d_jerk_v066_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_252d_jerk_v067_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_504d_jerk_v068_signal,
    f007cdp_f007_cup_depth_proxy_blenxvol_504d_jerk_v069_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_21d_jerk_v070_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_63d_jerk_v071_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_126d_jerk_v072_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_252d_jerk_v073_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_504d_jerk_v074_signal,
    f007cdp_f007_cup_depth_proxy_blenxdv_504d_jerk_v075_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_21d_jerk_v076_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_21d_jerk_v077_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_63d_jerk_v078_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_63d_jerk_v079_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_126d_jerk_v080_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_252d_jerk_v081_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_252d_jerk_v082_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_504d_jerk_v083_signal,
    f007cdp_f007_cup_depth_proxy_consxvol_504d_jerk_v084_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_21d_jerk_v085_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_63d_jerk_v086_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_126d_jerk_v087_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_252d_jerk_v088_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_504d_jerk_v089_signal,
    f007cdp_f007_cup_depth_proxy_consxdv_504d_jerk_v090_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_21d_jerk_v091_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_21d_jerk_v092_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_63d_jerk_v093_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_63d_jerk_v094_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_126d_jerk_v095_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_252d_jerk_v096_signal,
    f007cdp_f007_cup_depth_proxy_inrxhlr_252d_jerk_v097_signal,
    f007cdp_f007_cup_depth_proxy_blenxhlr_21d_jerk_v098_signal,
    f007cdp_f007_cup_depth_proxy_blenxhlr_63d_jerk_v099_signal,
    f007cdp_f007_cup_depth_proxy_blenxhlr_126d_jerk_v100_signal,
    f007cdp_f007_cup_depth_proxy_blenxhlr_252d_jerk_v101_signal,
    f007cdp_f007_cup_depth_proxy_consxhlr_21d_jerk_v102_signal,
    f007cdp_f007_cup_depth_proxy_consxhlr_63d_jerk_v103_signal,
    f007cdp_f007_cup_depth_proxy_consxhlr_126d_jerk_v104_signal,
    f007cdp_f007_cup_depth_proxy_consxhlr_252d_jerk_v105_signal,
    f007cdp_f007_cup_depth_proxy_lninr_21d_jerk_v106_signal,
    f007cdp_f007_cup_depth_proxy_lninr_21d_jerk_v107_signal,
    f007cdp_f007_cup_depth_proxy_lninr_63d_jerk_v108_signal,
    f007cdp_f007_cup_depth_proxy_lninr_63d_jerk_v109_signal,
    f007cdp_f007_cup_depth_proxy_lninr_126d_jerk_v110_signal,
    f007cdp_f007_cup_depth_proxy_lninr_252d_jerk_v111_signal,
    f007cdp_f007_cup_depth_proxy_lninr_504d_jerk_v112_signal,
    f007cdp_f007_cup_depth_proxy_lnblen_21d_jerk_v113_signal,
    f007cdp_f007_cup_depth_proxy_lnblen_63d_jerk_v114_signal,
    f007cdp_f007_cup_depth_proxy_lnblen_126d_jerk_v115_signal,
    f007cdp_f007_cup_depth_proxy_lnblen_252d_jerk_v116_signal,
    f007cdp_f007_cup_depth_proxy_lncons_21d_jerk_v117_signal,
    f007cdp_f007_cup_depth_proxy_lncons_63d_jerk_v118_signal,
    f007cdp_f007_cup_depth_proxy_lncons_126d_jerk_v119_signal,
    f007cdp_f007_cup_depth_proxy_lncons_252d_jerk_v120_signal,
    f007cdp_f007_cup_depth_proxy_inrema_21d_jerk_v121_signal,
    f007cdp_f007_cup_depth_proxy_inrema_21d_jerk_v122_signal,
    f007cdp_f007_cup_depth_proxy_inrema_63d_jerk_v123_signal,
    f007cdp_f007_cup_depth_proxy_inrema_126d_jerk_v124_signal,
    f007cdp_f007_cup_depth_proxy_inrema_252d_jerk_v125_signal,
    f007cdp_f007_cup_depth_proxy_blenema_21d_jerk_v126_signal,
    f007cdp_f007_cup_depth_proxy_blenema_63d_jerk_v127_signal,
    f007cdp_f007_cup_depth_proxy_blenema_126d_jerk_v128_signal,
    f007cdp_f007_cup_depth_proxy_blenema_252d_jerk_v129_signal,
    f007cdp_f007_cup_depth_proxy_consema_21d_jerk_v130_signal,
    f007cdp_f007_cup_depth_proxy_consema_63d_jerk_v131_signal,
    f007cdp_f007_cup_depth_proxy_consema_126d_jerk_v132_signal,
    f007cdp_f007_cup_depth_proxy_consema_252d_jerk_v133_signal,
    f007cdp_f007_cup_depth_proxy_inrmean_21d_jerk_v134_signal,
    f007cdp_f007_cup_depth_proxy_inrmean_63d_jerk_v135_signal,
    f007cdp_f007_cup_depth_proxy_blenplusinr_63d_jerk_v136_signal,
    f007cdp_f007_cup_depth_proxy_blenplusinr_126d_jerk_v137_signal,
    f007cdp_f007_cup_depth_proxy_blenplusinr_252d_jerk_v138_signal,
    f007cdp_f007_cup_depth_proxy_consplusinr_63d_jerk_v139_signal,
    f007cdp_f007_cup_depth_proxy_consplusinr_126d_jerk_v140_signal,
    f007cdp_f007_cup_depth_proxy_consplusinr_252d_jerk_v141_signal,
    f007cdp_f007_cup_depth_proxy_blenpluscons_63d_jerk_v142_signal,
    f007cdp_f007_cup_depth_proxy_blenpluscons_126d_jerk_v143_signal,
    f007cdp_f007_cup_depth_proxy_blenpluscons_252d_jerk_v144_signal,
    f007cdp_f007_cup_depth_proxy_sqrtinr_63d_jerk_v145_signal,
    f007cdp_f007_cup_depth_proxy_sqrtinr_252d_jerk_v146_signal,
    f007cdp_f007_cup_depth_proxy_sqrtblen_63d_jerk_v147_signal,
    f007cdp_f007_cup_depth_proxy_sqrtblen_252d_jerk_v148_signal,
    f007cdp_f007_cup_depth_proxy_sqrtcons_63d_jerk_v149_signal,
    f007cdp_f007_cup_depth_proxy_sqrtcons_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F007_CUP_DEPTH_PROXY_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f007_cup_drawdown", "_f007_cup_recovery", "_f007_cup_depth_score")
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
    print(f"OK f007_cup_depth_proxy_3rd_derivatives_001_150_claude: {n_features} features pass")
