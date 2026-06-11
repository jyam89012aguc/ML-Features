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

def f10rcd_f10_retail_comp_dynamics_dur_5d_jerk_v001_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    base = d * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_10d_jerk_v002_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    base = d * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_21d_jerk_v003_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    base = d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_42d_jerk_v004_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    base = d * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_63d_jerk_v005_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    base = d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_126d_jerk_v006_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    base = d * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_189d_jerk_v007_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    base = d * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_252d_jerk_v008_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    base = d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_378d_jerk_v009_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    base = d * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_504d_jerk_v010_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    base = d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_5d_jerk_v011_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_10d_jerk_v012_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_21d_jerk_v013_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_42d_jerk_v014_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_63d_jerk_v015_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_126d_jerk_v016_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_189d_jerk_v017_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_252d_jerk_v018_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_378d_jerk_v019_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_mean_504d_jerk_v020_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_5d_jerk_v021_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_10d_jerk_v022_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_21d_jerk_v023_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_42d_jerk_v024_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_63d_jerk_v025_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_126d_jerk_v026_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_189d_jerk_v027_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_252d_jerk_v028_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_378d_jerk_v029_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_std_504d_jerk_v030_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_5d_jerk_v031_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_10d_jerk_v032_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_21d_jerk_v033_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_42d_jerk_v034_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_63d_jerk_v035_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_126d_jerk_v036_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_189d_jerk_v037_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_252d_jerk_v038_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_378d_jerk_v039_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_z_504d_jerk_v040_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_5d_jerk_v041_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 5)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_10d_jerk_v042_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 10)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_21d_jerk_v043_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 21)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_42d_jerk_v044_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 42)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_63d_jerk_v045_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 63)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_126d_jerk_v046_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 126)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_189d_jerk_v047_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 189)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_252d_jerk_v048_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 252)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_378d_jerk_v049_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 378)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_dur_ema_504d_jerk_v050_signal(revenue, ppnenet, closeadj):
    d = _f10_comp_growth_durability(revenue, ppnenet, 504)
    base = _ema(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_5d_jerk_v051_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_10d_jerk_v052_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_21d_jerk_v053_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_42d_jerk_v054_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_63d_jerk_v055_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_84d_jerk_v056_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_105d_jerk_v057_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_126d_jerk_v058_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_168d_jerk_v059_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_189d_jerk_v060_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_5d_jerk_v061_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_10d_jerk_v062_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_21d_jerk_v063_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_42d_jerk_v064_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_63d_jerk_v065_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_84d_jerk_v066_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_105d_jerk_v067_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_126d_jerk_v068_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_168d_jerk_v069_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_mean_189d_jerk_v070_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_5d_jerk_v071_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_10d_jerk_v072_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_21d_jerk_v073_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_42d_jerk_v074_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_63d_jerk_v075_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_84d_jerk_v076_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_105d_jerk_v077_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_126d_jerk_v078_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_168d_jerk_v079_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_189d_jerk_v080_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_5d_jerk_v081_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_10d_jerk_v082_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_21d_jerk_v083_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_42d_jerk_v084_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_63d_jerk_v085_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_84d_jerk_v086_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_105d_jerk_v087_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_126d_jerk_v088_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_168d_jerk_v089_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_189d_jerk_v090_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_5d_jerk_v091_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    base = (f - f.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_10d_jerk_v092_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    base = (f - f.shift(10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_21d_jerk_v093_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    base = (f - f.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_42d_jerk_v094_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    base = (f - f.shift(42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_63d_jerk_v095_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    base = (f - f.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_84d_jerk_v096_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    base = (f - f.shift(84)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_105d_jerk_v097_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    base = (f - f.shift(105)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_126d_jerk_v098_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    base = (f - f.shift(126)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_168d_jerk_v099_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    base = (f - f.shift(168)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_189d_jerk_v100_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    base = (f - f.shift(189)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_5d_jerk_v101_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_10d_jerk_v102_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    base = s * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_21d_jerk_v103_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_42d_jerk_v104_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    base = s * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_63d_jerk_v105_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_126d_jerk_v106_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_189d_jerk_v107_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    base = s * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_252d_jerk_v108_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_378d_jerk_v109_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    base = s * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_504d_jerk_v110_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_5d_jerk_v111_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_10d_jerk_v112_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_21d_jerk_v113_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_42d_jerk_v114_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_63d_jerk_v115_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_126d_jerk_v116_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_189d_jerk_v117_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_252d_jerk_v118_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_378d_jerk_v119_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_504d_jerk_v120_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    base = _mean(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_5d_jerk_v121_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_10d_jerk_v122_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_21d_jerk_v123_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_42d_jerk_v124_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_63d_jerk_v125_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_126d_jerk_v126_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_189d_jerk_v127_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_252d_jerk_v128_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_378d_jerk_v129_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_504d_jerk_v130_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    base = _std(s, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_5d_jerk_v131_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_10d_jerk_v132_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_21d_jerk_v133_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_42d_jerk_v134_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_63d_jerk_v135_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_126d_jerk_v136_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_189d_jerk_v137_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_252d_jerk_v138_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_378d_jerk_v139_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_504d_jerk_v140_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    base = _z(s, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_5d_jerk_v141_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 5)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_10d_jerk_v142_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 10)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_21d_jerk_v143_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 21)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_42d_jerk_v144_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 42)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_63d_jerk_v145_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 63)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_126d_jerk_v146_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 126)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_189d_jerk_v147_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 189)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_252d_jerk_v148_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 252)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_378d_jerk_v149_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 378)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_504d_jerk_v150_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 504)
    base = s * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f10rcd_f10_retail_comp_dynamics_dur_5d_jerk_v001_signal,
    f10rcd_f10_retail_comp_dynamics_dur_10d_jerk_v002_signal,
    f10rcd_f10_retail_comp_dynamics_dur_21d_jerk_v003_signal,
    f10rcd_f10_retail_comp_dynamics_dur_42d_jerk_v004_signal,
    f10rcd_f10_retail_comp_dynamics_dur_63d_jerk_v005_signal,
    f10rcd_f10_retail_comp_dynamics_dur_126d_jerk_v006_signal,
    f10rcd_f10_retail_comp_dynamics_dur_189d_jerk_v007_signal,
    f10rcd_f10_retail_comp_dynamics_dur_252d_jerk_v008_signal,
    f10rcd_f10_retail_comp_dynamics_dur_378d_jerk_v009_signal,
    f10rcd_f10_retail_comp_dynamics_dur_504d_jerk_v010_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_5d_jerk_v011_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_10d_jerk_v012_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_21d_jerk_v013_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_42d_jerk_v014_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_63d_jerk_v015_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_126d_jerk_v016_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_189d_jerk_v017_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_252d_jerk_v018_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_378d_jerk_v019_signal,
    f10rcd_f10_retail_comp_dynamics_dur_mean_504d_jerk_v020_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_5d_jerk_v021_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_10d_jerk_v022_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_21d_jerk_v023_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_42d_jerk_v024_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_63d_jerk_v025_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_126d_jerk_v026_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_189d_jerk_v027_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_252d_jerk_v028_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_378d_jerk_v029_signal,
    f10rcd_f10_retail_comp_dynamics_dur_std_504d_jerk_v030_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_5d_jerk_v031_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_10d_jerk_v032_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_21d_jerk_v033_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_42d_jerk_v034_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_63d_jerk_v035_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_126d_jerk_v036_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_189d_jerk_v037_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_252d_jerk_v038_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_378d_jerk_v039_signal,
    f10rcd_f10_retail_comp_dynamics_dur_z_504d_jerk_v040_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_5d_jerk_v041_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_10d_jerk_v042_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_21d_jerk_v043_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_42d_jerk_v044_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_63d_jerk_v045_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_126d_jerk_v046_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_189d_jerk_v047_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_252d_jerk_v048_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_378d_jerk_v049_signal,
    f10rcd_f10_retail_comp_dynamics_dur_ema_504d_jerk_v050_signal,
    f10rcd_f10_retail_comp_dynamics_floor_5d_jerk_v051_signal,
    f10rcd_f10_retail_comp_dynamics_floor_10d_jerk_v052_signal,
    f10rcd_f10_retail_comp_dynamics_floor_21d_jerk_v053_signal,
    f10rcd_f10_retail_comp_dynamics_floor_42d_jerk_v054_signal,
    f10rcd_f10_retail_comp_dynamics_floor_63d_jerk_v055_signal,
    f10rcd_f10_retail_comp_dynamics_floor_84d_jerk_v056_signal,
    f10rcd_f10_retail_comp_dynamics_floor_105d_jerk_v057_signal,
    f10rcd_f10_retail_comp_dynamics_floor_126d_jerk_v058_signal,
    f10rcd_f10_retail_comp_dynamics_floor_168d_jerk_v059_signal,
    f10rcd_f10_retail_comp_dynamics_floor_189d_jerk_v060_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_5d_jerk_v061_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_10d_jerk_v062_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_21d_jerk_v063_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_42d_jerk_v064_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_63d_jerk_v065_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_84d_jerk_v066_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_105d_jerk_v067_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_126d_jerk_v068_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_168d_jerk_v069_signal,
    f10rcd_f10_retail_comp_dynamics_floor_mean_189d_jerk_v070_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_5d_jerk_v071_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_10d_jerk_v072_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_21d_jerk_v073_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_42d_jerk_v074_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_63d_jerk_v075_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_84d_jerk_v076_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_105d_jerk_v077_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_126d_jerk_v078_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_168d_jerk_v079_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_189d_jerk_v080_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_5d_jerk_v081_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_10d_jerk_v082_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_21d_jerk_v083_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_42d_jerk_v084_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_63d_jerk_v085_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_84d_jerk_v086_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_105d_jerk_v087_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_126d_jerk_v088_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_168d_jerk_v089_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_189d_jerk_v090_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_5d_jerk_v091_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_10d_jerk_v092_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_21d_jerk_v093_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_42d_jerk_v094_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_63d_jerk_v095_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_84d_jerk_v096_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_105d_jerk_v097_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_126d_jerk_v098_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_168d_jerk_v099_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_189d_jerk_v100_signal,
    f10rcd_f10_retail_comp_dynamics_stab_5d_jerk_v101_signal,
    f10rcd_f10_retail_comp_dynamics_stab_10d_jerk_v102_signal,
    f10rcd_f10_retail_comp_dynamics_stab_21d_jerk_v103_signal,
    f10rcd_f10_retail_comp_dynamics_stab_42d_jerk_v104_signal,
    f10rcd_f10_retail_comp_dynamics_stab_63d_jerk_v105_signal,
    f10rcd_f10_retail_comp_dynamics_stab_126d_jerk_v106_signal,
    f10rcd_f10_retail_comp_dynamics_stab_189d_jerk_v107_signal,
    f10rcd_f10_retail_comp_dynamics_stab_252d_jerk_v108_signal,
    f10rcd_f10_retail_comp_dynamics_stab_378d_jerk_v109_signal,
    f10rcd_f10_retail_comp_dynamics_stab_504d_jerk_v110_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_5d_jerk_v111_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_10d_jerk_v112_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_21d_jerk_v113_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_42d_jerk_v114_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_63d_jerk_v115_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_126d_jerk_v116_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_189d_jerk_v117_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_252d_jerk_v118_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_378d_jerk_v119_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_504d_jerk_v120_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_5d_jerk_v121_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_10d_jerk_v122_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_21d_jerk_v123_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_42d_jerk_v124_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_63d_jerk_v125_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_126d_jerk_v126_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_189d_jerk_v127_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_252d_jerk_v128_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_378d_jerk_v129_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_504d_jerk_v130_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_5d_jerk_v131_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_10d_jerk_v132_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_21d_jerk_v133_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_42d_jerk_v134_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_63d_jerk_v135_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_126d_jerk_v136_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_189d_jerk_v137_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_252d_jerk_v138_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_378d_jerk_v139_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_504d_jerk_v140_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_5d_jerk_v141_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_10d_jerk_v142_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_21d_jerk_v143_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_42d_jerk_v144_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_63d_jerk_v145_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_126d_jerk_v146_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_189d_jerk_v147_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_252d_jerk_v148_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_378d_jerk_v149_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RETAIL_COMP_DYNAMICS_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f10_retail_comp_dynamics_jerk_001_150_claude: {n_features} features pass")
