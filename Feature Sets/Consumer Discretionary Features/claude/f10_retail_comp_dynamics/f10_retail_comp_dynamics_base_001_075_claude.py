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


# ===== folder domain primitives =====
def _f10_comp_growth_durability(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g = rpp.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f10_comp_floor(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g = rpp.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).min()


def _f10_comp_stability(revenue, w):
    g = revenue.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)

def f10rcd_f10_retail_comp_dynamics_dur_5d_base_v001_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_10d_base_v002_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_21d_base_v003_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_42d_base_v004_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_63d_base_v005_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_126d_base_v006_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_189d_base_v007_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_252d_base_v008_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_378d_base_v009_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_504d_base_v010_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_5d_base_v011_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_10d_base_v012_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_21d_base_v013_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_42d_base_v014_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_63d_base_v015_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_126d_base_v016_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_189d_base_v017_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_252d_base_v018_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_378d_base_v019_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_504d_base_v020_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_5d_base_v021_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_10d_base_v022_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_21d_base_v023_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_42d_base_v024_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_63d_base_v025_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_126d_base_v026_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_189d_base_v027_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_252d_base_v028_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_378d_base_v029_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_504d_base_v030_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_5d_base_v031_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_10d_base_v032_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_21d_base_v033_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_42d_base_v034_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_63d_base_v035_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_126d_base_v036_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_189d_base_v037_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_252d_base_v038_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_378d_base_v039_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_504d_base_v040_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_5d_base_v041_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_10d_base_v042_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_21d_base_v043_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_42d_base_v044_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_63d_base_v045_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_126d_base_v046_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_189d_base_v047_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_252d_base_v048_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_378d_base_v049_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_504d_base_v050_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_5d_base_v051_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_10d_base_v052_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_21d_base_v053_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_42d_base_v054_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_63d_base_v055_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_84d_base_v056_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_105d_base_v057_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_126d_base_v058_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_168d_base_v059_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_189d_base_v060_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_5d_base_v061_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_10d_base_v062_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_21d_base_v063_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_42d_base_v064_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_63d_base_v065_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_84d_base_v066_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_105d_base_v067_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_126d_base_v068_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_168d_base_v069_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_189d_base_v070_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_5d_base_v071_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_10d_base_v072_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_21d_base_v073_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_42d_base_v074_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_63d_base_v075_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f10rcd_f10_retail_comp_dynamics_dur_5d_base_v001_signal,
    f10rcd_f10_retail_comp_dynamics_dur_10d_base_v002_signal,
    f10rcd_f10_retail_comp_dynamics_dur_21d_base_v003_signal,
    f10rcd_f10_retail_comp_dynamics_dur_42d_base_v004_signal,
    f10rcd_f10_retail_comp_dynamics_dur_63d_base_v005_signal,
    f10rcd_f10_retail_comp_dynamics_dur_126d_base_v006_signal,
    f10rcd_f10_retail_comp_dynamics_dur_189d_base_v007_signal,
    f10rcd_f10_retail_comp_dynamics_dur_252d_base_v008_signal,
    f10rcd_f10_retail_comp_dynamics_dur_378d_base_v009_signal,
    f10rcd_f10_retail_comp_dynamics_dur_504d_base_v010_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_5d_base_v011_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_10d_base_v012_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_21d_base_v013_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_42d_base_v014_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_63d_base_v015_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_126d_base_v016_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_189d_base_v017_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_252d_base_v018_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_378d_base_v019_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_504d_base_v020_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_5d_base_v021_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_10d_base_v022_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_21d_base_v023_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_42d_base_v024_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_63d_base_v025_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_126d_base_v026_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_189d_base_v027_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_252d_base_v028_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_378d_base_v029_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_504d_base_v030_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_5d_base_v031_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_10d_base_v032_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_21d_base_v033_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_42d_base_v034_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_63d_base_v035_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_126d_base_v036_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_189d_base_v037_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_252d_base_v038_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_378d_base_v039_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_504d_base_v040_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_5d_base_v041_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_10d_base_v042_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_21d_base_v043_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_42d_base_v044_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_63d_base_v045_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_126d_base_v046_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_189d_base_v047_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_252d_base_v048_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_378d_base_v049_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_504d_base_v050_signal,
    f10rcd_f10_retail_comp_dynamics_floor_5d_base_v051_signal,
    f10rcd_f10_retail_comp_dynamics_floor_10d_base_v052_signal,
    f10rcd_f10_retail_comp_dynamics_floor_21d_base_v053_signal,
    f10rcd_f10_retail_comp_dynamics_floor_42d_base_v054_signal,
    f10rcd_f10_retail_comp_dynamics_floor_63d_base_v055_signal,
    f10rcd_f10_retail_comp_dynamics_floor_84d_base_v056_signal,
    f10rcd_f10_retail_comp_dynamics_floor_105d_base_v057_signal,
    f10rcd_f10_retail_comp_dynamics_floor_126d_base_v058_signal,
    f10rcd_f10_retail_comp_dynamics_floor_168d_base_v059_signal,
    f10rcd_f10_retail_comp_dynamics_floor_189d_base_v060_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_5d_base_v061_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_10d_base_v062_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_21d_base_v063_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_42d_base_v064_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_63d_base_v065_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_84d_base_v066_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_105d_base_v067_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_126d_base_v068_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_168d_base_v069_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_189d_base_v070_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_5d_base_v071_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_10d_base_v072_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_21d_base_v073_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_42d_base_v074_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RETAIL_COMP_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_comp_growth_durability", "_f10_comp_floor", "_f10_comp_stability")
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
    print(f"OK f10_retail_comp_dynamics_001_075_claude: {n_features} features pass")
