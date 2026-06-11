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


# ===== folder domain primitives =====
def _f18_orderflow_proxy(revenue, deferredrev, w):
    combined = revenue + deferredrev
    return combined.pct_change(periods=w) * _mean(combined, w)

def _f18_backlog_buildup(deferredrev, w):
    return deferredrev.pct_change(periods=w) * _mean(deferredrev, w)

def _f18_long_cycle_acceleration(revenue, w):
    g = revenue.pct_change(periods=w)
    return g.diff(periods=w) * _mean(revenue, w)


# ===== features =====
def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v001_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v002_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v003_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v004_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v005_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v006_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v007_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v008_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v009_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v010_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v011_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v012_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v013_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v014_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v015_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v016_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v017_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v018_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v019_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v020_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v021_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v022_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 189) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v023_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v024_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v025_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v026_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v027_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v028_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v029_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v030_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v031_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v032_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 378) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v033_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v034_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 378) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v035_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v036_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v037_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v038_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v039_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v040_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v041_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v042_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 100) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v043_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v044_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 100) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v045_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v046_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 150) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v047_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v048_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 150) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v049_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 150) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v050_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 150) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v051_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v052_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v053_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v054_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v055_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v056_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v057_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v058_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v059_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v060_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v061_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v062_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v063_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v064_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v065_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v066_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v067_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v068_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v069_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v070_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v071_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v072_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 189) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v073_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v074_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v075_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v076_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v077_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v078_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v079_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v080_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v081_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v082_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 378) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v083_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v084_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 378) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v085_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v086_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v087_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v088_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v089_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v090_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v091_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v092_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 100) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v093_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v094_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 100) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v095_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 100) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v096_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 150) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v097_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v098_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 150) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v099_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 150) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v100_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 150) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v101_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v102_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v103_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v104_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v105_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v106_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v107_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v108_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v109_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v110_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v111_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v112_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v113_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v114_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v115_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v116_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v117_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v118_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v119_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v120_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v121_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v122_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 189) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v123_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v124_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v125_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v126_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v127_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v128_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v129_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v130_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v131_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v132_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 378) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v133_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v134_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 378) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v135_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v136_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v137_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v138_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v139_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v140_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v141_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 100) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v142_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 100) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v143_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 100) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v144_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 100) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v145_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 100) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v146_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 150) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v147_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v148_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 150) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v149_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 150) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v150_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 150) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v001_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v002_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v003_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v004_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_slope_v005_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v006_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v007_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v008_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v009_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_slope_v010_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v011_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v012_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v013_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v014_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_slope_v015_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v016_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v017_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v018_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v019_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_126d_slope_v020_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v021_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v022_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v023_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v024_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_189d_slope_v025_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v026_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v027_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v028_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v029_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_252d_slope_v030_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v031_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v032_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v033_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v034_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_378d_slope_v035_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v036_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v037_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v038_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v039_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_504d_slope_v040_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v041_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v042_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v043_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v044_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_100d_slope_v045_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v046_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v047_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v048_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v049_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_150d_slope_v050_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v051_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v052_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v053_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v054_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_slope_v055_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v056_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v057_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v058_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v059_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_slope_v060_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v061_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v062_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v063_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v064_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_slope_v065_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v066_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v067_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v068_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v069_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_126d_slope_v070_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v071_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v072_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v073_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v074_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_189d_slope_v075_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v076_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v077_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v078_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v079_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_252d_slope_v080_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v081_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v082_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v083_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v084_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_378d_slope_v085_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v086_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v087_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v088_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v089_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_504d_slope_v090_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v091_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v092_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v093_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v094_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_100d_slope_v095_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v096_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v097_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v098_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v099_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_150d_slope_v100_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v101_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v102_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v103_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v104_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_slope_v105_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v106_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v107_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v108_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v109_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_slope_v110_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v111_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v112_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v113_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v114_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_slope_v115_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v116_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v117_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v118_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v119_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_126d_slope_v120_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v121_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v122_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v123_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v124_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_189d_slope_v125_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v126_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v127_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v128_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v129_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_252d_slope_v130_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v131_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v132_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v133_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v134_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_378d_slope_v135_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v136_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v137_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v138_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v139_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_504d_slope_v140_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v141_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v142_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v143_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v144_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_100d_slope_v145_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v146_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v147_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v148_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v149_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_150d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_TRANSFORMER_ORDERFLOW_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "capex": capex, "assets": assets,
        "ppnenet": ppnenet, "deferredrev": deferredrev,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f18_orderflow_proxy", "_f18_backlog_buildup", "_f18_long_cycle_acceleration")
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
    print(f"OK f18_transformer_orderflow_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
