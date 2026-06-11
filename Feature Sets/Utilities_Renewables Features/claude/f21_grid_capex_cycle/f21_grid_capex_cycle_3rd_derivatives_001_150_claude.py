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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


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
def _f21_capex_intensity(capex, assets):
    return capex.rolling(63, min_periods=5).mean() / assets.replace(0, np.nan)


def _f21_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f21_capex_cycle(capex, revenue, w):
    ratio = capex / revenue.replace(0, np.nan)
    return ratio - ratio.rolling(w, min_periods=max(1, w // 2)).mean()



# ===== features =====

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_raw_jerk_v001_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_raw_jerk_v002_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_raw_jerk_v003_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_raw_jerk_v004_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_raw_jerk_v005_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_raw_jerk_v006_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_raw_jerk_v007_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_raw_jerk_v008_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_raw_jerk_v009_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_raw_jerk_v010_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_raw_jerk_v011_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_raw_jerk_v012_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_raw_jerk_v013_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_raw_jerk_v014_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_raw_jerk_v015_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_raw_jerk_v016_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_raw_jerk_v017_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_raw_jerk_v018_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_raw_jerk_v019_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_raw_jerk_v020_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_mean_jerk_v021_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_mean_jerk_v022_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_mean_jerk_v023_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_mean_jerk_v024_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_mean_jerk_v025_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_mean_jerk_v026_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_mean_jerk_v027_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_mean_jerk_v028_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_mean_jerk_v029_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_mean_jerk_v030_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_mean_jerk_v031_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_mean_jerk_v032_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_mean_jerk_v033_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * _mean(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_mean_jerk_v034_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * _mean(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_mean_jerk_v035_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * _mean(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_mean_jerk_v036_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * _mean(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_mean_jerk_v037_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_mean_jerk_v038_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * _mean(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_mean_jerk_v039_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * _mean(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_mean_jerk_v040_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * _mean(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_ema_jerk_v041_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * _ema(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_ema_jerk_v042_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * _ema(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_ema_jerk_v043_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_ema_jerk_v044_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * _ema(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_ema_jerk_v045_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_ema_jerk_v046_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_ema_jerk_v047_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * _ema(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_ema_jerk_v048_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * _ema(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_ema_jerk_v049_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * _ema(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_ema_jerk_v050_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * _ema(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_ema_jerk_v051_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * _ema(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_ema_jerk_v052_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * _ema(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_ema_jerk_v053_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * _ema(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_ema_jerk_v054_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * _ema(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_ema_jerk_v055_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * _ema(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_ema_jerk_v056_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * _ema(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_ema_jerk_v057_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * _ema(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_ema_jerk_v058_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * _ema(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_ema_jerk_v059_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * _ema(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_ema_jerk_v060_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * _ema(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_std_jerk_v061_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * _std(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_std_jerk_v062_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * _std(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_std_jerk_v063_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_std_jerk_v064_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * _std(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_std_jerk_v065_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_std_jerk_v066_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_std_jerk_v067_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * _std(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_std_jerk_v068_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_std_jerk_v069_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * _std(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_std_jerk_v070_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * _std(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_std_jerk_v071_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * _std(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_std_jerk_v072_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * _std(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_std_jerk_v073_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * _std(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_std_jerk_v074_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * _std(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_std_jerk_v075_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * _std(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_std_jerk_v076_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * _std(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_std_jerk_v077_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * _std(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_std_jerk_v078_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * _std(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_std_jerk_v079_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * _std(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_std_jerk_v080_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * _std(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_z_jerk_v081_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * _z(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_z_jerk_v082_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * _z(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_z_jerk_v083_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_z_jerk_v084_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * _z(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_z_jerk_v085_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_z_jerk_v086_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * _z(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_z_jerk_v087_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * _z(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_z_jerk_v088_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_z_jerk_v089_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * _z(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_z_jerk_v090_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * _z(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_z_jerk_v091_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * _z(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_z_jerk_v092_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * _z(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_z_jerk_v093_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * _z(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_z_jerk_v094_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * _z(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_z_jerk_v095_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * _z(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_z_jerk_v096_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * _z(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_z_jerk_v097_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * _z(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_z_jerk_v098_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * _z(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_z_jerk_v099_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * _z(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_z_jerk_v100_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * _z(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_abs_jerk_v101_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_abs_jerk_v102_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_abs_jerk_v103_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_abs_jerk_v104_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_abs_jerk_v105_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_abs_jerk_v106_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_abs_jerk_v107_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_abs_jerk_v108_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_abs_jerk_v109_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_abs_jerk_v110_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_abs_jerk_v111_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_abs_jerk_v112_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_abs_jerk_v113_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_abs_jerk_v114_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_abs_jerk_v115_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_abs_jerk_v116_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_abs_jerk_v117_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_abs_jerk_v118_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_abs_jerk_v119_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_abs_jerk_v120_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_sq_jerk_v121_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 5) * _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_sq_jerk_v122_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 10) * _jerk(base, 10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_sq_jerk_v123_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 21) * _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_sq_jerk_v124_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 42) * _jerk(base, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_sq_jerk_v125_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 63) * _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_sq_jerk_v126_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 126) * _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_sq_jerk_v127_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 189) * _jerk(base, 189).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_sq_jerk_v128_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 252) * _jerk(base, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_sq_jerk_v129_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 378) * _jerk(base, 378).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_sq_jerk_v130_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 504) * _jerk(base, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_sq_jerk_v131_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 7) * _jerk(base, 7).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_sq_jerk_v132_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 14) * _jerk(base, 14).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_sq_jerk_v133_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 30) * _jerk(base, 30).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_sq_jerk_v134_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 45) * _jerk(base, 45).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_sq_jerk_v135_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 90) * _jerk(base, 90).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_sq_jerk_v136_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 105) * _jerk(base, 105).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_sq_jerk_v137_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 168) * _jerk(base, 168).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_sq_jerk_v138_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 210) * _jerk(base, 210).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_sq_jerk_v139_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 315) * _jerk(base, 315).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_sq_jerk_v140_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = _jerk(base, 420) * _jerk(base, 420).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_sign_jerk_v141_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 5)) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_sign_jerk_v142_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 10)) * closeadj * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_sign_jerk_v143_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 21)) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_sign_jerk_v144_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 42)) * closeadj * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_sign_jerk_v145_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 63)) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_sign_jerk_v146_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 126)) * closeadj * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_sign_jerk_v147_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 189)) * closeadj * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_sign_jerk_v148_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 252)) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_sign_jerk_v149_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 378)) * closeadj * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_sign_jerk_v150_signal(capex, assets, closeadj):
    base = _f21_capex_intensity(capex, assets)
    result = np.sign(_jerk(base, 504)) * closeadj * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_raw_jerk_v001_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_raw_jerk_v002_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_raw_jerk_v003_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_raw_jerk_v004_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_raw_jerk_v005_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_raw_jerk_v006_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_raw_jerk_v007_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_raw_jerk_v008_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_raw_jerk_v009_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_raw_jerk_v010_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_raw_jerk_v011_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_raw_jerk_v012_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_raw_jerk_v013_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_raw_jerk_v014_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_raw_jerk_v015_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_raw_jerk_v016_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_raw_jerk_v017_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_raw_jerk_v018_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_raw_jerk_v019_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_raw_jerk_v020_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_mean_jerk_v021_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_mean_jerk_v022_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_mean_jerk_v023_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_mean_jerk_v024_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_mean_jerk_v025_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_mean_jerk_v026_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_mean_jerk_v027_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_mean_jerk_v028_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_mean_jerk_v029_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_mean_jerk_v030_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_mean_jerk_v031_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_mean_jerk_v032_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_mean_jerk_v033_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_mean_jerk_v034_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_mean_jerk_v035_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_mean_jerk_v036_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_mean_jerk_v037_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_mean_jerk_v038_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_mean_jerk_v039_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_mean_jerk_v040_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_ema_jerk_v041_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_ema_jerk_v042_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_ema_jerk_v043_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_ema_jerk_v044_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_ema_jerk_v045_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_ema_jerk_v046_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_ema_jerk_v047_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_ema_jerk_v048_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_ema_jerk_v049_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_ema_jerk_v050_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_ema_jerk_v051_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_ema_jerk_v052_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_ema_jerk_v053_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_ema_jerk_v054_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_ema_jerk_v055_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_ema_jerk_v056_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_ema_jerk_v057_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_ema_jerk_v058_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_ema_jerk_v059_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_ema_jerk_v060_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_std_jerk_v061_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_std_jerk_v062_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_std_jerk_v063_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_std_jerk_v064_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_std_jerk_v065_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_std_jerk_v066_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_std_jerk_v067_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_std_jerk_v068_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_std_jerk_v069_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_std_jerk_v070_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_std_jerk_v071_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_std_jerk_v072_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_std_jerk_v073_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_std_jerk_v074_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_std_jerk_v075_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_std_jerk_v076_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_std_jerk_v077_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_std_jerk_v078_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_std_jerk_v079_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_std_jerk_v080_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_z_jerk_v081_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_z_jerk_v082_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_z_jerk_v083_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_z_jerk_v084_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_z_jerk_v085_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_z_jerk_v086_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_z_jerk_v087_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_z_jerk_v088_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_z_jerk_v089_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_z_jerk_v090_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_z_jerk_v091_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_z_jerk_v092_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_z_jerk_v093_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_z_jerk_v094_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_z_jerk_v095_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_z_jerk_v096_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_z_jerk_v097_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_z_jerk_v098_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_z_jerk_v099_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_z_jerk_v100_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_abs_jerk_v101_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_abs_jerk_v102_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_abs_jerk_v103_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_abs_jerk_v104_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_abs_jerk_v105_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_abs_jerk_v106_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_abs_jerk_v107_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_abs_jerk_v108_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_abs_jerk_v109_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_abs_jerk_v110_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_abs_jerk_v111_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_abs_jerk_v112_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_abs_jerk_v113_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_abs_jerk_v114_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_abs_jerk_v115_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_abs_jerk_v116_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_abs_jerk_v117_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_abs_jerk_v118_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_abs_jerk_v119_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_abs_jerk_v120_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_sq_jerk_v121_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_sq_jerk_v122_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_sq_jerk_v123_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_sq_jerk_v124_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_sq_jerk_v125_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_sq_jerk_v126_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_sq_jerk_v127_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_sq_jerk_v128_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_sq_jerk_v129_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_sq_jerk_v130_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p7s_jerk_sq_jerk_v131_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p14s_jerk_sq_jerk_v132_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p30s_jerk_sq_jerk_v133_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p45s_jerk_sq_jerk_v134_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p90s_jerk_sq_jerk_v135_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p105s_jerk_sq_jerk_v136_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p168s_jerk_sq_jerk_v137_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p210s_jerk_sq_jerk_v138_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p315s_jerk_sq_jerk_v139_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p420s_jerk_sq_jerk_v140_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p5s_jerk_sign_jerk_v141_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p10s_jerk_sign_jerk_v142_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p21s_jerk_sign_jerk_v143_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p42s_jerk_sign_jerk_v144_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p63s_jerk_sign_jerk_v145_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p126s_jerk_sign_jerk_v146_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p189s_jerk_sign_jerk_v147_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p252s_jerk_sign_jerk_v148_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p378s_jerk_sign_jerk_v149_signal,
    f21gcc_f21_grid_capex_cycle_capex_intensity_63p504s_jerk_sign_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_GRID_CAPEX_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
            "capex": capex, "assets": assets, "ppnenet": ppnenet,
            "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f21_capex_intensity', '_f21_capex_to_ppe', '_f21_capex_cycle')
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
    print(f"OK f21_grid_capex_cycle_jerk_001_150_claude: {n_features} features pass")
