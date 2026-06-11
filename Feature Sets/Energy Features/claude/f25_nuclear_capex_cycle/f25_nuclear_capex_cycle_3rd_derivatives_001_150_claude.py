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
def _f25_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f25_capex_cycle(capex, assets, w):
    ratio = capex / assets.replace(0, np.nan).abs()
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return ratio - m


def _f25_capex_quality(capex, depamor, w):
    return (capex / depamor.replace(0, np.nan).abs()).rolling(w, min_periods=max(1, w // 2)).mean()


def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v001_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v002_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v003_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v004_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v005_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v006_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v007_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v008_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v009_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v010_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v011_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v012_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v013_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v014_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v015_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v016_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v017_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v018_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v019_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v020_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v021_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v022_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v023_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v024_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v025_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v026_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v027_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v028_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v029_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v030_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v031_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v032_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v033_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v034_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v035_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v036_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v037_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v038_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v039_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v040_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v041_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v042_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v043_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v044_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v045_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v046_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v047_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v048_signal(capex, revenue, closeadj):
    base = _f25_capex_intensity(capex, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v049_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v050_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v051_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v052_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v053_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v054_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v055_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v056_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v057_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v058_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v059_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v060_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * closeadj / 100.0))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v061_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v062_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v063_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v064_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v065_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v066_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v067_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v068_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v069_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v070_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v071_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v072_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v073_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v074_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v075_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v076_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v077_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v078_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v079_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v080_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v081_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v082_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v083_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v084_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v085_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v086_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v087_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v088_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v089_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v090_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v091_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v092_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v093_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v094_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v095_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v096_signal(capex, revenue, closeadj):
    base = (np.log1p(_f25_capex_intensity(capex, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v097_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v098_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v099_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v100_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v101_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v102_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v103_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v104_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v105_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v106_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v107_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v108_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v109_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v110_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v111_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v112_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v113_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v114_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v115_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v116_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v117_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v118_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v119_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v120_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v121_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v122_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v123_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v124_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v125_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v126_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v127_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v128_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v129_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v130_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v131_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v132_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v133_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v134_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v135_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v136_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v137_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v138_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v139_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v140_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v141_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v142_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v143_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v144_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v145_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v146_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v147_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v148_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v149_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v150_signal(capex, revenue, closeadj):
    base = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v001_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v002_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v003_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v004_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v005_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v006_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v007_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v008_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v009_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v010_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v011_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v012_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v013_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v014_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v015_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v016_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v017_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v018_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v019_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v020_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v021_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v022_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v023_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v024_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v025_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v026_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v027_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v028_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v029_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v030_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v031_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v032_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v033_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v034_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v035_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v036_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v037_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v038_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v039_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v040_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v041_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v042_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v043_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v044_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v045_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v046_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v047_signal,
    f25ncc_f25_nuclear_capex_cycle_capint_21d_jerk_v048_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v049_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v050_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v051_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v052_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v053_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v054_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v055_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v056_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v057_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v058_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v059_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v060_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v061_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v062_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v063_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v064_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v065_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v066_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v067_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v068_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v069_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v070_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v071_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v072_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v073_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v074_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v075_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v076_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v077_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v078_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v079_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v080_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v081_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v082_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v083_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v084_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v085_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v086_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v087_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v088_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v089_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v090_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v091_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v092_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v093_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v094_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v095_signal,
    f25ncc_f25_nuclear_capex_cycle_capintlog_21d_jerk_v096_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v097_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v098_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v099_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v100_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v101_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v102_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v103_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v104_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v105_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v106_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v107_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v108_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v109_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v110_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v111_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v112_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v113_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v114_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v115_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v116_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v117_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v118_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v119_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v120_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v121_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v122_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v123_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v124_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v125_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v126_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v127_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v128_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v129_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v130_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v131_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v132_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v133_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v134_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v135_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v136_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v137_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v138_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v139_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v140_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v141_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v142_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v143_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_jerk_v144_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v145_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v146_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v147_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v148_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v149_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_NUCLEAR_CAPEX_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "capex": capex,
        "depamor": depamor,
        "cor": cor,
        "assets": assets,
        "inventory": inventory,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f25_capex_intensity', '_f25_capex_cycle', '_f25_capex_quality')
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
    print(f"OK f25_nuclear_capex_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
