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
def _f03_margin_floor(grossmargin, w):
    g = grossmargin.pct_change(periods=w)
    return g - g.shift(w)


def _f03_margin_durability(grossmargin, w):
    base = grossmargin.rolling(w * 4, min_periods=max(1, w)).mean()
    return (grossmargin - base) / base.replace(0, np.nan).abs()


def _f03_margin_consistency(grossmargin, ebitdamargin, w):
    gm_g = grossmargin.pct_change(periods=w)
    em_g = ebitdamargin.pct_change(periods=w)
    return gm_g - 0.5 * em_g


# Build features programmatically to ensure uniqueness.
# Layout (150 features): 50 accel-slopes, 50 pulse-slopes, 50 sig-slopes.
# Each slot varies (base_window, slope_window, scaling) so bodies are unique.

# ---- accel slopes (v001-v050) ----

def f03dmd_f03_device_margin_durability_accel_21d_jerk_v001_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_21d_jerk_v002_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_21d_jerk_v003_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_21d_jerk_v004_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_21d_jerk_v005_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_63d_jerk_v006_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_63d_jerk_v007_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_63d_jerk_v008_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_63d_jerk_v009_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_63d_jerk_v010_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_126d_jerk_v011_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_126d_jerk_v012_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_126d_jerk_v013_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_126d_jerk_v014_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_126d_jerk_v015_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_252d_jerk_v016_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_252d_jerk_v017_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_252d_jerk_v018_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_252d_jerk_v019_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_252d_jerk_v020_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelmean_21d_jerk_v021_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_floor(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelmean_21d_jerk_v022_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_floor(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelmean_63d_jerk_v023_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_floor(grossmargin, 63), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelmean_63d_jerk_v024_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_floor(grossmargin, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelstd_21d_jerk_v025_signal(grossmargin, closeadj):
    base = _std(_f03_margin_floor(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelstd_21d_jerk_v026_signal(grossmargin, closeadj):
    base = _std(_f03_margin_floor(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelstd_63d_jerk_v027_signal(grossmargin, closeadj):
    base = _std(_f03_margin_floor(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelstd_63d_jerk_v028_signal(grossmargin, closeadj):
    base = _std(_f03_margin_floor(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxinst_21d_jerk_v029_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxinst_21d_jerk_v030_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxinst_63d_jerk_v031_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxinst_63d_jerk_v032_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxcap_21d_jerk_v033_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxcap_21d_jerk_v034_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxcap_63d_jerk_v035_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxcap_63d_jerk_v036_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxrev_21d_jerk_v037_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxrev_21d_jerk_v038_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxrev_63d_jerk_v039_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelxrev_63d_jerk_v040_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_42d_jerk_v041_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_42d_jerk_v042_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_189d_jerk_v043_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_189d_jerk_v044_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_378d_jerk_v045_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_378d_jerk_v046_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_504d_jerk_v047_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accel_504d_jerk_v048_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelsq_21d_jerk_v049_signal(grossmargin, closeadj):
    a = _f03_margin_floor(grossmargin, 21)
    base = a * a.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_accelsq_63d_jerk_v050_signal(grossmargin, closeadj):
    a = _f03_margin_floor(grossmargin, 63)
    base = a * a.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- pulse slopes (v051-v100) ----

def f03dmd_f03_device_margin_durability_pulse_21d_jerk_v051_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_21d_jerk_v052_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_21d_jerk_v053_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_21d_jerk_v054_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_21d_jerk_v055_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_63d_jerk_v056_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_63d_jerk_v057_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_63d_jerk_v058_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_63d_jerk_v059_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_63d_jerk_v060_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_126d_jerk_v061_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_126d_jerk_v062_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_126d_jerk_v063_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_126d_jerk_v064_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_126d_jerk_v065_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_252d_jerk_v066_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_252d_jerk_v067_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_252d_jerk_v068_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_252d_jerk_v069_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_252d_jerk_v070_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsemean_21d_jerk_v071_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_durability(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsemean_21d_jerk_v072_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_durability(grossmargin, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsemean_63d_jerk_v073_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_durability(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsemean_63d_jerk_v074_signal(grossmargin, closeadj):
    base = _mean(_f03_margin_durability(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsestd_21d_jerk_v075_signal(grossmargin, closeadj):
    base = _std(_f03_margin_durability(grossmargin, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsestd_21d_jerk_v076_signal(grossmargin, closeadj):
    base = _std(_f03_margin_durability(grossmargin, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsestd_63d_jerk_v077_signal(grossmargin, closeadj):
    base = _std(_f03_margin_durability(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsestd_63d_jerk_v078_signal(grossmargin, closeadj):
    base = _std(_f03_margin_durability(grossmargin, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexinst_21d_jerk_v079_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexinst_21d_jerk_v080_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexinst_63d_jerk_v081_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexinst_63d_jerk_v082_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexcap_21d_jerk_v083_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexcap_21d_jerk_v084_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexcap_63d_jerk_v085_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexcap_63d_jerk_v086_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexrev_21d_jerk_v087_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexrev_21d_jerk_v088_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexrev_63d_jerk_v089_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsexrev_63d_jerk_v090_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_42d_jerk_v091_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_42d_jerk_v092_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_189d_jerk_v093_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_189d_jerk_v094_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_378d_jerk_v095_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_378d_jerk_v096_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsesq_21d_jerk_v097_signal(grossmargin, closeadj):
    p = _f03_margin_durability(grossmargin, 21)
    base = p * p.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulsesq_63d_jerk_v098_signal(grossmargin, closeadj):
    p = _f03_margin_durability(grossmargin, 63)
    base = p * p.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_5d_jerk_v099_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_pulse_5d_jerk_v100_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- sig slopes (v101-v150) ----

def f03dmd_f03_device_margin_durability_sig_21d_jerk_v101_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_21d_jerk_v102_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_21d_jerk_v103_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_21d_jerk_v104_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_21d_jerk_v105_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_63d_jerk_v106_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_63d_jerk_v107_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_63d_jerk_v108_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_63d_jerk_v109_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_63d_jerk_v110_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_126d_jerk_v111_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_126d_jerk_v112_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_126d_jerk_v113_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_126d_jerk_v114_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_126d_jerk_v115_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v116_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v117_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v118_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v119_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v120_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigmean_21d_jerk_v121_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f03_margin_consistency(grossmargin, ebitdamargin, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigmean_21d_jerk_v122_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f03_margin_consistency(grossmargin, ebitdamargin, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigmean_63d_jerk_v123_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f03_margin_consistency(grossmargin, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigmean_63d_jerk_v124_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f03_margin_consistency(grossmargin, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigstd_21d_jerk_v125_signal(grossmargin, ebitdamargin, closeadj):
    base = _std(_f03_margin_consistency(grossmargin, ebitdamargin, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigstd_21d_jerk_v126_signal(grossmargin, ebitdamargin, closeadj):
    base = _std(_f03_margin_consistency(grossmargin, ebitdamargin, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigstd_63d_jerk_v127_signal(grossmargin, ebitdamargin, closeadj):
    base = _std(_f03_margin_consistency(grossmargin, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigstd_63d_jerk_v128_signal(grossmargin, ebitdamargin, closeadj):
    base = _std(_f03_margin_consistency(grossmargin, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxinst_21d_jerk_v129_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxinst_21d_jerk_v130_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxinst_63d_jerk_v131_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxinst_63d_jerk_v132_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * netmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxrev_21d_jerk_v133_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxrev_21d_jerk_v134_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxrev_63d_jerk_v135_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxrev_63d_jerk_v136_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxcap_21d_jerk_v137_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxcap_21d_jerk_v138_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxcap_63d_jerk_v139_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigxcap_63d_jerk_v140_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * ebitdamargin / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_42d_jerk_v141_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_42d_jerk_v142_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_189d_jerk_v143_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_189d_jerk_v144_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_378d_jerk_v145_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_378d_jerk_v146_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigsq_21d_jerk_v147_signal(grossmargin, ebitdamargin, closeadj):
    s = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    base = s * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sigsq_63d_jerk_v148_signal(grossmargin, ebitdamargin, closeadj):
    s = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    base = s * s.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v149_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f03dmd_f03_device_margin_durability_sig_252d_jerk_v150_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03dmd_f03_device_margin_durability_accel_21d_jerk_v001_signal,
    f03dmd_f03_device_margin_durability_accel_21d_jerk_v002_signal,
    f03dmd_f03_device_margin_durability_accel_21d_jerk_v003_signal,
    f03dmd_f03_device_margin_durability_accel_21d_jerk_v004_signal,
    f03dmd_f03_device_margin_durability_accel_21d_jerk_v005_signal,
    f03dmd_f03_device_margin_durability_accel_63d_jerk_v006_signal,
    f03dmd_f03_device_margin_durability_accel_63d_jerk_v007_signal,
    f03dmd_f03_device_margin_durability_accel_63d_jerk_v008_signal,
    f03dmd_f03_device_margin_durability_accel_63d_jerk_v009_signal,
    f03dmd_f03_device_margin_durability_accel_63d_jerk_v010_signal,
    f03dmd_f03_device_margin_durability_accel_126d_jerk_v011_signal,
    f03dmd_f03_device_margin_durability_accel_126d_jerk_v012_signal,
    f03dmd_f03_device_margin_durability_accel_126d_jerk_v013_signal,
    f03dmd_f03_device_margin_durability_accel_126d_jerk_v014_signal,
    f03dmd_f03_device_margin_durability_accel_126d_jerk_v015_signal,
    f03dmd_f03_device_margin_durability_accel_252d_jerk_v016_signal,
    f03dmd_f03_device_margin_durability_accel_252d_jerk_v017_signal,
    f03dmd_f03_device_margin_durability_accel_252d_jerk_v018_signal,
    f03dmd_f03_device_margin_durability_accel_252d_jerk_v019_signal,
    f03dmd_f03_device_margin_durability_accel_252d_jerk_v020_signal,
    f03dmd_f03_device_margin_durability_accelmean_21d_jerk_v021_signal,
    f03dmd_f03_device_margin_durability_accelmean_21d_jerk_v022_signal,
    f03dmd_f03_device_margin_durability_accelmean_63d_jerk_v023_signal,
    f03dmd_f03_device_margin_durability_accelmean_63d_jerk_v024_signal,
    f03dmd_f03_device_margin_durability_accelstd_21d_jerk_v025_signal,
    f03dmd_f03_device_margin_durability_accelstd_21d_jerk_v026_signal,
    f03dmd_f03_device_margin_durability_accelstd_63d_jerk_v027_signal,
    f03dmd_f03_device_margin_durability_accelstd_63d_jerk_v028_signal,
    f03dmd_f03_device_margin_durability_accelxinst_21d_jerk_v029_signal,
    f03dmd_f03_device_margin_durability_accelxinst_21d_jerk_v030_signal,
    f03dmd_f03_device_margin_durability_accelxinst_63d_jerk_v031_signal,
    f03dmd_f03_device_margin_durability_accelxinst_63d_jerk_v032_signal,
    f03dmd_f03_device_margin_durability_accelxcap_21d_jerk_v033_signal,
    f03dmd_f03_device_margin_durability_accelxcap_21d_jerk_v034_signal,
    f03dmd_f03_device_margin_durability_accelxcap_63d_jerk_v035_signal,
    f03dmd_f03_device_margin_durability_accelxcap_63d_jerk_v036_signal,
    f03dmd_f03_device_margin_durability_accelxrev_21d_jerk_v037_signal,
    f03dmd_f03_device_margin_durability_accelxrev_21d_jerk_v038_signal,
    f03dmd_f03_device_margin_durability_accelxrev_63d_jerk_v039_signal,
    f03dmd_f03_device_margin_durability_accelxrev_63d_jerk_v040_signal,
    f03dmd_f03_device_margin_durability_accel_42d_jerk_v041_signal,
    f03dmd_f03_device_margin_durability_accel_42d_jerk_v042_signal,
    f03dmd_f03_device_margin_durability_accel_189d_jerk_v043_signal,
    f03dmd_f03_device_margin_durability_accel_189d_jerk_v044_signal,
    f03dmd_f03_device_margin_durability_accel_378d_jerk_v045_signal,
    f03dmd_f03_device_margin_durability_accel_378d_jerk_v046_signal,
    f03dmd_f03_device_margin_durability_accel_504d_jerk_v047_signal,
    f03dmd_f03_device_margin_durability_accel_504d_jerk_v048_signal,
    f03dmd_f03_device_margin_durability_accelsq_21d_jerk_v049_signal,
    f03dmd_f03_device_margin_durability_accelsq_63d_jerk_v050_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_jerk_v051_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_jerk_v052_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_jerk_v053_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_jerk_v054_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_jerk_v055_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_jerk_v056_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_jerk_v057_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_jerk_v058_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_jerk_v059_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_jerk_v060_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_jerk_v061_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_jerk_v062_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_jerk_v063_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_jerk_v064_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_jerk_v065_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_jerk_v066_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_jerk_v067_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_jerk_v068_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_jerk_v069_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_jerk_v070_signal,
    f03dmd_f03_device_margin_durability_pulsemean_21d_jerk_v071_signal,
    f03dmd_f03_device_margin_durability_pulsemean_21d_jerk_v072_signal,
    f03dmd_f03_device_margin_durability_pulsemean_63d_jerk_v073_signal,
    f03dmd_f03_device_margin_durability_pulsemean_63d_jerk_v074_signal,
    f03dmd_f03_device_margin_durability_pulsestd_21d_jerk_v075_signal,
    f03dmd_f03_device_margin_durability_pulsestd_21d_jerk_v076_signal,
    f03dmd_f03_device_margin_durability_pulsestd_63d_jerk_v077_signal,
    f03dmd_f03_device_margin_durability_pulsestd_63d_jerk_v078_signal,
    f03dmd_f03_device_margin_durability_pulsexinst_21d_jerk_v079_signal,
    f03dmd_f03_device_margin_durability_pulsexinst_21d_jerk_v080_signal,
    f03dmd_f03_device_margin_durability_pulsexinst_63d_jerk_v081_signal,
    f03dmd_f03_device_margin_durability_pulsexinst_63d_jerk_v082_signal,
    f03dmd_f03_device_margin_durability_pulsexcap_21d_jerk_v083_signal,
    f03dmd_f03_device_margin_durability_pulsexcap_21d_jerk_v084_signal,
    f03dmd_f03_device_margin_durability_pulsexcap_63d_jerk_v085_signal,
    f03dmd_f03_device_margin_durability_pulsexcap_63d_jerk_v086_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_21d_jerk_v087_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_21d_jerk_v088_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_63d_jerk_v089_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_63d_jerk_v090_signal,
    f03dmd_f03_device_margin_durability_pulse_42d_jerk_v091_signal,
    f03dmd_f03_device_margin_durability_pulse_42d_jerk_v092_signal,
    f03dmd_f03_device_margin_durability_pulse_189d_jerk_v093_signal,
    f03dmd_f03_device_margin_durability_pulse_189d_jerk_v094_signal,
    f03dmd_f03_device_margin_durability_pulse_378d_jerk_v095_signal,
    f03dmd_f03_device_margin_durability_pulse_378d_jerk_v096_signal,
    f03dmd_f03_device_margin_durability_pulsesq_21d_jerk_v097_signal,
    f03dmd_f03_device_margin_durability_pulsesq_63d_jerk_v098_signal,
    f03dmd_f03_device_margin_durability_pulse_5d_jerk_v099_signal,
    f03dmd_f03_device_margin_durability_pulse_5d_jerk_v100_signal,
    f03dmd_f03_device_margin_durability_sig_21d_jerk_v101_signal,
    f03dmd_f03_device_margin_durability_sig_21d_jerk_v102_signal,
    f03dmd_f03_device_margin_durability_sig_21d_jerk_v103_signal,
    f03dmd_f03_device_margin_durability_sig_21d_jerk_v104_signal,
    f03dmd_f03_device_margin_durability_sig_21d_jerk_v105_signal,
    f03dmd_f03_device_margin_durability_sig_63d_jerk_v106_signal,
    f03dmd_f03_device_margin_durability_sig_63d_jerk_v107_signal,
    f03dmd_f03_device_margin_durability_sig_63d_jerk_v108_signal,
    f03dmd_f03_device_margin_durability_sig_63d_jerk_v109_signal,
    f03dmd_f03_device_margin_durability_sig_63d_jerk_v110_signal,
    f03dmd_f03_device_margin_durability_sig_126d_jerk_v111_signal,
    f03dmd_f03_device_margin_durability_sig_126d_jerk_v112_signal,
    f03dmd_f03_device_margin_durability_sig_126d_jerk_v113_signal,
    f03dmd_f03_device_margin_durability_sig_126d_jerk_v114_signal,
    f03dmd_f03_device_margin_durability_sig_126d_jerk_v115_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v116_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v117_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v118_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v119_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v120_signal,
    f03dmd_f03_device_margin_durability_sigmean_21d_jerk_v121_signal,
    f03dmd_f03_device_margin_durability_sigmean_21d_jerk_v122_signal,
    f03dmd_f03_device_margin_durability_sigmean_63d_jerk_v123_signal,
    f03dmd_f03_device_margin_durability_sigmean_63d_jerk_v124_signal,
    f03dmd_f03_device_margin_durability_sigstd_21d_jerk_v125_signal,
    f03dmd_f03_device_margin_durability_sigstd_21d_jerk_v126_signal,
    f03dmd_f03_device_margin_durability_sigstd_63d_jerk_v127_signal,
    f03dmd_f03_device_margin_durability_sigstd_63d_jerk_v128_signal,
    f03dmd_f03_device_margin_durability_sigxinst_21d_jerk_v129_signal,
    f03dmd_f03_device_margin_durability_sigxinst_21d_jerk_v130_signal,
    f03dmd_f03_device_margin_durability_sigxinst_63d_jerk_v131_signal,
    f03dmd_f03_device_margin_durability_sigxinst_63d_jerk_v132_signal,
    f03dmd_f03_device_margin_durability_sigxrev_21d_jerk_v133_signal,
    f03dmd_f03_device_margin_durability_sigxrev_21d_jerk_v134_signal,
    f03dmd_f03_device_margin_durability_sigxrev_63d_jerk_v135_signal,
    f03dmd_f03_device_margin_durability_sigxrev_63d_jerk_v136_signal,
    f03dmd_f03_device_margin_durability_sigxcap_21d_jerk_v137_signal,
    f03dmd_f03_device_margin_durability_sigxcap_21d_jerk_v138_signal,
    f03dmd_f03_device_margin_durability_sigxcap_63d_jerk_v139_signal,
    f03dmd_f03_device_margin_durability_sigxcap_63d_jerk_v140_signal,
    f03dmd_f03_device_margin_durability_sig_42d_jerk_v141_signal,
    f03dmd_f03_device_margin_durability_sig_42d_jerk_v142_signal,
    f03dmd_f03_device_margin_durability_sig_189d_jerk_v143_signal,
    f03dmd_f03_device_margin_durability_sig_189d_jerk_v144_signal,
    f03dmd_f03_device_margin_durability_sig_378d_jerk_v145_signal,
    f03dmd_f03_device_margin_durability_sig_378d_jerk_v146_signal,
    f03dmd_f03_device_margin_durability_sigsq_21d_jerk_v147_signal,
    f03dmd_f03_device_margin_durability_sigsq_63d_jerk_v148_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v149_signal,
    f03dmd_f03_device_margin_durability_sig_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_DEVICE_MARGIN_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {"closeadj": closeadj, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f03_margin_floor", "_f03_margin_durability", "_f03_margin_consistency")
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
    print(f"OK f03_device_margin_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
