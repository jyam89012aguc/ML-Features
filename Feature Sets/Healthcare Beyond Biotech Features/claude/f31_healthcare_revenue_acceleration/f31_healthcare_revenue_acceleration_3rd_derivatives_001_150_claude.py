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


def _ema(s, w):
    return s.ewm(span=w, adjust=False).mean()


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
def _f31_revenue_growth_accel(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f31_acceleration_persistence(revenue, w):
    g = revenue.pct_change(periods=w)
    a = g - g.shift(w)
    return _mean(a, w) / _std(a, w).replace(0, np.nan)


def _f31_growth_quality(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return _mean(eg - rg, w)

def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_mean_5d_xc_jerk_v001_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_mean_21d_xmc_jerk_v002_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_std_5d_xc_jerk_v003_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_std_21d_xmc_jerk_v004_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_ema_5d_xc_jerk_v005_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_ema_21d_xmc_jerk_v006_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_z_5d_xc_jerk_v007_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_z_21d_xmc_jerk_v008_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_log_5d_xc_jerk_v009_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_log_21d_xmc_jerk_v010_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_mean_5d_xc_jerk_v011_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_mean_21d_xmc_jerk_v012_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_std_5d_xc_jerk_v013_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_std_21d_xmc_jerk_v014_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_ema_5d_xc_jerk_v015_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_ema_21d_xmc_jerk_v016_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_z_5d_xc_jerk_v017_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_z_21d_xmc_jerk_v018_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_log_5d_xc_jerk_v019_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_log_21d_xmc_jerk_v020_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_mean_5d_xc_jerk_v021_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_mean_21d_xmc_jerk_v022_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_std_5d_xc_jerk_v023_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_std_21d_xmc_jerk_v024_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_ema_5d_xc_jerk_v025_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_ema_21d_xmc_jerk_v026_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_z_5d_xc_jerk_v027_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_z_21d_xmc_jerk_v028_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_log_5d_xc_jerk_v029_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_log_21d_xmc_jerk_v030_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_mean_5d_xc_jerk_v031_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_mean_21d_xmc_jerk_v032_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_std_5d_xc_jerk_v033_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_std_21d_xmc_jerk_v034_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_ema_5d_xc_jerk_v035_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_ema_21d_xmc_jerk_v036_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_z_5d_xc_jerk_v037_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_z_21d_xmc_jerk_v038_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_log_5d_xc_jerk_v039_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_log_21d_xmc_jerk_v040_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_mean_5d_xc_jerk_v041_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_mean_21d_xmc_jerk_v042_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_std_5d_xc_jerk_v043_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_std_21d_xmc_jerk_v044_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_ema_5d_xc_jerk_v045_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_ema_21d_xmc_jerk_v046_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_z_5d_xc_jerk_v047_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_z_21d_xmc_jerk_v048_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_log_5d_xc_jerk_v049_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_log_21d_xmc_jerk_v050_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_mean_5d_xc_jerk_v051_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_mean_21d_xmc_jerk_v052_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_std_5d_xc_jerk_v053_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_std_21d_xmc_jerk_v054_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_ema_5d_xc_jerk_v055_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_ema_21d_xmc_jerk_v056_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_z_5d_xc_jerk_v057_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_z_21d_xmc_jerk_v058_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_log_5d_xc_jerk_v059_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_5d_log_21d_xmc_jerk_v060_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_mean_5d_xc_jerk_v061_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_mean_21d_xmc_jerk_v062_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_std_5d_xc_jerk_v063_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_std_21d_xmc_jerk_v064_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_ema_5d_xc_jerk_v065_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_ema_21d_xmc_jerk_v066_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_z_5d_xc_jerk_v067_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_z_21d_xmc_jerk_v068_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_log_5d_xc_jerk_v069_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_10d_log_21d_xmc_jerk_v070_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_mean_5d_xc_jerk_v071_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_mean_21d_xmc_jerk_v072_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_std_5d_xc_jerk_v073_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_std_21d_xmc_jerk_v074_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_ema_5d_xc_jerk_v075_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_ema_21d_xmc_jerk_v076_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_z_5d_xc_jerk_v077_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_z_21d_xmc_jerk_v078_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_log_5d_xc_jerk_v079_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_log_21d_xmc_jerk_v080_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_mean_5d_xc_jerk_v081_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_mean_21d_xmc_jerk_v082_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_std_5d_xc_jerk_v083_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_std_21d_xmc_jerk_v084_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_ema_5d_xc_jerk_v085_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_ema_21d_xmc_jerk_v086_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_z_5d_xc_jerk_v087_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_z_21d_xmc_jerk_v088_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_log_5d_xc_jerk_v089_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_42d_log_21d_xmc_jerk_v090_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_mean_5d_xc_jerk_v091_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_mean_21d_xmc_jerk_v092_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_std_5d_xc_jerk_v093_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_std_21d_xmc_jerk_v094_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_ema_5d_xc_jerk_v095_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_ema_21d_xmc_jerk_v096_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_z_5d_xc_jerk_v097_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_z_21d_xmc_jerk_v098_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_log_5d_xc_jerk_v099_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_log_21d_xmc_jerk_v100_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_mean_5d_xc_jerk_v101_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_mean_21d_xmc_jerk_v102_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_std_5d_xc_jerk_v103_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_std_21d_xmc_jerk_v104_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_ema_5d_xc_jerk_v105_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_ema_21d_xmc_jerk_v106_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_z_5d_xc_jerk_v107_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_z_21d_xmc_jerk_v108_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_log_5d_xc_jerk_v109_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_5d_log_21d_xmc_jerk_v110_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_mean_5d_xc_jerk_v111_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_mean_21d_xmc_jerk_v112_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_std_5d_xc_jerk_v113_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_std_21d_xmc_jerk_v114_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_ema_5d_xc_jerk_v115_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_ema_21d_xmc_jerk_v116_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_z_5d_xc_jerk_v117_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_z_21d_xmc_jerk_v118_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_log_5d_xc_jerk_v119_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_10d_log_21d_xmc_jerk_v120_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_mean_5d_xc_jerk_v121_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_mean_21d_xmc_jerk_v122_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_std_5d_xc_jerk_v123_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_std_21d_xmc_jerk_v124_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_ema_5d_xc_jerk_v125_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_ema_21d_xmc_jerk_v126_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_z_5d_xc_jerk_v127_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_z_21d_xmc_jerk_v128_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_log_5d_xc_jerk_v129_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_log_21d_xmc_jerk_v130_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_mean_5d_xc_jerk_v131_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_mean_21d_xmc_jerk_v132_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_std_5d_xc_jerk_v133_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_std_21d_xmc_jerk_v134_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_ema_5d_xc_jerk_v135_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_ema_21d_xmc_jerk_v136_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_z_5d_xc_jerk_v137_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_z_21d_xmc_jerk_v138_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_log_5d_xc_jerk_v139_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_42d_log_21d_xmc_jerk_v140_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_mean_5d_xc_jerk_v141_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_mean_21d_xmc_jerk_v142_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_std_5d_xc_jerk_v143_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_std_21d_xmc_jerk_v144_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_ema_5d_xc_jerk_v145_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_ema_21d_xmc_jerk_v146_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_z_5d_xc_jerk_v147_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_z_21d_xmc_jerk_v148_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_log_5d_xc_jerk_v149_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_log_21d_xmc_jerk_v150_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_mean_5d_xc_jerk_v001_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_mean_21d_xmc_jerk_v002_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_std_5d_xc_jerk_v003_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_std_21d_xmc_jerk_v004_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_ema_5d_xc_jerk_v005_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_ema_21d_xmc_jerk_v006_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_z_5d_xc_jerk_v007_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_z_21d_xmc_jerk_v008_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_log_5d_xc_jerk_v009_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_5d_log_21d_xmc_jerk_v010_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_mean_5d_xc_jerk_v011_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_mean_21d_xmc_jerk_v012_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_std_5d_xc_jerk_v013_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_std_21d_xmc_jerk_v014_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_ema_5d_xc_jerk_v015_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_ema_21d_xmc_jerk_v016_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_z_5d_xc_jerk_v017_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_z_21d_xmc_jerk_v018_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_log_5d_xc_jerk_v019_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_10d_log_21d_xmc_jerk_v020_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_mean_5d_xc_jerk_v021_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_mean_21d_xmc_jerk_v022_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_std_5d_xc_jerk_v023_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_std_21d_xmc_jerk_v024_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_ema_5d_xc_jerk_v025_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_ema_21d_xmc_jerk_v026_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_z_5d_xc_jerk_v027_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_z_21d_xmc_jerk_v028_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_log_5d_xc_jerk_v029_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_21d_log_21d_xmc_jerk_v030_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_mean_5d_xc_jerk_v031_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_mean_21d_xmc_jerk_v032_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_std_5d_xc_jerk_v033_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_std_21d_xmc_jerk_v034_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_ema_5d_xc_jerk_v035_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_ema_21d_xmc_jerk_v036_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_z_5d_xc_jerk_v037_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_z_21d_xmc_jerk_v038_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_log_5d_xc_jerk_v039_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_42d_log_21d_xmc_jerk_v040_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_mean_5d_xc_jerk_v041_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_mean_21d_xmc_jerk_v042_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_std_5d_xc_jerk_v043_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_std_21d_xmc_jerk_v044_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_ema_5d_xc_jerk_v045_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_ema_21d_xmc_jerk_v046_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_z_5d_xc_jerk_v047_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_z_21d_xmc_jerk_v048_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_log_5d_xc_jerk_v049_signal,
    f31hra_f31_healthcare_revenue_acceleration_rgaccel_63d_log_21d_xmc_jerk_v050_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_mean_5d_xc_jerk_v051_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_mean_21d_xmc_jerk_v052_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_std_5d_xc_jerk_v053_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_std_21d_xmc_jerk_v054_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_ema_5d_xc_jerk_v055_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_ema_21d_xmc_jerk_v056_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_z_5d_xc_jerk_v057_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_z_21d_xmc_jerk_v058_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_log_5d_xc_jerk_v059_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_5d_log_21d_xmc_jerk_v060_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_mean_5d_xc_jerk_v061_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_mean_21d_xmc_jerk_v062_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_std_5d_xc_jerk_v063_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_std_21d_xmc_jerk_v064_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_ema_5d_xc_jerk_v065_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_ema_21d_xmc_jerk_v066_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_z_5d_xc_jerk_v067_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_z_21d_xmc_jerk_v068_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_log_5d_xc_jerk_v069_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_10d_log_21d_xmc_jerk_v070_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_mean_5d_xc_jerk_v071_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_mean_21d_xmc_jerk_v072_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_std_5d_xc_jerk_v073_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_std_21d_xmc_jerk_v074_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_ema_5d_xc_jerk_v075_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_ema_21d_xmc_jerk_v076_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_z_5d_xc_jerk_v077_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_z_21d_xmc_jerk_v078_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_log_5d_xc_jerk_v079_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_log_21d_xmc_jerk_v080_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_mean_5d_xc_jerk_v081_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_mean_21d_xmc_jerk_v082_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_std_5d_xc_jerk_v083_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_std_21d_xmc_jerk_v084_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_ema_5d_xc_jerk_v085_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_ema_21d_xmc_jerk_v086_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_z_5d_xc_jerk_v087_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_z_21d_xmc_jerk_v088_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_log_5d_xc_jerk_v089_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_42d_log_21d_xmc_jerk_v090_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_mean_5d_xc_jerk_v091_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_mean_21d_xmc_jerk_v092_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_std_5d_xc_jerk_v093_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_std_21d_xmc_jerk_v094_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_ema_5d_xc_jerk_v095_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_ema_21d_xmc_jerk_v096_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_z_5d_xc_jerk_v097_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_z_21d_xmc_jerk_v098_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_log_5d_xc_jerk_v099_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_log_21d_xmc_jerk_v100_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_mean_5d_xc_jerk_v101_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_mean_21d_xmc_jerk_v102_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_std_5d_xc_jerk_v103_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_std_21d_xmc_jerk_v104_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_ema_5d_xc_jerk_v105_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_ema_21d_xmc_jerk_v106_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_z_5d_xc_jerk_v107_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_z_21d_xmc_jerk_v108_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_log_5d_xc_jerk_v109_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_5d_log_21d_xmc_jerk_v110_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_mean_5d_xc_jerk_v111_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_mean_21d_xmc_jerk_v112_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_std_5d_xc_jerk_v113_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_std_21d_xmc_jerk_v114_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_ema_5d_xc_jerk_v115_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_ema_21d_xmc_jerk_v116_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_z_5d_xc_jerk_v117_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_z_21d_xmc_jerk_v118_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_log_5d_xc_jerk_v119_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_10d_log_21d_xmc_jerk_v120_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_mean_5d_xc_jerk_v121_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_mean_21d_xmc_jerk_v122_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_std_5d_xc_jerk_v123_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_std_21d_xmc_jerk_v124_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_ema_5d_xc_jerk_v125_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_ema_21d_xmc_jerk_v126_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_z_5d_xc_jerk_v127_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_z_21d_xmc_jerk_v128_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_log_5d_xc_jerk_v129_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_log_21d_xmc_jerk_v130_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_mean_5d_xc_jerk_v131_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_mean_21d_xmc_jerk_v132_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_std_5d_xc_jerk_v133_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_std_21d_xmc_jerk_v134_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_ema_5d_xc_jerk_v135_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_ema_21d_xmc_jerk_v136_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_z_5d_xc_jerk_v137_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_z_21d_xmc_jerk_v138_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_log_5d_xc_jerk_v139_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_42d_log_21d_xmc_jerk_v140_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_mean_5d_xc_jerk_v141_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_mean_21d_xmc_jerk_v142_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_std_5d_xc_jerk_v143_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_std_21d_xmc_jerk_v144_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_ema_5d_xc_jerk_v145_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_ema_21d_xmc_jerk_v146_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_z_5d_xc_jerk_v147_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_z_21d_xmc_jerk_v148_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_log_5d_xc_jerk_v149_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_log_21d_xmc_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HEALTHCARE_REVENUE_ACCELERATION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f31_revenue_growth_accel', '_f31_acceleration_persistence', '_f31_growth_quality')
    import hashlib
    body_hashes = set()
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
        body = "\n".join(l.strip() for l in src.splitlines()
                          if l.strip() and not l.strip().startswith("#")
                          and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in body_hashes, f"DUP body: {name}"
        body_hashes.add(h)
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f31_healthcare_revenue_acceleration_3rd_derivatives_001_150_claude: {n_features} features pass")
