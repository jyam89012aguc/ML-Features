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
def _f07_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f07_rollout_pulse(capex, w):
    m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = capex.rolling(w, min_periods=max(1, w // 2)).std()
    return (capex - m) / sd.replace(0, np.nan)


def _f07_capex_revenue_dynamics(capex, revenue, w):
    intensity = capex / revenue.replace(0, np.nan)
    rev_g = revenue.pct_change(periods=w)
    return intensity * rev_g

def f07srs_f07_store_rollout_signature_capi_mean_5d_base_v001_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_10d_base_v002_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_21d_base_v003_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_42d_base_v004_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_63d_base_v005_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_126d_base_v006_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_189d_base_v007_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_252d_base_v008_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_378d_base_v009_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_504d_base_v010_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _mean(ci, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_5d_base_v011_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_10d_base_v012_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_21d_base_v013_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_42d_base_v014_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_63d_base_v015_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_126d_base_v016_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_189d_base_v017_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_252d_base_v018_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_378d_base_v019_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_504d_base_v020_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _std(ci, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_5d_base_v021_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_10d_base_v022_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_21d_base_v023_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_42d_base_v024_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_63d_base_v025_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_126d_base_v026_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_189d_base_v027_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_252d_base_v028_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_378d_base_v029_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_504d_base_v030_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _z(ci, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_5d_base_v031_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_10d_base_v032_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_21d_base_v033_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_42d_base_v034_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_63d_base_v035_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_126d_base_v036_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_189d_base_v037_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_252d_base_v038_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_378d_base_v039_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_504d_base_v040_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = _ema(ci, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_5d_base_v041_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_10d_base_v042_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_21d_base_v043_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_42d_base_v044_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_63d_base_v045_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_126d_base_v046_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_189d_base_v047_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_252d_base_v048_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_378d_base_v049_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_504d_base_v050_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    result = (ci - ci.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_5d_base_v051_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_10d_base_v052_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_21d_base_v053_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_42d_base_v054_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_63d_base_v055_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_126d_base_v056_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_189d_base_v057_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_252d_base_v058_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_378d_base_v059_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_504d_base_v060_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_5d_base_v061_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_10d_base_v062_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_21d_base_v063_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_42d_base_v064_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_63d_base_v065_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_126d_base_v066_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_189d_base_v067_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_252d_base_v068_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_378d_base_v069_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_504d_base_v070_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_5d_base_v071_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_10d_base_v072_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_21d_base_v073_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_42d_base_v074_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_63d_base_v075_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f07srs_f07_store_rollout_signature_capi_mean_5d_base_v001_signal,
    f07srs_f07_store_rollout_signature_capi_mean_10d_base_v002_signal,
    f07srs_f07_store_rollout_signature_capi_mean_21d_base_v003_signal,
    f07srs_f07_store_rollout_signature_capi_mean_42d_base_v004_signal,
    f07srs_f07_store_rollout_signature_capi_mean_63d_base_v005_signal,
    f07srs_f07_store_rollout_signature_capi_mean_126d_base_v006_signal,
    f07srs_f07_store_rollout_signature_capi_mean_189d_base_v007_signal,
    f07srs_f07_store_rollout_signature_capi_mean_252d_base_v008_signal,
    f07srs_f07_store_rollout_signature_capi_mean_378d_base_v009_signal,
    f07srs_f07_store_rollout_signature_capi_mean_504d_base_v010_signal,
    f07srs_f07_store_rollout_signature_capi_std_5d_base_v011_signal,
    f07srs_f07_store_rollout_signature_capi_std_10d_base_v012_signal,
    f07srs_f07_store_rollout_signature_capi_std_21d_base_v013_signal,
    f07srs_f07_store_rollout_signature_capi_std_42d_base_v014_signal,
    f07srs_f07_store_rollout_signature_capi_std_63d_base_v015_signal,
    f07srs_f07_store_rollout_signature_capi_std_126d_base_v016_signal,
    f07srs_f07_store_rollout_signature_capi_std_189d_base_v017_signal,
    f07srs_f07_store_rollout_signature_capi_std_252d_base_v018_signal,
    f07srs_f07_store_rollout_signature_capi_std_378d_base_v019_signal,
    f07srs_f07_store_rollout_signature_capi_std_504d_base_v020_signal,
    f07srs_f07_store_rollout_signature_capi_z_5d_base_v021_signal,
    f07srs_f07_store_rollout_signature_capi_z_10d_base_v022_signal,
    f07srs_f07_store_rollout_signature_capi_z_21d_base_v023_signal,
    f07srs_f07_store_rollout_signature_capi_z_42d_base_v024_signal,
    f07srs_f07_store_rollout_signature_capi_z_63d_base_v025_signal,
    f07srs_f07_store_rollout_signature_capi_z_126d_base_v026_signal,
    f07srs_f07_store_rollout_signature_capi_z_189d_base_v027_signal,
    f07srs_f07_store_rollout_signature_capi_z_252d_base_v028_signal,
    f07srs_f07_store_rollout_signature_capi_z_378d_base_v029_signal,
    f07srs_f07_store_rollout_signature_capi_z_504d_base_v030_signal,
    f07srs_f07_store_rollout_signature_capi_ema_5d_base_v031_signal,
    f07srs_f07_store_rollout_signature_capi_ema_10d_base_v032_signal,
    f07srs_f07_store_rollout_signature_capi_ema_21d_base_v033_signal,
    f07srs_f07_store_rollout_signature_capi_ema_42d_base_v034_signal,
    f07srs_f07_store_rollout_signature_capi_ema_63d_base_v035_signal,
    f07srs_f07_store_rollout_signature_capi_ema_126d_base_v036_signal,
    f07srs_f07_store_rollout_signature_capi_ema_189d_base_v037_signal,
    f07srs_f07_store_rollout_signature_capi_ema_252d_base_v038_signal,
    f07srs_f07_store_rollout_signature_capi_ema_378d_base_v039_signal,
    f07srs_f07_store_rollout_signature_capi_ema_504d_base_v040_signal,
    f07srs_f07_store_rollout_signature_capi_diff_5d_base_v041_signal,
    f07srs_f07_store_rollout_signature_capi_diff_10d_base_v042_signal,
    f07srs_f07_store_rollout_signature_capi_diff_21d_base_v043_signal,
    f07srs_f07_store_rollout_signature_capi_diff_42d_base_v044_signal,
    f07srs_f07_store_rollout_signature_capi_diff_63d_base_v045_signal,
    f07srs_f07_store_rollout_signature_capi_diff_126d_base_v046_signal,
    f07srs_f07_store_rollout_signature_capi_diff_189d_base_v047_signal,
    f07srs_f07_store_rollout_signature_capi_diff_252d_base_v048_signal,
    f07srs_f07_store_rollout_signature_capi_diff_378d_base_v049_signal,
    f07srs_f07_store_rollout_signature_capi_diff_504d_base_v050_signal,
    f07srs_f07_store_rollout_signature_pulse_5d_base_v051_signal,
    f07srs_f07_store_rollout_signature_pulse_10d_base_v052_signal,
    f07srs_f07_store_rollout_signature_pulse_21d_base_v053_signal,
    f07srs_f07_store_rollout_signature_pulse_42d_base_v054_signal,
    f07srs_f07_store_rollout_signature_pulse_63d_base_v055_signal,
    f07srs_f07_store_rollout_signature_pulse_126d_base_v056_signal,
    f07srs_f07_store_rollout_signature_pulse_189d_base_v057_signal,
    f07srs_f07_store_rollout_signature_pulse_252d_base_v058_signal,
    f07srs_f07_store_rollout_signature_pulse_378d_base_v059_signal,
    f07srs_f07_store_rollout_signature_pulse_504d_base_v060_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_5d_base_v061_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_10d_base_v062_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_21d_base_v063_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_42d_base_v064_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_63d_base_v065_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_126d_base_v066_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_189d_base_v067_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_252d_base_v068_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_378d_base_v069_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_504d_base_v070_signal,
    f07srs_f07_store_rollout_signature_pulse_std_5d_base_v071_signal,
    f07srs_f07_store_rollout_signature_pulse_std_10d_base_v072_signal,
    f07srs_f07_store_rollout_signature_pulse_std_21d_base_v073_signal,
    f07srs_f07_store_rollout_signature_pulse_std_42d_base_v074_signal,
    f07srs_f07_store_rollout_signature_pulse_std_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_STORE_ROLLOUT_SIGNATURE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f07_capex_intensity", "_f07_rollout_pulse", "_f07_capex_revenue_dynamics")
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
    print(f"OK f07_store_rollout_signature_001_075_claude: {n_features} features pass")
