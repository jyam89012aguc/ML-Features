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
def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v001_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v002_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v003_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v004_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v005_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v006_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v007_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v008_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v009_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v010_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v011_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v012_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v013_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v014_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v015_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v016_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v017_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v018_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v019_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v020_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v021_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v022_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v023_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v024_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v025_signal(revenue, deferredrev, closeadj):
    base = _f18_orderflow_proxy(revenue, deferredrev, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v026_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v027_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v028_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v029_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v030_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v031_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v032_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v033_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v034_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v035_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v036_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v037_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v038_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v039_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v040_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v041_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v042_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v043_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v044_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v045_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v046_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v047_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v048_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v049_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v050_signal(deferredrev, closeadj):
    base = _f18_backlog_buildup(deferredrev, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v051_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v052_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v053_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v054_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v055_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v056_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v057_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v058_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v059_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v060_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v061_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v062_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v063_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v064_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v065_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v066_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v067_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v068_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v069_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v070_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v071_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v072_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v073_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v074_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v075_signal(revenue, closeadj):
    base = _f18_long_cycle_acceleration(revenue, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v001_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v002_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v003_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v004_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_5d_base_v005_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v006_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v007_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v008_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v009_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_10d_base_v010_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v011_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v012_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v013_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v014_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_21d_base_v015_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v016_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v017_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v018_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v019_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_42d_base_v020_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v021_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v022_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v023_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v024_signal,
    f18tof_f18_transformer_orderflow_proxy_orderflow_proxy_63d_base_v025_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v026_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v027_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v028_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v029_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_5d_base_v030_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v031_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v032_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v033_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v034_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_10d_base_v035_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v036_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v037_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v038_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v039_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_21d_base_v040_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v041_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v042_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v043_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v044_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_42d_base_v045_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v046_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v047_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v048_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v049_signal,
    f18tof_f18_transformer_orderflow_proxy_backlog_buildup_63d_base_v050_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v051_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v052_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v053_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v054_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_5d_base_v055_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v056_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v057_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v058_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v059_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_10d_base_v060_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v061_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v062_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v063_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v064_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_21d_base_v065_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v066_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v067_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v068_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v069_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_42d_base_v070_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v071_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v072_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v073_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v074_signal,
    f18tof_f18_transformer_orderflow_proxy_long_cycle_acceleration_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_TRANSFORMER_ORDERFLOW_PROXY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_transformer_orderflow_proxy_base_001_075_claude: {n_features} features pass")
