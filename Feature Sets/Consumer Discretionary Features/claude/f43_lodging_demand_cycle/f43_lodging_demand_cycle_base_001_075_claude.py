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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f43_revenue_vol(revenue, w):
    g = revenue.pct_change()
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f43_revenue_drawdown(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - peak) / peak.replace(0, np.nan).abs()


def _f43_demand_cycle_score(revenue, ebitda, w):
    r = ebitda / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f43ldc_f43_lodging_demand_cycle_rvol_5d_base_v001_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_10d_base_v002_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_21d_base_v003_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_42d_base_v004_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_63d_base_v005_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_126d_base_v006_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_189d_base_v007_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_252d_base_v008_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_378d_base_v009_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvol_504d_base_v010_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_5d_base_v011_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 5)
    result = _ema(v, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_10d_base_v012_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 10)
    result = _ema(v, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_21d_base_v013_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 21)
    result = _ema(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_42d_base_v014_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 42)
    result = _ema(v, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_63d_base_v015_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _ema(v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_126d_base_v016_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 126)
    result = _ema(v, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_189d_base_v017_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 189)
    result = _ema(v, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_252d_base_v018_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    result = _ema(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_378d_base_v019_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 378)
    result = _ema(v, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolema_504d_base_v020_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    result = _ema(v, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_21d_base_v021_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_42d_base_v022_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_63d_base_v023_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_126d_base_v024_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_189d_base_v025_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_252d_base_v026_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_378d_base_v027_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolz_504d_base_v028_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _z(v, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_5d_base_v029_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_10d_base_v030_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_21d_base_v031_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_42d_base_v032_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_63d_base_v033_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_126d_base_v034_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_189d_base_v035_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_252d_base_v036_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_378d_base_v037_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdd_504d_base_v038_signal(revenue, closeadj):
    result = _f43_revenue_drawdown(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_base_v039_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_base_v040_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = _mean(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_base_v041_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    result = _mean(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_base_v042_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 126)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_5d_base_v043_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_10d_base_v044_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_21d_base_v045_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_42d_base_v046_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_63d_base_v047_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_126d_base_v048_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_189d_base_v049_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_252d_base_v050_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_378d_base_v051_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcs_504d_base_v052_signal(revenue, ebitda, closeadj):
    result = _f43_demand_cycle_score(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_5d_base_v053_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 5)
    result = _ema(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_10d_base_v054_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 10)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_21d_base_v055_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_42d_base_v056_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 42)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_63d_base_v057_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_126d_base_v058_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 126)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_189d_base_v059_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 189)
    result = _ema(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_252d_base_v060_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_378d_base_v061_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 378)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsema_504d_base_v062_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 504)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_21d_base_v063_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_42d_base_v064_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_63d_base_v065_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_126d_base_v066_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_189d_base_v067_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_252d_base_v068_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_378d_base_v069_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsz_504d_base_v070_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxvol_21d_base_v071_signal(revenue, volume):
    v = _f43_revenue_vol(revenue, 21)
    result = v * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxvol_63d_base_v072_signal(revenue, volume):
    v = _f43_revenue_vol(revenue, 63)
    result = v * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxvol_252d_base_v073_signal(revenue, volume):
    v = _f43_revenue_vol(revenue, 252)
    result = v * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxvol_21d_base_v074_signal(revenue, volume):
    d = _f43_revenue_drawdown(revenue, 21)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxvol_63d_base_v075_signal(revenue, volume):
    d = _f43_revenue_drawdown(revenue, 63)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43ldc_f43_lodging_demand_cycle_rvol_5d_base_v001_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_10d_base_v002_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_21d_base_v003_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_42d_base_v004_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_63d_base_v005_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_126d_base_v006_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_189d_base_v007_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_252d_base_v008_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_378d_base_v009_signal,
    f43ldc_f43_lodging_demand_cycle_rvol_504d_base_v010_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_5d_base_v011_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_10d_base_v012_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_21d_base_v013_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_42d_base_v014_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_63d_base_v015_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_126d_base_v016_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_189d_base_v017_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_252d_base_v018_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_378d_base_v019_signal,
    f43ldc_f43_lodging_demand_cycle_rvolema_504d_base_v020_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_21d_base_v021_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_42d_base_v022_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_63d_base_v023_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_126d_base_v024_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_189d_base_v025_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_252d_base_v026_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_378d_base_v027_signal,
    f43ldc_f43_lodging_demand_cycle_rvolz_504d_base_v028_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_5d_base_v029_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_10d_base_v030_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_21d_base_v031_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_42d_base_v032_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_63d_base_v033_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_126d_base_v034_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_189d_base_v035_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_252d_base_v036_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_378d_base_v037_signal,
    f43ldc_f43_lodging_demand_cycle_rdd_504d_base_v038_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_63o21_base_v039_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_252o63_base_v040_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_504o126_base_v041_signal,
    f43ldc_f43_lodging_demand_cycle_rddsmooth_126o21_base_v042_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_5d_base_v043_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_10d_base_v044_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_21d_base_v045_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_42d_base_v046_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_63d_base_v047_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_126d_base_v048_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_189d_base_v049_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_252d_base_v050_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_378d_base_v051_signal,
    f43ldc_f43_lodging_demand_cycle_dcs_504d_base_v052_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_5d_base_v053_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_10d_base_v054_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_21d_base_v055_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_42d_base_v056_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_63d_base_v057_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_126d_base_v058_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_189d_base_v059_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_252d_base_v060_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_378d_base_v061_signal,
    f43ldc_f43_lodging_demand_cycle_dcsema_504d_base_v062_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_21d_base_v063_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_42d_base_v064_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_63d_base_v065_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_126d_base_v066_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_189d_base_v067_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_252d_base_v068_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_378d_base_v069_signal,
    f43ldc_f43_lodging_demand_cycle_dcsz_504d_base_v070_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxvol_21d_base_v071_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxvol_63d_base_v072_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxvol_252d_base_v073_signal,
    f43ldc_f43_lodging_demand_cycle_rddxvol_21d_base_v074_signal,
    f43ldc_f43_lodging_demand_cycle_rddxvol_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_LODGING_DEMAND_CYCLE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK lodging_demand_cycle_base_001_075_claude: {n_features} features pass")
