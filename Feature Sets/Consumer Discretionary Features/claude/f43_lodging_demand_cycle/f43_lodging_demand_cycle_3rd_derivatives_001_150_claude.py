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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f43_revenue_vol(revenue, w):
    g = revenue.pct_change()
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f43_revenue_drawdown(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - peak) / peak.replace(0, np.nan).abs()


def _f43_demand_cycle_score(revenue, ebitda, w):
    r = ebitda / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v001_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v002_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v003_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v004_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v005_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v006_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v007_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v008_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v009_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v010_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v011_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v012_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v013_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v014_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v015_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v016_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v017_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v018_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v019_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v020_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v021_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v022_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v023_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v024_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v025_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v026_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v027_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v028_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v029_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v030_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v031_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = _ema(v, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v032_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = _ema(v, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v033_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    base = _ema(v, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v034_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = _ema(v, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v035_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = _ema(v, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v036_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    base = _ema(v, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v037_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = _ema(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v038_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = _ema(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v039_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    base = _ema(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v040_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = _ema(v, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v041_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = _ema(v, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v042_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    base = _ema(v, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v043_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _ema(v, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v044_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _ema(v, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v045_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _ema(v, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v046_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = _ema(v, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v047_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = _ema(v, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v048_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    base = _ema(v, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v049_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = _ema(v, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v050_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = _ema(v, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v051_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    base = _ema(v, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v052_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = _ema(v, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v053_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = _ema(v, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v054_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    base = _ema(v, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v055_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = _ema(v, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v056_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = _ema(v, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v057_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    base = _ema(v, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v058_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = _ema(v, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v059_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = _ema(v, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v060_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    base = _ema(v, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v061_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v062_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v063_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v064_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v065_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v066_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v067_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v068_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v069_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v070_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v071_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v072_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v073_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v074_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v075_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v076_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v077_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v078_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v079_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v080_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v081_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v082_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v083_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v084_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    base = _z(v, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v085_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v086_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v087_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v088_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v089_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v090_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v091_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v092_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v093_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v094_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v095_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v096_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v097_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v098_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v099_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v100_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v101_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v102_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v103_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v104_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v105_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v106_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v107_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v108_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v109_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v110_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v111_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v112_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v113_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v114_signal(revenue, closeadj):
    base = _f43_revenue_drawdown(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v115_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v116_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v117_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v118_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    base = _mean(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v119_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    base = _mean(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v120_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    base = _mean(d, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v121_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    base = _mean(d, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v122_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    base = _mean(d, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v123_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    base = _mean(d, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v124_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 126)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v125_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 126)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v126_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 126)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v127_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v128_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v129_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v130_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v131_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v132_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v133_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v134_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v135_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v136_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v137_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v138_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v139_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v140_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v141_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v142_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v143_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v144_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v145_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v146_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v147_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v148_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v149_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v150_signal(revenue, ebitda, closeadj):
    base = _f43_demand_cycle_score(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v001_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v002_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_5d_jerk_v003_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v004_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v005_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_10d_jerk_v006_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v007_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v008_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_21d_jerk_v009_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v010_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v011_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_42d_jerk_v012_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v013_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v014_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_63d_jerk_v015_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v016_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v017_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_126d_jerk_v018_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v019_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v020_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_189d_jerk_v021_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v022_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v023_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_252d_jerk_v024_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v025_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v026_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_378d_jerk_v027_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v028_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v029_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_504d_jerk_v030_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v031_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v032_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_5d_jerk_v033_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v034_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v035_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_10d_jerk_v036_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v037_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v038_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_21d_jerk_v039_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v040_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v041_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_42d_jerk_v042_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v043_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v044_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_63d_jerk_v045_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v046_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v047_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_126d_jerk_v048_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v049_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v050_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_189d_jerk_v051_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v052_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v053_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_252d_jerk_v054_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v055_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v056_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_378d_jerk_v057_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v058_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v059_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_504d_jerk_v060_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v061_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v062_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_21d_jerk_v063_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v064_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v065_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_42d_jerk_v066_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v067_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v068_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_63d_jerk_v069_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v070_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v071_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_126d_jerk_v072_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v073_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v074_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_189d_jerk_v075_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v076_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v077_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_252d_jerk_v078_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v079_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v080_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_378d_jerk_v081_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v082_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v083_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_504d_jerk_v084_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v085_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v086_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_5d_jerk_v087_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v088_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v089_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_10d_jerk_v090_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v091_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v092_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_21d_jerk_v093_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v094_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v095_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_42d_jerk_v096_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v097_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v098_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_63d_jerk_v099_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v100_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v101_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_126d_jerk_v102_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v103_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v104_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_189d_jerk_v105_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v106_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v107_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_252d_jerk_v108_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v109_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v110_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_378d_jerk_v111_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v112_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v113_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_504d_jerk_v114_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v115_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v116_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_jerk_v117_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v118_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v119_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_jerk_v120_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v121_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v122_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_jerk_v123_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v124_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v125_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_jerk_v126_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v127_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v128_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_5d_jerk_v129_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v130_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v131_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_10d_jerk_v132_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v133_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v134_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_21d_jerk_v135_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v136_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v137_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_42d_jerk_v138_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v139_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v140_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_63d_jerk_v141_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v142_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v143_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_126d_jerk_v144_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v145_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v146_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_189d_jerk_v147_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v148_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v149_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_LODGING_DEMAND_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ebitda": ebitda }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f43_revenue_vol", "_f43_revenue_drawdown", "_f43_demand_cycle_score")
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
    print(f"OK lodging_demand_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
