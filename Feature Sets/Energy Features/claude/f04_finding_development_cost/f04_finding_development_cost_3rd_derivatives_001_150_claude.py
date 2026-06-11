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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f04_fd_cost_proxy(capex, assets, w):
    ag = (assets - assets.shift(w)) / assets.shift(w).replace(0, np.nan).abs()
    cx = capex.rolling(w, min_periods=max(1, w // 2)).sum()
    return cx / (assets * ag.abs()).replace(0, np.nan)


def _f04_fd_efficiency(capex, assets, w):
    cx = capex.rolling(w, min_periods=max(1, w // 2)).sum()
    ag = (assets - assets.shift(w))
    return ag / cx.replace(0, np.nan)


def _f04_reserve_replacement(capex, depamor, w):
    cx = capex.rolling(w, min_periods=max(1, w // 2)).sum()
    da = depamor.rolling(w, min_periods=max(1, w // 2)).sum()
    return cx / da.replace(0, np.nan)

# ===== features =====

def f04fdc_f04_finding_development_cost_fdcp_ema63_xclose_5d_jerk_v001_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseema21_5d_jerk_v002_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseema63_5d_jerk_v003_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose21_5d_jerk_v004_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose63_5d_jerk_v005_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose252_5d_jerk_v006_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xstdclose63_5d_jerk_v007_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xstdclose252_5d_jerk_v008_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xzclose63_5d_jerk_v009_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xzclose252_5d_jerk_v010_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret5_5d_jerk_v011_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret21_5d_jerk_v012_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret63_5d_jerk_v013_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xclosediff21_5d_jerk_v014_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema63_xclosediff63_5d_jerk_v015_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 63)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xclose_5d_jerk_v016_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseema21_5d_jerk_v017_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseema63_5d_jerk_v018_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose21_5d_jerk_v019_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose63_5d_jerk_v020_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose252_5d_jerk_v021_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xstdclose63_5d_jerk_v022_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xstdclose252_5d_jerk_v023_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xzclose63_5d_jerk_v024_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xzclose252_5d_jerk_v025_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret5_5d_jerk_v026_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret21_5d_jerk_v027_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret63_5d_jerk_v028_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xclosediff21_5d_jerk_v029_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema126_xclosediff63_5d_jerk_v030_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 126)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xclose_5d_jerk_v031_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseema21_5d_jerk_v032_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseema63_5d_jerk_v033_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose21_5d_jerk_v034_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose63_5d_jerk_v035_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose252_5d_jerk_v036_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xstdclose63_5d_jerk_v037_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xstdclose252_5d_jerk_v038_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xzclose63_5d_jerk_v039_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xzclose252_5d_jerk_v040_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret5_5d_jerk_v041_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret21_5d_jerk_v042_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret63_5d_jerk_v043_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xclosediff21_5d_jerk_v044_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_ema252_xclosediff63_5d_jerk_v045_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_ema(x0, 252)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xclose_5d_jerk_v046_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xcloseema21_5d_jerk_v047_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xcloseema63_5d_jerk_v048_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose21_5d_jerk_v049_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose63_5d_jerk_v050_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose252_5d_jerk_v051_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xstdclose63_5d_jerk_v052_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xstdclose252_5d_jerk_v053_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xzclose63_5d_jerk_v054_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xzclose252_5d_jerk_v055_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret5_5d_jerk_v056_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret21_5d_jerk_v057_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret63_5d_jerk_v058_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xclosediff21_5d_jerk_v059_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z63_xclosediff63_5d_jerk_v060_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 63)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xclose_5d_jerk_v061_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xcloseema21_5d_jerk_v062_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xcloseema63_5d_jerk_v063_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose21_5d_jerk_v064_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose63_5d_jerk_v065_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose252_5d_jerk_v066_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xstdclose63_5d_jerk_v067_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xstdclose252_5d_jerk_v068_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xzclose63_5d_jerk_v069_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xzclose252_5d_jerk_v070_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret5_5d_jerk_v071_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret21_5d_jerk_v072_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret63_5d_jerk_v073_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xclosediff21_5d_jerk_v074_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z126_xclosediff63_5d_jerk_v075_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 126)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xclose_5d_jerk_v076_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xcloseema21_5d_jerk_v077_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xcloseema63_5d_jerk_v078_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose21_5d_jerk_v079_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose63_5d_jerk_v080_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose252_5d_jerk_v081_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xstdclose63_5d_jerk_v082_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xstdclose252_5d_jerk_v083_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xzclose63_5d_jerk_v084_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xzclose252_5d_jerk_v085_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret5_5d_jerk_v086_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret21_5d_jerk_v087_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret63_5d_jerk_v088_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xclosediff21_5d_jerk_v089_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z252_xclosediff63_5d_jerk_v090_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 252)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xclose_5d_jerk_v091_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xcloseema21_5d_jerk_v092_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xcloseema63_5d_jerk_v093_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose21_5d_jerk_v094_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose63_5d_jerk_v095_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose252_5d_jerk_v096_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xstdclose63_5d_jerk_v097_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xstdclose252_5d_jerk_v098_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xzclose63_5d_jerk_v099_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xzclose252_5d_jerk_v100_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret5_5d_jerk_v101_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret21_5d_jerk_v102_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret63_5d_jerk_v103_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xclosediff21_5d_jerk_v104_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_z504_xclosediff63_5d_jerk_v105_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = (_z(x0, 504)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xclose_5d_jerk_v106_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xcloseema21_5d_jerk_v107_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xcloseema63_5d_jerk_v108_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose21_5d_jerk_v109_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose63_5d_jerk_v110_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose252_5d_jerk_v111_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xstdclose63_5d_jerk_v112_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xstdclose252_5d_jerk_v113_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xzclose63_5d_jerk_v114_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xzclose252_5d_jerk_v115_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret5_5d_jerk_v116_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret21_5d_jerk_v117_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret63_5d_jerk_v118_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xclosediff21_5d_jerk_v119_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_abs_xclosediff63_5d_jerk_v120_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).abs()) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xclose_5d_jerk_v121_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xcloseema21_5d_jerk_v122_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xcloseema63_5d_jerk_v123_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose21_5d_jerk_v124_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose63_5d_jerk_v125_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose252_5d_jerk_v126_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xstdclose63_5d_jerk_v127_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xstdclose252_5d_jerk_v128_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xzclose63_5d_jerk_v129_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xzclose252_5d_jerk_v130_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret5_5d_jerk_v131_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret21_5d_jerk_v132_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret63_5d_jerk_v133_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xclosediff21_5d_jerk_v134_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_sq_xclosediff63_5d_jerk_v135_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0) * (x0).abs()) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xclose_5d_jerk_v136_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseema21_5d_jerk_v137_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _ema(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseema63_5d_jerk_v138_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _ema(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose21_5d_jerk_v139_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose63_5d_jerk_v140_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose252_5d_jerk_v141_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xstdclose63_5d_jerk_v142_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xstdclose252_5d_jerk_v143_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * _std(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xzclose63_5d_jerk_v144_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (1 + _z(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xzclose252_5d_jerk_v145_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (1 + _z(closeadj, 252))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret5_5d_jerk_v146_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (closeadj / closeadj.shift(5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret21_5d_jerk_v147_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (closeadj / closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret63_5d_jerk_v148_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (closeadj / closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xclosediff21_5d_jerk_v149_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (closeadj - closeadj.shift(21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04fdc_f04_finding_development_cost_fdcp_diff21_xclosediff63_5d_jerk_v150_signal(capex, assets, closeadj):
    x0 = _f04_fd_cost_proxy(capex, assets, 5)
    base = ((x0).diff(21)) * (closeadj - closeadj.shift(63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04fdc_f04_finding_development_cost_fdcp_ema63_xclose_5d_jerk_v001_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseema21_5d_jerk_v002_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseema63_5d_jerk_v003_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose21_5d_jerk_v004_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose63_5d_jerk_v005_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xmeanclose252_5d_jerk_v006_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xstdclose63_5d_jerk_v007_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xstdclose252_5d_jerk_v008_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xzclose63_5d_jerk_v009_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xzclose252_5d_jerk_v010_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret5_5d_jerk_v011_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret21_5d_jerk_v012_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xcloseret63_5d_jerk_v013_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xclosediff21_5d_jerk_v014_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema63_xclosediff63_5d_jerk_v015_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xclose_5d_jerk_v016_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseema21_5d_jerk_v017_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseema63_5d_jerk_v018_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose21_5d_jerk_v019_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose63_5d_jerk_v020_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xmeanclose252_5d_jerk_v021_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xstdclose63_5d_jerk_v022_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xstdclose252_5d_jerk_v023_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xzclose63_5d_jerk_v024_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xzclose252_5d_jerk_v025_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret5_5d_jerk_v026_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret21_5d_jerk_v027_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xcloseret63_5d_jerk_v028_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xclosediff21_5d_jerk_v029_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema126_xclosediff63_5d_jerk_v030_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xclose_5d_jerk_v031_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseema21_5d_jerk_v032_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseema63_5d_jerk_v033_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose21_5d_jerk_v034_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose63_5d_jerk_v035_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xmeanclose252_5d_jerk_v036_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xstdclose63_5d_jerk_v037_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xstdclose252_5d_jerk_v038_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xzclose63_5d_jerk_v039_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xzclose252_5d_jerk_v040_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret5_5d_jerk_v041_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret21_5d_jerk_v042_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xcloseret63_5d_jerk_v043_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xclosediff21_5d_jerk_v044_signal,
    f04fdc_f04_finding_development_cost_fdcp_ema252_xclosediff63_5d_jerk_v045_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xclose_5d_jerk_v046_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xcloseema21_5d_jerk_v047_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xcloseema63_5d_jerk_v048_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose21_5d_jerk_v049_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose63_5d_jerk_v050_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xmeanclose252_5d_jerk_v051_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xstdclose63_5d_jerk_v052_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xstdclose252_5d_jerk_v053_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xzclose63_5d_jerk_v054_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xzclose252_5d_jerk_v055_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret5_5d_jerk_v056_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret21_5d_jerk_v057_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xcloseret63_5d_jerk_v058_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xclosediff21_5d_jerk_v059_signal,
    f04fdc_f04_finding_development_cost_fdcp_z63_xclosediff63_5d_jerk_v060_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xclose_5d_jerk_v061_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xcloseema21_5d_jerk_v062_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xcloseema63_5d_jerk_v063_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose21_5d_jerk_v064_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose63_5d_jerk_v065_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xmeanclose252_5d_jerk_v066_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xstdclose63_5d_jerk_v067_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xstdclose252_5d_jerk_v068_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xzclose63_5d_jerk_v069_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xzclose252_5d_jerk_v070_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret5_5d_jerk_v071_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret21_5d_jerk_v072_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xcloseret63_5d_jerk_v073_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xclosediff21_5d_jerk_v074_signal,
    f04fdc_f04_finding_development_cost_fdcp_z126_xclosediff63_5d_jerk_v075_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xclose_5d_jerk_v076_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xcloseema21_5d_jerk_v077_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xcloseema63_5d_jerk_v078_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose21_5d_jerk_v079_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose63_5d_jerk_v080_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xmeanclose252_5d_jerk_v081_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xstdclose63_5d_jerk_v082_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xstdclose252_5d_jerk_v083_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xzclose63_5d_jerk_v084_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xzclose252_5d_jerk_v085_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret5_5d_jerk_v086_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret21_5d_jerk_v087_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xcloseret63_5d_jerk_v088_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xclosediff21_5d_jerk_v089_signal,
    f04fdc_f04_finding_development_cost_fdcp_z252_xclosediff63_5d_jerk_v090_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xclose_5d_jerk_v091_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xcloseema21_5d_jerk_v092_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xcloseema63_5d_jerk_v093_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose21_5d_jerk_v094_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose63_5d_jerk_v095_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xmeanclose252_5d_jerk_v096_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xstdclose63_5d_jerk_v097_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xstdclose252_5d_jerk_v098_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xzclose63_5d_jerk_v099_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xzclose252_5d_jerk_v100_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret5_5d_jerk_v101_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret21_5d_jerk_v102_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xcloseret63_5d_jerk_v103_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xclosediff21_5d_jerk_v104_signal,
    f04fdc_f04_finding_development_cost_fdcp_z504_xclosediff63_5d_jerk_v105_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xclose_5d_jerk_v106_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xcloseema21_5d_jerk_v107_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xcloseema63_5d_jerk_v108_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose21_5d_jerk_v109_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose63_5d_jerk_v110_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xmeanclose252_5d_jerk_v111_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xstdclose63_5d_jerk_v112_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xstdclose252_5d_jerk_v113_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xzclose63_5d_jerk_v114_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xzclose252_5d_jerk_v115_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret5_5d_jerk_v116_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret21_5d_jerk_v117_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xcloseret63_5d_jerk_v118_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xclosediff21_5d_jerk_v119_signal,
    f04fdc_f04_finding_development_cost_fdcp_abs_xclosediff63_5d_jerk_v120_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xclose_5d_jerk_v121_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xcloseema21_5d_jerk_v122_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xcloseema63_5d_jerk_v123_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose21_5d_jerk_v124_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose63_5d_jerk_v125_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xmeanclose252_5d_jerk_v126_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xstdclose63_5d_jerk_v127_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xstdclose252_5d_jerk_v128_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xzclose63_5d_jerk_v129_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xzclose252_5d_jerk_v130_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret5_5d_jerk_v131_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret21_5d_jerk_v132_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xcloseret63_5d_jerk_v133_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xclosediff21_5d_jerk_v134_signal,
    f04fdc_f04_finding_development_cost_fdcp_sq_xclosediff63_5d_jerk_v135_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xclose_5d_jerk_v136_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseema21_5d_jerk_v137_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseema63_5d_jerk_v138_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose21_5d_jerk_v139_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose63_5d_jerk_v140_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xmeanclose252_5d_jerk_v141_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xstdclose63_5d_jerk_v142_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xstdclose252_5d_jerk_v143_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xzclose63_5d_jerk_v144_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xzclose252_5d_jerk_v145_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret5_5d_jerk_v146_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret21_5d_jerk_v147_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xcloseret63_5d_jerk_v148_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xclosediff21_5d_jerk_v149_signal,
    f04fdc_f04_finding_development_cost_fdcp_diff21_xclosediff63_5d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_FINDING_DEVELOPMENT_COST_REGISTRY_JERK_001_150 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_fd_cost_proxy", "_f04_fd_efficiency", "_f04_reserve_replacement")
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
    print(f"OK f04_finding_development_cost_3rd_derivatives_001_150_claude: {n_features} features pass")
