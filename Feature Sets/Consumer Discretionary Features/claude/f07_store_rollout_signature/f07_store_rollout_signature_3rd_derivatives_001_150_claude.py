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

def f07srs_f07_store_rollout_signature_capi_mean_5d_jerk_v001_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_10d_jerk_v002_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_21d_jerk_v003_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_42d_jerk_v004_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_63d_jerk_v005_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_126d_jerk_v006_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_189d_jerk_v007_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_252d_jerk_v008_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_378d_jerk_v009_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_mean_504d_jerk_v010_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _mean(ci, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_5d_jerk_v011_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_10d_jerk_v012_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_21d_jerk_v013_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_42d_jerk_v014_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_63d_jerk_v015_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_126d_jerk_v016_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_189d_jerk_v017_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_252d_jerk_v018_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_378d_jerk_v019_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_std_504d_jerk_v020_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _std(ci, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_5d_jerk_v021_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_10d_jerk_v022_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_21d_jerk_v023_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_42d_jerk_v024_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_63d_jerk_v025_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_126d_jerk_v026_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_189d_jerk_v027_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_252d_jerk_v028_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_378d_jerk_v029_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_z_504d_jerk_v030_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _z(ci, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_5d_jerk_v031_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_10d_jerk_v032_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_21d_jerk_v033_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_42d_jerk_v034_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_63d_jerk_v035_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_126d_jerk_v036_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_189d_jerk_v037_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_252d_jerk_v038_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_378d_jerk_v039_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_ema_504d_jerk_v040_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = _ema(ci, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_5d_jerk_v041_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_10d_jerk_v042_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_21d_jerk_v043_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_42d_jerk_v044_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_63d_jerk_v045_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_126d_jerk_v046_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_189d_jerk_v047_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(189)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_252d_jerk_v048_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_378d_jerk_v049_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(378)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_capi_diff_504d_jerk_v050_signal(capex, revenue, closeadj):
    ci = _f07_capex_intensity(capex, revenue)
    base = (ci - ci.shift(504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_5d_jerk_v051_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    base = p * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_10d_jerk_v052_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    base = p * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_21d_jerk_v053_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    base = p * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_42d_jerk_v054_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    base = p * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_63d_jerk_v055_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    base = p * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_126d_jerk_v056_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    base = p * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_189d_jerk_v057_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    base = p * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_252d_jerk_v058_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    base = p * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_378d_jerk_v059_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    base = p * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_504d_jerk_v060_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    base = p * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_5d_jerk_v061_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_10d_jerk_v062_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_21d_jerk_v063_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_42d_jerk_v064_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_63d_jerk_v065_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_126d_jerk_v066_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_189d_jerk_v067_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_252d_jerk_v068_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_378d_jerk_v069_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_mean_504d_jerk_v070_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    base = _mean(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_5d_jerk_v071_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_10d_jerk_v072_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_21d_jerk_v073_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_42d_jerk_v074_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_63d_jerk_v075_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_126d_jerk_v076_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_189d_jerk_v077_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_252d_jerk_v078_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_378d_jerk_v079_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_504d_jerk_v080_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    base = _std(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_5d_jerk_v081_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_10d_jerk_v082_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_21d_jerk_v083_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_42d_jerk_v084_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_63d_jerk_v085_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_126d_jerk_v086_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_189d_jerk_v087_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_252d_jerk_v088_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_378d_jerk_v089_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_504d_jerk_v090_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    base = _ema(p, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_5d_jerk_v091_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 5)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_10d_jerk_v092_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 10)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_21d_jerk_v093_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 21)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_42d_jerk_v094_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 42)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_63d_jerk_v095_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 63)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_126d_jerk_v096_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 126)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_189d_jerk_v097_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 189)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_252d_jerk_v098_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 252)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_378d_jerk_v099_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 378)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_504d_jerk_v100_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 504)
    base = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_5d_jerk_v101_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    base = d * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_10d_jerk_v102_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    base = d * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_21d_jerk_v103_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    base = d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_42d_jerk_v104_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    base = d * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_63d_jerk_v105_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    base = d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_126d_jerk_v106_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    base = d * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_189d_jerk_v107_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    base = d * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_252d_jerk_v108_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    base = d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_378d_jerk_v109_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    base = d * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_504d_jerk_v110_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    base = d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_5d_jerk_v111_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_10d_jerk_v112_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_21d_jerk_v113_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_42d_jerk_v114_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_63d_jerk_v115_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_126d_jerk_v116_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_189d_jerk_v117_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_252d_jerk_v118_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_378d_jerk_v119_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_504d_jerk_v120_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    base = _mean(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_5d_jerk_v121_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_10d_jerk_v122_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_21d_jerk_v123_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_42d_jerk_v124_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_63d_jerk_v125_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_126d_jerk_v126_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_189d_jerk_v127_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_252d_jerk_v128_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_378d_jerk_v129_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_504d_jerk_v130_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    base = _std(d, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_5d_jerk_v131_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_10d_jerk_v132_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_21d_jerk_v133_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_42d_jerk_v134_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_63d_jerk_v135_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_126d_jerk_v136_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_189d_jerk_v137_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_252d_jerk_v138_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_378d_jerk_v139_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_504d_jerk_v140_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    base = _z(d, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_5d_jerk_v141_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_10d_jerk_v142_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_21d_jerk_v143_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_42d_jerk_v144_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_63d_jerk_v145_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_126d_jerk_v146_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_189d_jerk_v147_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_252d_jerk_v148_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_378d_jerk_v149_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_504d_jerk_v150_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    base = d * (ppnenet / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f07srs_f07_store_rollout_signature_capi_mean_5d_jerk_v001_signal,
    f07srs_f07_store_rollout_signature_capi_mean_10d_jerk_v002_signal,
    f07srs_f07_store_rollout_signature_capi_mean_21d_jerk_v003_signal,
    f07srs_f07_store_rollout_signature_capi_mean_42d_jerk_v004_signal,
    f07srs_f07_store_rollout_signature_capi_mean_63d_jerk_v005_signal,
    f07srs_f07_store_rollout_signature_capi_mean_126d_jerk_v006_signal,
    f07srs_f07_store_rollout_signature_capi_mean_189d_jerk_v007_signal,
    f07srs_f07_store_rollout_signature_capi_mean_252d_jerk_v008_signal,
    f07srs_f07_store_rollout_signature_capi_mean_378d_jerk_v009_signal,
    f07srs_f07_store_rollout_signature_capi_mean_504d_jerk_v010_signal,
    f07srs_f07_store_rollout_signature_capi_std_5d_jerk_v011_signal,
    f07srs_f07_store_rollout_signature_capi_std_10d_jerk_v012_signal,
    f07srs_f07_store_rollout_signature_capi_std_21d_jerk_v013_signal,
    f07srs_f07_store_rollout_signature_capi_std_42d_jerk_v014_signal,
    f07srs_f07_store_rollout_signature_capi_std_63d_jerk_v015_signal,
    f07srs_f07_store_rollout_signature_capi_std_126d_jerk_v016_signal,
    f07srs_f07_store_rollout_signature_capi_std_189d_jerk_v017_signal,
    f07srs_f07_store_rollout_signature_capi_std_252d_jerk_v018_signal,
    f07srs_f07_store_rollout_signature_capi_std_378d_jerk_v019_signal,
    f07srs_f07_store_rollout_signature_capi_std_504d_jerk_v020_signal,
    f07srs_f07_store_rollout_signature_capi_z_5d_jerk_v021_signal,
    f07srs_f07_store_rollout_signature_capi_z_10d_jerk_v022_signal,
    f07srs_f07_store_rollout_signature_capi_z_21d_jerk_v023_signal,
    f07srs_f07_store_rollout_signature_capi_z_42d_jerk_v024_signal,
    f07srs_f07_store_rollout_signature_capi_z_63d_jerk_v025_signal,
    f07srs_f07_store_rollout_signature_capi_z_126d_jerk_v026_signal,
    f07srs_f07_store_rollout_signature_capi_z_189d_jerk_v027_signal,
    f07srs_f07_store_rollout_signature_capi_z_252d_jerk_v028_signal,
    f07srs_f07_store_rollout_signature_capi_z_378d_jerk_v029_signal,
    f07srs_f07_store_rollout_signature_capi_z_504d_jerk_v030_signal,
    f07srs_f07_store_rollout_signature_capi_ema_5d_jerk_v031_signal,
    f07srs_f07_store_rollout_signature_capi_ema_10d_jerk_v032_signal,
    f07srs_f07_store_rollout_signature_capi_ema_21d_jerk_v033_signal,
    f07srs_f07_store_rollout_signature_capi_ema_42d_jerk_v034_signal,
    f07srs_f07_store_rollout_signature_capi_ema_63d_jerk_v035_signal,
    f07srs_f07_store_rollout_signature_capi_ema_126d_jerk_v036_signal,
    f07srs_f07_store_rollout_signature_capi_ema_189d_jerk_v037_signal,
    f07srs_f07_store_rollout_signature_capi_ema_252d_jerk_v038_signal,
    f07srs_f07_store_rollout_signature_capi_ema_378d_jerk_v039_signal,
    f07srs_f07_store_rollout_signature_capi_ema_504d_jerk_v040_signal,
    f07srs_f07_store_rollout_signature_capi_diff_5d_jerk_v041_signal,
    f07srs_f07_store_rollout_signature_capi_diff_10d_jerk_v042_signal,
    f07srs_f07_store_rollout_signature_capi_diff_21d_jerk_v043_signal,
    f07srs_f07_store_rollout_signature_capi_diff_42d_jerk_v044_signal,
    f07srs_f07_store_rollout_signature_capi_diff_63d_jerk_v045_signal,
    f07srs_f07_store_rollout_signature_capi_diff_126d_jerk_v046_signal,
    f07srs_f07_store_rollout_signature_capi_diff_189d_jerk_v047_signal,
    f07srs_f07_store_rollout_signature_capi_diff_252d_jerk_v048_signal,
    f07srs_f07_store_rollout_signature_capi_diff_378d_jerk_v049_signal,
    f07srs_f07_store_rollout_signature_capi_diff_504d_jerk_v050_signal,
    f07srs_f07_store_rollout_signature_pulse_5d_jerk_v051_signal,
    f07srs_f07_store_rollout_signature_pulse_10d_jerk_v052_signal,
    f07srs_f07_store_rollout_signature_pulse_21d_jerk_v053_signal,
    f07srs_f07_store_rollout_signature_pulse_42d_jerk_v054_signal,
    f07srs_f07_store_rollout_signature_pulse_63d_jerk_v055_signal,
    f07srs_f07_store_rollout_signature_pulse_126d_jerk_v056_signal,
    f07srs_f07_store_rollout_signature_pulse_189d_jerk_v057_signal,
    f07srs_f07_store_rollout_signature_pulse_252d_jerk_v058_signal,
    f07srs_f07_store_rollout_signature_pulse_378d_jerk_v059_signal,
    f07srs_f07_store_rollout_signature_pulse_504d_jerk_v060_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_5d_jerk_v061_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_10d_jerk_v062_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_21d_jerk_v063_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_42d_jerk_v064_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_63d_jerk_v065_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_126d_jerk_v066_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_189d_jerk_v067_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_252d_jerk_v068_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_378d_jerk_v069_signal,
    f07srs_f07_store_rollout_signature_pulse_mean_504d_jerk_v070_signal,
    f07srs_f07_store_rollout_signature_pulse_std_5d_jerk_v071_signal,
    f07srs_f07_store_rollout_signature_pulse_std_10d_jerk_v072_signal,
    f07srs_f07_store_rollout_signature_pulse_std_21d_jerk_v073_signal,
    f07srs_f07_store_rollout_signature_pulse_std_42d_jerk_v074_signal,
    f07srs_f07_store_rollout_signature_pulse_std_63d_jerk_v075_signal,
    f07srs_f07_store_rollout_signature_pulse_std_126d_jerk_v076_signal,
    f07srs_f07_store_rollout_signature_pulse_std_189d_jerk_v077_signal,
    f07srs_f07_store_rollout_signature_pulse_std_252d_jerk_v078_signal,
    f07srs_f07_store_rollout_signature_pulse_std_378d_jerk_v079_signal,
    f07srs_f07_store_rollout_signature_pulse_std_504d_jerk_v080_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_5d_jerk_v081_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_10d_jerk_v082_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_21d_jerk_v083_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_42d_jerk_v084_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_63d_jerk_v085_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_126d_jerk_v086_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_189d_jerk_v087_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_252d_jerk_v088_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_378d_jerk_v089_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_504d_jerk_v090_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_5d_jerk_v091_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_10d_jerk_v092_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_21d_jerk_v093_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_42d_jerk_v094_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_63d_jerk_v095_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_126d_jerk_v096_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_189d_jerk_v097_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_252d_jerk_v098_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_378d_jerk_v099_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_504d_jerk_v100_signal,
    f07srs_f07_store_rollout_signature_dyn_5d_jerk_v101_signal,
    f07srs_f07_store_rollout_signature_dyn_10d_jerk_v102_signal,
    f07srs_f07_store_rollout_signature_dyn_21d_jerk_v103_signal,
    f07srs_f07_store_rollout_signature_dyn_42d_jerk_v104_signal,
    f07srs_f07_store_rollout_signature_dyn_63d_jerk_v105_signal,
    f07srs_f07_store_rollout_signature_dyn_126d_jerk_v106_signal,
    f07srs_f07_store_rollout_signature_dyn_189d_jerk_v107_signal,
    f07srs_f07_store_rollout_signature_dyn_252d_jerk_v108_signal,
    f07srs_f07_store_rollout_signature_dyn_378d_jerk_v109_signal,
    f07srs_f07_store_rollout_signature_dyn_504d_jerk_v110_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_5d_jerk_v111_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_10d_jerk_v112_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_21d_jerk_v113_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_42d_jerk_v114_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_63d_jerk_v115_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_126d_jerk_v116_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_189d_jerk_v117_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_252d_jerk_v118_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_378d_jerk_v119_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_504d_jerk_v120_signal,
    f07srs_f07_store_rollout_signature_dyn_std_5d_jerk_v121_signal,
    f07srs_f07_store_rollout_signature_dyn_std_10d_jerk_v122_signal,
    f07srs_f07_store_rollout_signature_dyn_std_21d_jerk_v123_signal,
    f07srs_f07_store_rollout_signature_dyn_std_42d_jerk_v124_signal,
    f07srs_f07_store_rollout_signature_dyn_std_63d_jerk_v125_signal,
    f07srs_f07_store_rollout_signature_dyn_std_126d_jerk_v126_signal,
    f07srs_f07_store_rollout_signature_dyn_std_189d_jerk_v127_signal,
    f07srs_f07_store_rollout_signature_dyn_std_252d_jerk_v128_signal,
    f07srs_f07_store_rollout_signature_dyn_std_378d_jerk_v129_signal,
    f07srs_f07_store_rollout_signature_dyn_std_504d_jerk_v130_signal,
    f07srs_f07_store_rollout_signature_dyn_z_5d_jerk_v131_signal,
    f07srs_f07_store_rollout_signature_dyn_z_10d_jerk_v132_signal,
    f07srs_f07_store_rollout_signature_dyn_z_21d_jerk_v133_signal,
    f07srs_f07_store_rollout_signature_dyn_z_42d_jerk_v134_signal,
    f07srs_f07_store_rollout_signature_dyn_z_63d_jerk_v135_signal,
    f07srs_f07_store_rollout_signature_dyn_z_126d_jerk_v136_signal,
    f07srs_f07_store_rollout_signature_dyn_z_189d_jerk_v137_signal,
    f07srs_f07_store_rollout_signature_dyn_z_252d_jerk_v138_signal,
    f07srs_f07_store_rollout_signature_dyn_z_378d_jerk_v139_signal,
    f07srs_f07_store_rollout_signature_dyn_z_504d_jerk_v140_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_5d_jerk_v141_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_10d_jerk_v142_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_21d_jerk_v143_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_42d_jerk_v144_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_63d_jerk_v145_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_126d_jerk_v146_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_189d_jerk_v147_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_252d_jerk_v148_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_378d_jerk_v149_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_STORE_ROLLOUT_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_store_rollout_signature_jerk_001_150_claude: {n_features} features pass")
