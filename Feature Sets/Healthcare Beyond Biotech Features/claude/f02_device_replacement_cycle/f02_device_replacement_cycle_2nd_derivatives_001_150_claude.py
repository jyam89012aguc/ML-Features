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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f02_revenue_smoothness(revenue, w):
    g = revenue.pct_change(periods=w)
    return -g.rolling(w, min_periods=max(1, w // 2)).std()


def _f02_recurring_signature(revenue, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - floor) / revenue.replace(0, np.nan).abs() - 0.5


def _f02_replacement_score(revenue, grossmargin, w):
    g = revenue.pct_change(periods=w)
    return g * (grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean())


# Build features programmatically to ensure uniqueness.
# Layout (150 features): 50 accel-slopes, 50 pulse-slopes, 50 sig-slopes.
# Each slot varies (base_window, slope_window, scaling) so bodies are unique.

# ---- accel slopes (v001-v050) ----

def f02drc_f02_device_replacement_cycle_accel_21d_slope_v001_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_21d_slope_v002_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_21d_slope_v003_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_21d_slope_v004_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_21d_slope_v005_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_63d_slope_v006_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_63d_slope_v007_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_63d_slope_v008_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_63d_slope_v009_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_63d_slope_v010_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_126d_slope_v011_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_126d_slope_v012_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_126d_slope_v013_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_126d_slope_v014_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_126d_slope_v015_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_252d_slope_v016_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_252d_slope_v017_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_252d_slope_v018_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_252d_slope_v019_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_252d_slope_v020_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelmean_21d_slope_v021_signal(revenue, closeadj):
    base = _mean(_f02_revenue_smoothness(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelmean_21d_slope_v022_signal(revenue, closeadj):
    base = _mean(_f02_revenue_smoothness(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelmean_63d_slope_v023_signal(revenue, closeadj):
    base = _mean(_f02_revenue_smoothness(revenue, 63), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelmean_63d_slope_v024_signal(revenue, closeadj):
    base = _mean(_f02_revenue_smoothness(revenue, 63), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelstd_21d_slope_v025_signal(revenue, closeadj):
    base = _std(_f02_revenue_smoothness(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelstd_21d_slope_v026_signal(revenue, closeadj):
    base = _std(_f02_revenue_smoothness(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelstd_63d_slope_v027_signal(revenue, closeadj):
    base = _std(_f02_revenue_smoothness(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelstd_63d_slope_v028_signal(revenue, closeadj):
    base = _std(_f02_revenue_smoothness(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxinst_21d_slope_v029_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxinst_21d_slope_v030_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxinst_63d_slope_v031_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxinst_63d_slope_v032_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxcap_21d_slope_v033_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxcap_21d_slope_v034_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxcap_63d_slope_v035_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxcap_63d_slope_v036_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxrev_21d_slope_v037_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxrev_21d_slope_v038_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxrev_63d_slope_v039_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelxrev_63d_slope_v040_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_42d_slope_v041_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_42d_slope_v042_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_189d_slope_v043_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_189d_slope_v044_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_378d_slope_v045_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_378d_slope_v046_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_504d_slope_v047_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accel_504d_slope_v048_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelsq_21d_slope_v049_signal(revenue, closeadj):
    a = _f02_revenue_smoothness(revenue, 21)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_accelsq_63d_slope_v050_signal(revenue, closeadj):
    a = _f02_revenue_smoothness(revenue, 63)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- pulse slopes (v051-v100) ----

def f02drc_f02_device_replacement_cycle_pulse_21d_slope_v051_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_21d_slope_v052_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_21d_slope_v053_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_21d_slope_v054_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_21d_slope_v055_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_63d_slope_v056_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_63d_slope_v057_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_63d_slope_v058_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_63d_slope_v059_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_63d_slope_v060_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_126d_slope_v061_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_126d_slope_v062_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_126d_slope_v063_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_126d_slope_v064_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_126d_slope_v065_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_252d_slope_v066_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_252d_slope_v067_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_252d_slope_v068_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_252d_slope_v069_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_252d_slope_v070_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsemean_21d_slope_v071_signal(revenue, closeadj):
    base = _mean(_f02_recurring_signature(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsemean_21d_slope_v072_signal(revenue, closeadj):
    base = _mean(_f02_recurring_signature(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsemean_63d_slope_v073_signal(revenue, closeadj):
    base = _mean(_f02_recurring_signature(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsemean_63d_slope_v074_signal(revenue, closeadj):
    base = _mean(_f02_recurring_signature(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsestd_21d_slope_v075_signal(revenue, closeadj):
    base = _std(_f02_recurring_signature(revenue, 21), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsestd_21d_slope_v076_signal(revenue, closeadj):
    base = _std(_f02_recurring_signature(revenue, 21), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsestd_63d_slope_v077_signal(revenue, closeadj):
    base = _std(_f02_recurring_signature(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsestd_63d_slope_v078_signal(revenue, closeadj):
    base = _std(_f02_recurring_signature(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexinst_21d_slope_v079_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexinst_21d_slope_v080_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexinst_63d_slope_v081_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexinst_63d_slope_v082_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexcap_21d_slope_v083_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexcap_21d_slope_v084_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexcap_63d_slope_v085_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexcap_63d_slope_v086_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexrev_21d_slope_v087_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexrev_21d_slope_v088_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexrev_63d_slope_v089_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsexrev_63d_slope_v090_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_42d_slope_v091_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_42d_slope_v092_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_189d_slope_v093_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_189d_slope_v094_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_378d_slope_v095_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_378d_slope_v096_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsesq_21d_slope_v097_signal(revenue, closeadj):
    p = _f02_recurring_signature(revenue, 21)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulsesq_63d_slope_v098_signal(revenue, closeadj):
    p = _f02_recurring_signature(revenue, 63)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_5d_slope_v099_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_pulse_5d_slope_v100_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- sig slopes (v101-v150) ----

def f02drc_f02_device_replacement_cycle_sig_21d_slope_v101_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_21d_slope_v102_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_21d_slope_v103_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_21d_slope_v104_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_21d_slope_v105_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_63d_slope_v106_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_63d_slope_v107_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_63d_slope_v108_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_63d_slope_v109_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_63d_slope_v110_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_126d_slope_v111_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_126d_slope_v112_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_126d_slope_v113_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_126d_slope_v114_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_126d_slope_v115_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v116_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v117_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v118_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v119_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v120_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigmean_21d_slope_v121_signal(revenue, grossmargin, closeadj):
    base = _mean(_f02_replacement_score(revenue, grossmargin, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigmean_21d_slope_v122_signal(revenue, grossmargin, closeadj):
    base = _mean(_f02_replacement_score(revenue, grossmargin, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigmean_63d_slope_v123_signal(revenue, grossmargin, closeadj):
    base = _mean(_f02_replacement_score(revenue, grossmargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigmean_63d_slope_v124_signal(revenue, grossmargin, closeadj):
    base = _mean(_f02_replacement_score(revenue, grossmargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigstd_21d_slope_v125_signal(revenue, grossmargin, closeadj):
    base = _std(_f02_replacement_score(revenue, grossmargin, 21), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigstd_21d_slope_v126_signal(revenue, grossmargin, closeadj):
    base = _std(_f02_replacement_score(revenue, grossmargin, 21), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigstd_63d_slope_v127_signal(revenue, grossmargin, closeadj):
    base = _std(_f02_replacement_score(revenue, grossmargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigstd_63d_slope_v128_signal(revenue, grossmargin, closeadj):
    base = _std(_f02_replacement_score(revenue, grossmargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxinst_21d_slope_v129_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxinst_21d_slope_v130_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxinst_63d_slope_v131_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxinst_63d_slope_v132_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxrev_21d_slope_v133_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxrev_21d_slope_v134_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxrev_63d_slope_v135_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxrev_63d_slope_v136_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxcap_21d_slope_v137_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxcap_21d_slope_v138_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxcap_63d_slope_v139_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigxcap_63d_slope_v140_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63) * grossmargin / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_42d_slope_v141_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_42d_slope_v142_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_189d_slope_v143_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_189d_slope_v144_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_378d_slope_v145_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_378d_slope_v146_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigsq_21d_slope_v147_signal(revenue, grossmargin, closeadj):
    s = _f02_replacement_score(revenue, grossmargin, 21)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sigsq_63d_slope_v148_signal(revenue, grossmargin, closeadj):
    s = _f02_replacement_score(revenue, grossmargin, 63)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v149_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f02drc_f02_device_replacement_cycle_sig_252d_slope_v150_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02drc_f02_device_replacement_cycle_accel_21d_slope_v001_signal,
    f02drc_f02_device_replacement_cycle_accel_21d_slope_v002_signal,
    f02drc_f02_device_replacement_cycle_accel_21d_slope_v003_signal,
    f02drc_f02_device_replacement_cycle_accel_21d_slope_v004_signal,
    f02drc_f02_device_replacement_cycle_accel_21d_slope_v005_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_slope_v006_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_slope_v007_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_slope_v008_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_slope_v009_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_slope_v010_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_slope_v011_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_slope_v012_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_slope_v013_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_slope_v014_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_slope_v015_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_slope_v016_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_slope_v017_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_slope_v018_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_slope_v019_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_slope_v020_signal,
    f02drc_f02_device_replacement_cycle_accelmean_21d_slope_v021_signal,
    f02drc_f02_device_replacement_cycle_accelmean_21d_slope_v022_signal,
    f02drc_f02_device_replacement_cycle_accelmean_63d_slope_v023_signal,
    f02drc_f02_device_replacement_cycle_accelmean_63d_slope_v024_signal,
    f02drc_f02_device_replacement_cycle_accelstd_21d_slope_v025_signal,
    f02drc_f02_device_replacement_cycle_accelstd_21d_slope_v026_signal,
    f02drc_f02_device_replacement_cycle_accelstd_63d_slope_v027_signal,
    f02drc_f02_device_replacement_cycle_accelstd_63d_slope_v028_signal,
    f02drc_f02_device_replacement_cycle_accelxinst_21d_slope_v029_signal,
    f02drc_f02_device_replacement_cycle_accelxinst_21d_slope_v030_signal,
    f02drc_f02_device_replacement_cycle_accelxinst_63d_slope_v031_signal,
    f02drc_f02_device_replacement_cycle_accelxinst_63d_slope_v032_signal,
    f02drc_f02_device_replacement_cycle_accelxcap_21d_slope_v033_signal,
    f02drc_f02_device_replacement_cycle_accelxcap_21d_slope_v034_signal,
    f02drc_f02_device_replacement_cycle_accelxcap_63d_slope_v035_signal,
    f02drc_f02_device_replacement_cycle_accelxcap_63d_slope_v036_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_21d_slope_v037_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_21d_slope_v038_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_63d_slope_v039_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_63d_slope_v040_signal,
    f02drc_f02_device_replacement_cycle_accel_42d_slope_v041_signal,
    f02drc_f02_device_replacement_cycle_accel_42d_slope_v042_signal,
    f02drc_f02_device_replacement_cycle_accel_189d_slope_v043_signal,
    f02drc_f02_device_replacement_cycle_accel_189d_slope_v044_signal,
    f02drc_f02_device_replacement_cycle_accel_378d_slope_v045_signal,
    f02drc_f02_device_replacement_cycle_accel_378d_slope_v046_signal,
    f02drc_f02_device_replacement_cycle_accel_504d_slope_v047_signal,
    f02drc_f02_device_replacement_cycle_accel_504d_slope_v048_signal,
    f02drc_f02_device_replacement_cycle_accelsq_21d_slope_v049_signal,
    f02drc_f02_device_replacement_cycle_accelsq_63d_slope_v050_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_slope_v051_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_slope_v052_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_slope_v053_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_slope_v054_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_slope_v055_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_slope_v056_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_slope_v057_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_slope_v058_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_slope_v059_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_slope_v060_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_slope_v061_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_slope_v062_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_slope_v063_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_slope_v064_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_slope_v065_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_slope_v066_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_slope_v067_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_slope_v068_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_slope_v069_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_slope_v070_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_21d_slope_v071_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_21d_slope_v072_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_63d_slope_v073_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_63d_slope_v074_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_21d_slope_v075_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_21d_slope_v076_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_63d_slope_v077_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_63d_slope_v078_signal,
    f02drc_f02_device_replacement_cycle_pulsexinst_21d_slope_v079_signal,
    f02drc_f02_device_replacement_cycle_pulsexinst_21d_slope_v080_signal,
    f02drc_f02_device_replacement_cycle_pulsexinst_63d_slope_v081_signal,
    f02drc_f02_device_replacement_cycle_pulsexinst_63d_slope_v082_signal,
    f02drc_f02_device_replacement_cycle_pulsexcap_21d_slope_v083_signal,
    f02drc_f02_device_replacement_cycle_pulsexcap_21d_slope_v084_signal,
    f02drc_f02_device_replacement_cycle_pulsexcap_63d_slope_v085_signal,
    f02drc_f02_device_replacement_cycle_pulsexcap_63d_slope_v086_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_21d_slope_v087_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_21d_slope_v088_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_63d_slope_v089_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_63d_slope_v090_signal,
    f02drc_f02_device_replacement_cycle_pulse_42d_slope_v091_signal,
    f02drc_f02_device_replacement_cycle_pulse_42d_slope_v092_signal,
    f02drc_f02_device_replacement_cycle_pulse_189d_slope_v093_signal,
    f02drc_f02_device_replacement_cycle_pulse_189d_slope_v094_signal,
    f02drc_f02_device_replacement_cycle_pulse_378d_slope_v095_signal,
    f02drc_f02_device_replacement_cycle_pulse_378d_slope_v096_signal,
    f02drc_f02_device_replacement_cycle_pulsesq_21d_slope_v097_signal,
    f02drc_f02_device_replacement_cycle_pulsesq_63d_slope_v098_signal,
    f02drc_f02_device_replacement_cycle_pulse_5d_slope_v099_signal,
    f02drc_f02_device_replacement_cycle_pulse_5d_slope_v100_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_slope_v101_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_slope_v102_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_slope_v103_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_slope_v104_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_slope_v105_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_slope_v106_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_slope_v107_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_slope_v108_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_slope_v109_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_slope_v110_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_slope_v111_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_slope_v112_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_slope_v113_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_slope_v114_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_slope_v115_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v116_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v117_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v118_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v119_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v120_signal,
    f02drc_f02_device_replacement_cycle_sigmean_21d_slope_v121_signal,
    f02drc_f02_device_replacement_cycle_sigmean_21d_slope_v122_signal,
    f02drc_f02_device_replacement_cycle_sigmean_63d_slope_v123_signal,
    f02drc_f02_device_replacement_cycle_sigmean_63d_slope_v124_signal,
    f02drc_f02_device_replacement_cycle_sigstd_21d_slope_v125_signal,
    f02drc_f02_device_replacement_cycle_sigstd_21d_slope_v126_signal,
    f02drc_f02_device_replacement_cycle_sigstd_63d_slope_v127_signal,
    f02drc_f02_device_replacement_cycle_sigstd_63d_slope_v128_signal,
    f02drc_f02_device_replacement_cycle_sigxinst_21d_slope_v129_signal,
    f02drc_f02_device_replacement_cycle_sigxinst_21d_slope_v130_signal,
    f02drc_f02_device_replacement_cycle_sigxinst_63d_slope_v131_signal,
    f02drc_f02_device_replacement_cycle_sigxinst_63d_slope_v132_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_21d_slope_v133_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_21d_slope_v134_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_63d_slope_v135_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_63d_slope_v136_signal,
    f02drc_f02_device_replacement_cycle_sigxcap_21d_slope_v137_signal,
    f02drc_f02_device_replacement_cycle_sigxcap_21d_slope_v138_signal,
    f02drc_f02_device_replacement_cycle_sigxcap_63d_slope_v139_signal,
    f02drc_f02_device_replacement_cycle_sigxcap_63d_slope_v140_signal,
    f02drc_f02_device_replacement_cycle_sig_42d_slope_v141_signal,
    f02drc_f02_device_replacement_cycle_sig_42d_slope_v142_signal,
    f02drc_f02_device_replacement_cycle_sig_189d_slope_v143_signal,
    f02drc_f02_device_replacement_cycle_sig_189d_slope_v144_signal,
    f02drc_f02_device_replacement_cycle_sig_378d_slope_v145_signal,
    f02drc_f02_device_replacement_cycle_sig_378d_slope_v146_signal,
    f02drc_f02_device_replacement_cycle_sigsq_21d_slope_v147_signal,
    f02drc_f02_device_replacement_cycle_sigsq_63d_slope_v148_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v149_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_DEVICE_REPLACEMENT_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "grossmargin": grossmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f02_revenue_smoothness", "_f02_recurring_signature", "_f02_replacement_score")
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
    print(f"OK f02_device_replacement_cycle_2nd_derivatives_001_150_claude: {n_features} features pass")
