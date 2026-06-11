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

# ===== folder domain primitives =====
def _f23_revenue_smoothness(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f23_contracted_proxy(revenue, deferredrev, w):
    ratio = deferredrev / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f23_stability_score(revenue, ebitda, w):
    rs = revenue.rolling(w, min_periods=max(1, w // 2)).std() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    es = ebitda.rolling(w, min_periods=max(1, w // 2)).std() / ebitda.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return 1.0 / (rs + es).replace(0, np.nan)



# ===== features =====

def f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_raw_base_v001_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_mean_w_base_v002_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_mean_w_base_v003_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_mean_w_base_v004_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_mean_w_base_v005_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_mean_w_base_v006_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_mean_w_base_v007_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_mean_w_base_v008_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_mean_w_base_v009_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_mean_w_base_v010_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_mean_w_base_v011_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_mean_w_base_v012_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_mean_w_base_v013_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_mean_w_base_v014_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_mean_w_base_v015_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_mean_w_base_v016_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_mean_w_base_v017_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_mean_w_base_v018_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_mean_w_base_v019_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_mean_w_base_v020_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_mean_w_base_v021_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _mean(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_std_w_base_v022_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_std_w_base_v023_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_std_w_base_v024_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_std_w_base_v025_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_std_w_base_v026_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_std_w_base_v027_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_std_w_base_v028_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_std_w_base_v029_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_std_w_base_v030_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_std_w_base_v031_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_std_w_base_v032_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_std_w_base_v033_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_std_w_base_v034_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_std_w_base_v035_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_std_w_base_v036_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_std_w_base_v037_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_std_w_base_v038_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_std_w_base_v039_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_std_w_base_v040_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_std_w_base_v041_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _std(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_z_w_base_v042_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_z_w_base_v043_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_z_w_base_v044_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_z_w_base_v045_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_z_w_base_v046_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_z_w_base_v047_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_z_w_base_v048_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_z_w_base_v049_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_z_w_base_v050_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_z_w_base_v051_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_z_w_base_v052_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_z_w_base_v053_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_z_w_base_v054_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_z_w_base_v055_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_z_w_base_v056_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_z_w_base_v057_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_z_w_base_v058_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_z_w_base_v059_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_z_w_base_v060_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_z_w_base_v061_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _z(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_ema_w_base_v062_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_ema_w_base_v063_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_ema_w_base_v064_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_ema_w_base_v065_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_ema_w_base_v066_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_ema_w_base_v067_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_ema_w_base_v068_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_ema_w_base_v069_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_ema_w_base_v070_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_ema_w_base_v071_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_ema_w_base_v072_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_ema_w_base_v073_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_ema_w_base_v074_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_ema_w_base_v075_signal(revenue, closeadj):
    base = _f23_revenue_smoothness(revenue, 5)
    result = _ema(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_raw_base_v001_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_mean_w_base_v002_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_mean_w_base_v003_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_mean_w_base_v004_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_mean_w_base_v005_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_mean_w_base_v006_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_mean_w_base_v007_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_mean_w_base_v008_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_mean_w_base_v009_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_mean_w_base_v010_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_mean_w_base_v011_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_mean_w_base_v012_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_mean_w_base_v013_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_mean_w_base_v014_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_mean_w_base_v015_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_mean_w_base_v016_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_mean_w_base_v017_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_mean_w_base_v018_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_mean_w_base_v019_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_mean_w_base_v020_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_mean_w_base_v021_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_std_w_base_v022_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_std_w_base_v023_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_std_w_base_v024_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_std_w_base_v025_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_std_w_base_v026_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_std_w_base_v027_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_std_w_base_v028_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_std_w_base_v029_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_std_w_base_v030_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_std_w_base_v031_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_std_w_base_v032_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_std_w_base_v033_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_std_w_base_v034_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_std_w_base_v035_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_std_w_base_v036_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_std_w_base_v037_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_std_w_base_v038_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_std_w_base_v039_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_std_w_base_v040_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_std_w_base_v041_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_z_w_base_v042_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_z_w_base_v043_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_z_w_base_v044_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_z_w_base_v045_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_z_w_base_v046_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_z_w_base_v047_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_z_w_base_v048_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_z_w_base_v049_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_z_w_base_v050_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_z_w_base_v051_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_z_w_base_v052_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_z_w_base_v053_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_z_w_base_v054_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_z_w_base_v055_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p90s_z_w_base_v056_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p105s_z_w_base_v057_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p168s_z_w_base_v058_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p210s_z_w_base_v059_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p315s_z_w_base_v060_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p420s_z_w_base_v061_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p5s_ema_w_base_v062_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p10s_ema_w_base_v063_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p21s_ema_w_base_v064_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p42s_ema_w_base_v065_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p63s_ema_w_base_v066_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p126s_ema_w_base_v067_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p189s_ema_w_base_v068_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p252s_ema_w_base_v069_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p378s_ema_w_base_v070_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p504s_ema_w_base_v071_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p7s_ema_w_base_v072_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p14s_ema_w_base_v073_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p30s_ema_w_base_v074_signal,
    f23tre_f23_transmission_revenue_revenue_smoothness_5p45s_ema_w_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_TRANSMISSION_REVENUE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f23_revenue_smoothness', '_f23_contracted_proxy', '_f23_stability_score')
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
    print(f"OK f23_transmission_revenue_001_075_claude: {n_features} features pass")
