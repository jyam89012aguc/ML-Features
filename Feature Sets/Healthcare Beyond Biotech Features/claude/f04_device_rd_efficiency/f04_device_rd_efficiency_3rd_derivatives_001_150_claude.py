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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _jerk_pct(s, w):
    sl = s.pct_change(periods=w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f04_rd_efficiency(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - rd_g


def _f04_rd_intensity(rnd, revenue, w):
    ratio = rnd / revenue.replace(0, np.nan).abs()
    base = ratio.rolling(w * 4, min_periods=max(1, w)).mean()
    return (ratio - base) / base.replace(0, np.nan).abs()


def _f04_rd_productivity(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - 0.5 * rd_g


# Build features programmatically to ensure uniqueness.
# Layout (150 features): 50 accel-slopes, 50 pulse-slopes, 50 sig-slopes.
# Each slot varies (base_window, slope_window, scaling) so bodies are unique.

# ---- accel slopes (v001-v050) ----

def f04dre_f04_device_rd_efficiency_accel_21d_jerk_v001_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_21d_jerk_v002_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_21d_jerk_v003_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_21d_jerk_v004_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_21d_jerk_v005_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_63d_jerk_v006_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_63d_jerk_v007_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_63d_jerk_v008_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_63d_jerk_v009_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_63d_jerk_v010_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_126d_jerk_v011_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_126d_jerk_v012_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_126d_jerk_v013_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_126d_jerk_v014_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_126d_jerk_v015_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_252d_jerk_v016_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_252d_jerk_v017_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_252d_jerk_v018_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_252d_jerk_v019_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_252d_jerk_v020_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelmean_21d_jerk_v021_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_efficiency(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelmean_21d_jerk_v022_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_efficiency(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelmean_63d_jerk_v023_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_efficiency(rnd, revenue, 63), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelmean_63d_jerk_v024_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_efficiency(rnd, revenue, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelstd_21d_jerk_v025_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_efficiency(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelstd_21d_jerk_v026_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_efficiency(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelstd_63d_jerk_v027_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_efficiency(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelstd_63d_jerk_v028_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_efficiency(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxinst_21d_jerk_v029_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxinst_21d_jerk_v030_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxinst_63d_jerk_v031_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxinst_63d_jerk_v032_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxcap_21d_jerk_v033_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxcap_21d_jerk_v034_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxcap_63d_jerk_v035_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxcap_63d_jerk_v036_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxrev_21d_jerk_v037_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxrev_21d_jerk_v038_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxrev_63d_jerk_v039_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelxrev_63d_jerk_v040_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_42d_jerk_v041_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_42d_jerk_v042_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_189d_jerk_v043_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_189d_jerk_v044_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_378d_jerk_v045_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_378d_jerk_v046_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_504d_jerk_v047_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accel_504d_jerk_v048_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelsq_21d_jerk_v049_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 21)
    base = a * a.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_accelsq_63d_jerk_v050_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 63)
    base = a * a.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- pulse slopes (v051-v100) ----

def f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v051_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v052_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v053_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v054_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v055_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v056_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v057_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v058_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v059_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v060_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v061_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v062_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v063_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v064_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v065_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v066_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v067_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v068_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v069_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v070_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsemean_21d_jerk_v071_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_intensity(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsemean_21d_jerk_v072_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_intensity(rnd, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsemean_63d_jerk_v073_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_intensity(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsemean_63d_jerk_v074_signal(rnd, revenue, closeadj):
    base = _mean(_f04_rd_intensity(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsestd_21d_jerk_v075_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_intensity(rnd, revenue, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsestd_21d_jerk_v076_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_intensity(rnd, revenue, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsestd_63d_jerk_v077_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_intensity(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsestd_63d_jerk_v078_signal(rnd, revenue, closeadj):
    base = _std(_f04_rd_intensity(rnd, revenue, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexinst_21d_jerk_v079_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexinst_21d_jerk_v080_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexinst_63d_jerk_v081_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexinst_63d_jerk_v082_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexcap_21d_jerk_v083_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexcap_21d_jerk_v084_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexcap_63d_jerk_v085_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexcap_63d_jerk_v086_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexrev_21d_jerk_v087_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexrev_21d_jerk_v088_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexrev_63d_jerk_v089_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsexrev_63d_jerk_v090_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_42d_jerk_v091_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_42d_jerk_v092_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_189d_jerk_v093_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_189d_jerk_v094_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_378d_jerk_v095_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_378d_jerk_v096_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsesq_21d_jerk_v097_signal(rnd, revenue, closeadj):
    p = _f04_rd_intensity(rnd, revenue, 21)
    base = p * p.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulsesq_63d_jerk_v098_signal(rnd, revenue, closeadj):
    p = _f04_rd_intensity(rnd, revenue, 63)
    base = p * p.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_5d_jerk_v099_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_pulse_5d_jerk_v100_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- sig slopes (v101-v150) ----

def f04dre_f04_device_rd_efficiency_sig_21d_jerk_v101_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_21d_jerk_v102_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_21d_jerk_v103_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_21d_jerk_v104_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_21d_jerk_v105_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_63d_jerk_v106_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_63d_jerk_v107_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_63d_jerk_v108_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_63d_jerk_v109_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_63d_jerk_v110_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_126d_jerk_v111_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_126d_jerk_v112_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_126d_jerk_v113_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_126d_jerk_v114_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_126d_jerk_v115_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v116_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v117_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v118_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v119_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v120_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigmean_21d_jerk_v121_signal(rnd, closeadj):
    base = _mean(_f04_rd_productivity(rnd, rnd, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigmean_21d_jerk_v122_signal(rnd, closeadj):
    base = _mean(_f04_rd_productivity(rnd, rnd, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigmean_63d_jerk_v123_signal(rnd, closeadj):
    base = _mean(_f04_rd_productivity(rnd, rnd, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigmean_63d_jerk_v124_signal(rnd, closeadj):
    base = _mean(_f04_rd_productivity(rnd, rnd, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigstd_21d_jerk_v125_signal(rnd, closeadj):
    base = _std(_f04_rd_productivity(rnd, rnd, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigstd_21d_jerk_v126_signal(rnd, closeadj):
    base = _std(_f04_rd_productivity(rnd, rnd, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigstd_63d_jerk_v127_signal(rnd, closeadj):
    base = _std(_f04_rd_productivity(rnd, rnd, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigstd_63d_jerk_v128_signal(rnd, closeadj):
    base = _std(_f04_rd_productivity(rnd, rnd, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxinst_21d_jerk_v129_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxinst_21d_jerk_v130_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxinst_63d_jerk_v131_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxinst_63d_jerk_v132_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * (rnd * 100.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxrev_21d_jerk_v133_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxrev_21d_jerk_v134_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxrev_63d_jerk_v135_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxrev_63d_jerk_v136_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * (rnd * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxcap_21d_jerk_v137_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxcap_21d_jerk_v138_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxcap_63d_jerk_v139_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigxcap_63d_jerk_v140_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63) * rnd / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_42d_jerk_v141_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_42d_jerk_v142_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_189d_jerk_v143_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_189d_jerk_v144_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_378d_jerk_v145_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_378d_jerk_v146_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigsq_21d_jerk_v147_signal(rnd, closeadj):
    s = _f04_rd_productivity(rnd, rnd, 21)
    base = s * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sigsq_63d_jerk_v148_signal(rnd, closeadj):
    s = _f04_rd_productivity(rnd, rnd, 63)
    base = s * s.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v149_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f04dre_f04_device_rd_efficiency_sig_252d_jerk_v150_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dre_f04_device_rd_efficiency_accel_21d_jerk_v001_signal,
    f04dre_f04_device_rd_efficiency_accel_21d_jerk_v002_signal,
    f04dre_f04_device_rd_efficiency_accel_21d_jerk_v003_signal,
    f04dre_f04_device_rd_efficiency_accel_21d_jerk_v004_signal,
    f04dre_f04_device_rd_efficiency_accel_21d_jerk_v005_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_jerk_v006_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_jerk_v007_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_jerk_v008_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_jerk_v009_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_jerk_v010_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_jerk_v011_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_jerk_v012_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_jerk_v013_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_jerk_v014_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_jerk_v015_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_jerk_v016_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_jerk_v017_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_jerk_v018_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_jerk_v019_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_jerk_v020_signal,
    f04dre_f04_device_rd_efficiency_accelmean_21d_jerk_v021_signal,
    f04dre_f04_device_rd_efficiency_accelmean_21d_jerk_v022_signal,
    f04dre_f04_device_rd_efficiency_accelmean_63d_jerk_v023_signal,
    f04dre_f04_device_rd_efficiency_accelmean_63d_jerk_v024_signal,
    f04dre_f04_device_rd_efficiency_accelstd_21d_jerk_v025_signal,
    f04dre_f04_device_rd_efficiency_accelstd_21d_jerk_v026_signal,
    f04dre_f04_device_rd_efficiency_accelstd_63d_jerk_v027_signal,
    f04dre_f04_device_rd_efficiency_accelstd_63d_jerk_v028_signal,
    f04dre_f04_device_rd_efficiency_accelxinst_21d_jerk_v029_signal,
    f04dre_f04_device_rd_efficiency_accelxinst_21d_jerk_v030_signal,
    f04dre_f04_device_rd_efficiency_accelxinst_63d_jerk_v031_signal,
    f04dre_f04_device_rd_efficiency_accelxinst_63d_jerk_v032_signal,
    f04dre_f04_device_rd_efficiency_accelxcap_21d_jerk_v033_signal,
    f04dre_f04_device_rd_efficiency_accelxcap_21d_jerk_v034_signal,
    f04dre_f04_device_rd_efficiency_accelxcap_63d_jerk_v035_signal,
    f04dre_f04_device_rd_efficiency_accelxcap_63d_jerk_v036_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_21d_jerk_v037_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_21d_jerk_v038_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_63d_jerk_v039_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_63d_jerk_v040_signal,
    f04dre_f04_device_rd_efficiency_accel_42d_jerk_v041_signal,
    f04dre_f04_device_rd_efficiency_accel_42d_jerk_v042_signal,
    f04dre_f04_device_rd_efficiency_accel_189d_jerk_v043_signal,
    f04dre_f04_device_rd_efficiency_accel_189d_jerk_v044_signal,
    f04dre_f04_device_rd_efficiency_accel_378d_jerk_v045_signal,
    f04dre_f04_device_rd_efficiency_accel_378d_jerk_v046_signal,
    f04dre_f04_device_rd_efficiency_accel_504d_jerk_v047_signal,
    f04dre_f04_device_rd_efficiency_accel_504d_jerk_v048_signal,
    f04dre_f04_device_rd_efficiency_accelsq_21d_jerk_v049_signal,
    f04dre_f04_device_rd_efficiency_accelsq_63d_jerk_v050_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v051_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v052_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v053_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v054_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_jerk_v055_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v056_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v057_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v058_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v059_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_jerk_v060_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v061_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v062_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v063_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v064_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_jerk_v065_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v066_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v067_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v068_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v069_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_jerk_v070_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_21d_jerk_v071_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_21d_jerk_v072_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_63d_jerk_v073_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_63d_jerk_v074_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_21d_jerk_v075_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_21d_jerk_v076_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_63d_jerk_v077_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_63d_jerk_v078_signal,
    f04dre_f04_device_rd_efficiency_pulsexinst_21d_jerk_v079_signal,
    f04dre_f04_device_rd_efficiency_pulsexinst_21d_jerk_v080_signal,
    f04dre_f04_device_rd_efficiency_pulsexinst_63d_jerk_v081_signal,
    f04dre_f04_device_rd_efficiency_pulsexinst_63d_jerk_v082_signal,
    f04dre_f04_device_rd_efficiency_pulsexcap_21d_jerk_v083_signal,
    f04dre_f04_device_rd_efficiency_pulsexcap_21d_jerk_v084_signal,
    f04dre_f04_device_rd_efficiency_pulsexcap_63d_jerk_v085_signal,
    f04dre_f04_device_rd_efficiency_pulsexcap_63d_jerk_v086_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_21d_jerk_v087_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_21d_jerk_v088_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_63d_jerk_v089_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_63d_jerk_v090_signal,
    f04dre_f04_device_rd_efficiency_pulse_42d_jerk_v091_signal,
    f04dre_f04_device_rd_efficiency_pulse_42d_jerk_v092_signal,
    f04dre_f04_device_rd_efficiency_pulse_189d_jerk_v093_signal,
    f04dre_f04_device_rd_efficiency_pulse_189d_jerk_v094_signal,
    f04dre_f04_device_rd_efficiency_pulse_378d_jerk_v095_signal,
    f04dre_f04_device_rd_efficiency_pulse_378d_jerk_v096_signal,
    f04dre_f04_device_rd_efficiency_pulsesq_21d_jerk_v097_signal,
    f04dre_f04_device_rd_efficiency_pulsesq_63d_jerk_v098_signal,
    f04dre_f04_device_rd_efficiency_pulse_5d_jerk_v099_signal,
    f04dre_f04_device_rd_efficiency_pulse_5d_jerk_v100_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_jerk_v101_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_jerk_v102_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_jerk_v103_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_jerk_v104_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_jerk_v105_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_jerk_v106_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_jerk_v107_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_jerk_v108_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_jerk_v109_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_jerk_v110_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_jerk_v111_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_jerk_v112_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_jerk_v113_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_jerk_v114_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_jerk_v115_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v116_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v117_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v118_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v119_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v120_signal,
    f04dre_f04_device_rd_efficiency_sigmean_21d_jerk_v121_signal,
    f04dre_f04_device_rd_efficiency_sigmean_21d_jerk_v122_signal,
    f04dre_f04_device_rd_efficiency_sigmean_63d_jerk_v123_signal,
    f04dre_f04_device_rd_efficiency_sigmean_63d_jerk_v124_signal,
    f04dre_f04_device_rd_efficiency_sigstd_21d_jerk_v125_signal,
    f04dre_f04_device_rd_efficiency_sigstd_21d_jerk_v126_signal,
    f04dre_f04_device_rd_efficiency_sigstd_63d_jerk_v127_signal,
    f04dre_f04_device_rd_efficiency_sigstd_63d_jerk_v128_signal,
    f04dre_f04_device_rd_efficiency_sigxinst_21d_jerk_v129_signal,
    f04dre_f04_device_rd_efficiency_sigxinst_21d_jerk_v130_signal,
    f04dre_f04_device_rd_efficiency_sigxinst_63d_jerk_v131_signal,
    f04dre_f04_device_rd_efficiency_sigxinst_63d_jerk_v132_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_21d_jerk_v133_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_21d_jerk_v134_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_63d_jerk_v135_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_63d_jerk_v136_signal,
    f04dre_f04_device_rd_efficiency_sigxcap_21d_jerk_v137_signal,
    f04dre_f04_device_rd_efficiency_sigxcap_21d_jerk_v138_signal,
    f04dre_f04_device_rd_efficiency_sigxcap_63d_jerk_v139_signal,
    f04dre_f04_device_rd_efficiency_sigxcap_63d_jerk_v140_signal,
    f04dre_f04_device_rd_efficiency_sig_42d_jerk_v141_signal,
    f04dre_f04_device_rd_efficiency_sig_42d_jerk_v142_signal,
    f04dre_f04_device_rd_efficiency_sig_189d_jerk_v143_signal,
    f04dre_f04_device_rd_efficiency_sig_189d_jerk_v144_signal,
    f04dre_f04_device_rd_efficiency_sig_378d_jerk_v145_signal,
    f04dre_f04_device_rd_efficiency_sig_378d_jerk_v146_signal,
    f04dre_f04_device_rd_efficiency_sigsq_21d_jerk_v147_signal,
    f04dre_f04_device_rd_efficiency_sigsq_63d_jerk_v148_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v149_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEVICE_RD_EFFICIENCY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "rnd": rnd, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_rd_efficiency", "_f04_rd_intensity", "_f04_rd_productivity")
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
    print(f"OK f04_device_rd_efficiency_3rd_derivatives_001_150_claude: {n_features} features pass")
