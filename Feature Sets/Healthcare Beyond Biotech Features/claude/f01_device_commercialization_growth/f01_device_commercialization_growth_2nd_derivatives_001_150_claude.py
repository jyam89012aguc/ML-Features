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
def _f01_revenue_accel(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f01_launch_pulse(revenue, w):
    base = revenue.rolling(w * 4, min_periods=max(1, w)).mean()
    return (revenue - base) / base.replace(0, np.nan).abs()


def _f01_commercialization_signature(revenue, capex, w):
    rev_g = revenue.pct_change(periods=w)
    cap_g = capex.pct_change(periods=w)
    return rev_g - 0.5 * cap_g


# Build features programmatically to ensure uniqueness.
# Layout (150 features): 50 accel-slopes, 50 pulse-slopes, 50 sig-slopes.
# Each slot varies (base_window, slope_window, scaling) so bodies are unique.

# ---- accel slopes (v001-v050) ----

def f01dcg_f01_device_commercialization_growth_accel_21d_slope_v001_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_21d_slope_v002_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_21d_slope_v003_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_21d_slope_v004_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_21d_slope_v005_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_63d_slope_v006_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_63d_slope_v007_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_63d_slope_v008_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_63d_slope_v009_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_63d_slope_v010_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_126d_slope_v011_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_126d_slope_v012_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_126d_slope_v013_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_126d_slope_v014_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_126d_slope_v015_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_252d_slope_v016_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_252d_slope_v017_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_252d_slope_v018_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_252d_slope_v019_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_252d_slope_v020_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelmean_21d_slope_v021_signal(revenue, closeadj):
    base = _mean(_f01_revenue_accel(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelmean_21d_slope_v022_signal(revenue, closeadj):
    base = _mean(_f01_revenue_accel(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelmean_63d_slope_v023_signal(revenue, closeadj):
    base = _mean(_f01_revenue_accel(revenue, 63), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelmean_63d_slope_v024_signal(revenue, closeadj):
    base = _mean(_f01_revenue_accel(revenue, 63), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelstd_21d_slope_v025_signal(revenue, closeadj):
    base = _std(_f01_revenue_accel(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelstd_21d_slope_v026_signal(revenue, closeadj):
    base = _std(_f01_revenue_accel(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelstd_63d_slope_v027_signal(revenue, closeadj):
    base = _std(_f01_revenue_accel(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelstd_63d_slope_v028_signal(revenue, closeadj):
    base = _std(_f01_revenue_accel(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxinst_21d_slope_v029_signal(revenue, ppnenet, closeadj):
    base = _f01_revenue_accel(revenue, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxinst_21d_slope_v030_signal(revenue, ppnenet, closeadj):
    base = _f01_revenue_accel(revenue, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxinst_63d_slope_v031_signal(revenue, ppnenet, closeadj):
    base = _f01_revenue_accel(revenue, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxinst_63d_slope_v032_signal(revenue, ppnenet, closeadj):
    base = _f01_revenue_accel(revenue, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxcap_21d_slope_v033_signal(revenue, capex, closeadj):
    base = _f01_revenue_accel(revenue, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxcap_21d_slope_v034_signal(revenue, capex, closeadj):
    base = _f01_revenue_accel(revenue, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxcap_63d_slope_v035_signal(revenue, capex, closeadj):
    base = _f01_revenue_accel(revenue, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxcap_63d_slope_v036_signal(revenue, capex, closeadj):
    base = _f01_revenue_accel(revenue, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxrev_21d_slope_v037_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxrev_21d_slope_v038_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxrev_63d_slope_v039_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelxrev_63d_slope_v040_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_42d_slope_v041_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_42d_slope_v042_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_189d_slope_v043_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_189d_slope_v044_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_378d_slope_v045_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_378d_slope_v046_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_504d_slope_v047_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accel_504d_slope_v048_signal(revenue, closeadj):
    base = _f01_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelsq_21d_slope_v049_signal(revenue, closeadj):
    a = _f01_revenue_accel(revenue, 21)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_accelsq_63d_slope_v050_signal(revenue, closeadj):
    a = _f01_revenue_accel(revenue, 63)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- pulse slopes (v051-v100) ----

def f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v051_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v052_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v053_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v054_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v055_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v056_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v057_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v058_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v059_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v060_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v061_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v062_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v063_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v064_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v065_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v066_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v067_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v068_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v069_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v070_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsemean_21d_slope_v071_signal(revenue, closeadj):
    base = _mean(_f01_launch_pulse(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsemean_21d_slope_v072_signal(revenue, closeadj):
    base = _mean(_f01_launch_pulse(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsemean_63d_slope_v073_signal(revenue, closeadj):
    base = _mean(_f01_launch_pulse(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsemean_63d_slope_v074_signal(revenue, closeadj):
    base = _mean(_f01_launch_pulse(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsestd_21d_slope_v075_signal(revenue, closeadj):
    base = _std(_f01_launch_pulse(revenue, 21), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsestd_21d_slope_v076_signal(revenue, closeadj):
    base = _std(_f01_launch_pulse(revenue, 21), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsestd_63d_slope_v077_signal(revenue, closeadj):
    base = _std(_f01_launch_pulse(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsestd_63d_slope_v078_signal(revenue, closeadj):
    base = _std(_f01_launch_pulse(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexinst_21d_slope_v079_signal(revenue, ppnenet, closeadj):
    base = _f01_launch_pulse(revenue, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexinst_21d_slope_v080_signal(revenue, ppnenet, closeadj):
    base = _f01_launch_pulse(revenue, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexinst_63d_slope_v081_signal(revenue, ppnenet, closeadj):
    base = _f01_launch_pulse(revenue, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexinst_63d_slope_v082_signal(revenue, ppnenet, closeadj):
    base = _f01_launch_pulse(revenue, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexcap_21d_slope_v083_signal(revenue, capex, closeadj):
    base = _f01_launch_pulse(revenue, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexcap_21d_slope_v084_signal(revenue, capex, closeadj):
    base = _f01_launch_pulse(revenue, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexcap_63d_slope_v085_signal(revenue, capex, closeadj):
    base = _f01_launch_pulse(revenue, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexcap_63d_slope_v086_signal(revenue, capex, closeadj):
    base = _f01_launch_pulse(revenue, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexrev_21d_slope_v087_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexrev_21d_slope_v088_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexrev_63d_slope_v089_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsexrev_63d_slope_v090_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_42d_slope_v091_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_42d_slope_v092_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_189d_slope_v093_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_189d_slope_v094_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_378d_slope_v095_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_378d_slope_v096_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsesq_21d_slope_v097_signal(revenue, closeadj):
    p = _f01_launch_pulse(revenue, 21)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulsesq_63d_slope_v098_signal(revenue, closeadj):
    p = _f01_launch_pulse(revenue, 63)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_5d_slope_v099_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_pulse_5d_slope_v100_signal(revenue, closeadj):
    base = _f01_launch_pulse(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- sig slopes (v101-v150) ----

def f01dcg_f01_device_commercialization_growth_sig_21d_slope_v101_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_21d_slope_v102_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_21d_slope_v103_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_21d_slope_v104_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_21d_slope_v105_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_63d_slope_v106_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_63d_slope_v107_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_63d_slope_v108_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_63d_slope_v109_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_63d_slope_v110_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_126d_slope_v111_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_126d_slope_v112_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_126d_slope_v113_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_126d_slope_v114_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_126d_slope_v115_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v116_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v117_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v118_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v119_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v120_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigmean_21d_slope_v121_signal(revenue, capex, closeadj):
    base = _mean(_f01_commercialization_signature(revenue, capex, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigmean_21d_slope_v122_signal(revenue, capex, closeadj):
    base = _mean(_f01_commercialization_signature(revenue, capex, 21), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigmean_63d_slope_v123_signal(revenue, capex, closeadj):
    base = _mean(_f01_commercialization_signature(revenue, capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigmean_63d_slope_v124_signal(revenue, capex, closeadj):
    base = _mean(_f01_commercialization_signature(revenue, capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigstd_21d_slope_v125_signal(revenue, capex, closeadj):
    base = _std(_f01_commercialization_signature(revenue, capex, 21), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigstd_21d_slope_v126_signal(revenue, capex, closeadj):
    base = _std(_f01_commercialization_signature(revenue, capex, 21), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigstd_63d_slope_v127_signal(revenue, capex, closeadj):
    base = _std(_f01_commercialization_signature(revenue, capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigstd_63d_slope_v128_signal(revenue, capex, closeadj):
    base = _std(_f01_commercialization_signature(revenue, capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxinst_21d_slope_v129_signal(revenue, capex, ppnenet, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxinst_21d_slope_v130_signal(revenue, capex, ppnenet, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxinst_63d_slope_v131_signal(revenue, capex, ppnenet, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxinst_63d_slope_v132_signal(revenue, capex, ppnenet, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * ppnenet / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxrev_21d_slope_v133_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxrev_21d_slope_v134_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxrev_63d_slope_v135_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxrev_63d_slope_v136_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * revenue / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxcap_21d_slope_v137_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxcap_21d_slope_v138_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 21) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxcap_63d_slope_v139_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigxcap_63d_slope_v140_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 63) * capex / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_42d_slope_v141_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_42d_slope_v142_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_189d_slope_v143_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_189d_slope_v144_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 189) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_378d_slope_v145_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_378d_slope_v146_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigsq_21d_slope_v147_signal(revenue, capex, closeadj):
    s = _f01_commercialization_signature(revenue, capex, 21)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sigsq_63d_slope_v148_signal(revenue, capex, closeadj):
    s = _f01_commercialization_signature(revenue, capex, 63)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v149_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01dcg_f01_device_commercialization_growth_sig_252d_slope_v150_signal(revenue, capex, closeadj):
    base = _f01_commercialization_signature(revenue, capex, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01dcg_f01_device_commercialization_growth_accel_21d_slope_v001_signal,
    f01dcg_f01_device_commercialization_growth_accel_21d_slope_v002_signal,
    f01dcg_f01_device_commercialization_growth_accel_21d_slope_v003_signal,
    f01dcg_f01_device_commercialization_growth_accel_21d_slope_v004_signal,
    f01dcg_f01_device_commercialization_growth_accel_21d_slope_v005_signal,
    f01dcg_f01_device_commercialization_growth_accel_63d_slope_v006_signal,
    f01dcg_f01_device_commercialization_growth_accel_63d_slope_v007_signal,
    f01dcg_f01_device_commercialization_growth_accel_63d_slope_v008_signal,
    f01dcg_f01_device_commercialization_growth_accel_63d_slope_v009_signal,
    f01dcg_f01_device_commercialization_growth_accel_63d_slope_v010_signal,
    f01dcg_f01_device_commercialization_growth_accel_126d_slope_v011_signal,
    f01dcg_f01_device_commercialization_growth_accel_126d_slope_v012_signal,
    f01dcg_f01_device_commercialization_growth_accel_126d_slope_v013_signal,
    f01dcg_f01_device_commercialization_growth_accel_126d_slope_v014_signal,
    f01dcg_f01_device_commercialization_growth_accel_126d_slope_v015_signal,
    f01dcg_f01_device_commercialization_growth_accel_252d_slope_v016_signal,
    f01dcg_f01_device_commercialization_growth_accel_252d_slope_v017_signal,
    f01dcg_f01_device_commercialization_growth_accel_252d_slope_v018_signal,
    f01dcg_f01_device_commercialization_growth_accel_252d_slope_v019_signal,
    f01dcg_f01_device_commercialization_growth_accel_252d_slope_v020_signal,
    f01dcg_f01_device_commercialization_growth_accelmean_21d_slope_v021_signal,
    f01dcg_f01_device_commercialization_growth_accelmean_21d_slope_v022_signal,
    f01dcg_f01_device_commercialization_growth_accelmean_63d_slope_v023_signal,
    f01dcg_f01_device_commercialization_growth_accelmean_63d_slope_v024_signal,
    f01dcg_f01_device_commercialization_growth_accelstd_21d_slope_v025_signal,
    f01dcg_f01_device_commercialization_growth_accelstd_21d_slope_v026_signal,
    f01dcg_f01_device_commercialization_growth_accelstd_63d_slope_v027_signal,
    f01dcg_f01_device_commercialization_growth_accelstd_63d_slope_v028_signal,
    f01dcg_f01_device_commercialization_growth_accelxinst_21d_slope_v029_signal,
    f01dcg_f01_device_commercialization_growth_accelxinst_21d_slope_v030_signal,
    f01dcg_f01_device_commercialization_growth_accelxinst_63d_slope_v031_signal,
    f01dcg_f01_device_commercialization_growth_accelxinst_63d_slope_v032_signal,
    f01dcg_f01_device_commercialization_growth_accelxcap_21d_slope_v033_signal,
    f01dcg_f01_device_commercialization_growth_accelxcap_21d_slope_v034_signal,
    f01dcg_f01_device_commercialization_growth_accelxcap_63d_slope_v035_signal,
    f01dcg_f01_device_commercialization_growth_accelxcap_63d_slope_v036_signal,
    f01dcg_f01_device_commercialization_growth_accelxrev_21d_slope_v037_signal,
    f01dcg_f01_device_commercialization_growth_accelxrev_21d_slope_v038_signal,
    f01dcg_f01_device_commercialization_growth_accelxrev_63d_slope_v039_signal,
    f01dcg_f01_device_commercialization_growth_accelxrev_63d_slope_v040_signal,
    f01dcg_f01_device_commercialization_growth_accel_42d_slope_v041_signal,
    f01dcg_f01_device_commercialization_growth_accel_42d_slope_v042_signal,
    f01dcg_f01_device_commercialization_growth_accel_189d_slope_v043_signal,
    f01dcg_f01_device_commercialization_growth_accel_189d_slope_v044_signal,
    f01dcg_f01_device_commercialization_growth_accel_378d_slope_v045_signal,
    f01dcg_f01_device_commercialization_growth_accel_378d_slope_v046_signal,
    f01dcg_f01_device_commercialization_growth_accel_504d_slope_v047_signal,
    f01dcg_f01_device_commercialization_growth_accel_504d_slope_v048_signal,
    f01dcg_f01_device_commercialization_growth_accelsq_21d_slope_v049_signal,
    f01dcg_f01_device_commercialization_growth_accelsq_63d_slope_v050_signal,
    f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v051_signal,
    f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v052_signal,
    f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v053_signal,
    f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v054_signal,
    f01dcg_f01_device_commercialization_growth_pulse_21d_slope_v055_signal,
    f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v056_signal,
    f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v057_signal,
    f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v058_signal,
    f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v059_signal,
    f01dcg_f01_device_commercialization_growth_pulse_63d_slope_v060_signal,
    f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v061_signal,
    f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v062_signal,
    f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v063_signal,
    f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v064_signal,
    f01dcg_f01_device_commercialization_growth_pulse_126d_slope_v065_signal,
    f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v066_signal,
    f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v067_signal,
    f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v068_signal,
    f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v069_signal,
    f01dcg_f01_device_commercialization_growth_pulse_252d_slope_v070_signal,
    f01dcg_f01_device_commercialization_growth_pulsemean_21d_slope_v071_signal,
    f01dcg_f01_device_commercialization_growth_pulsemean_21d_slope_v072_signal,
    f01dcg_f01_device_commercialization_growth_pulsemean_63d_slope_v073_signal,
    f01dcg_f01_device_commercialization_growth_pulsemean_63d_slope_v074_signal,
    f01dcg_f01_device_commercialization_growth_pulsestd_21d_slope_v075_signal,
    f01dcg_f01_device_commercialization_growth_pulsestd_21d_slope_v076_signal,
    f01dcg_f01_device_commercialization_growth_pulsestd_63d_slope_v077_signal,
    f01dcg_f01_device_commercialization_growth_pulsestd_63d_slope_v078_signal,
    f01dcg_f01_device_commercialization_growth_pulsexinst_21d_slope_v079_signal,
    f01dcg_f01_device_commercialization_growth_pulsexinst_21d_slope_v080_signal,
    f01dcg_f01_device_commercialization_growth_pulsexinst_63d_slope_v081_signal,
    f01dcg_f01_device_commercialization_growth_pulsexinst_63d_slope_v082_signal,
    f01dcg_f01_device_commercialization_growth_pulsexcap_21d_slope_v083_signal,
    f01dcg_f01_device_commercialization_growth_pulsexcap_21d_slope_v084_signal,
    f01dcg_f01_device_commercialization_growth_pulsexcap_63d_slope_v085_signal,
    f01dcg_f01_device_commercialization_growth_pulsexcap_63d_slope_v086_signal,
    f01dcg_f01_device_commercialization_growth_pulsexrev_21d_slope_v087_signal,
    f01dcg_f01_device_commercialization_growth_pulsexrev_21d_slope_v088_signal,
    f01dcg_f01_device_commercialization_growth_pulsexrev_63d_slope_v089_signal,
    f01dcg_f01_device_commercialization_growth_pulsexrev_63d_slope_v090_signal,
    f01dcg_f01_device_commercialization_growth_pulse_42d_slope_v091_signal,
    f01dcg_f01_device_commercialization_growth_pulse_42d_slope_v092_signal,
    f01dcg_f01_device_commercialization_growth_pulse_189d_slope_v093_signal,
    f01dcg_f01_device_commercialization_growth_pulse_189d_slope_v094_signal,
    f01dcg_f01_device_commercialization_growth_pulse_378d_slope_v095_signal,
    f01dcg_f01_device_commercialization_growth_pulse_378d_slope_v096_signal,
    f01dcg_f01_device_commercialization_growth_pulsesq_21d_slope_v097_signal,
    f01dcg_f01_device_commercialization_growth_pulsesq_63d_slope_v098_signal,
    f01dcg_f01_device_commercialization_growth_pulse_5d_slope_v099_signal,
    f01dcg_f01_device_commercialization_growth_pulse_5d_slope_v100_signal,
    f01dcg_f01_device_commercialization_growth_sig_21d_slope_v101_signal,
    f01dcg_f01_device_commercialization_growth_sig_21d_slope_v102_signal,
    f01dcg_f01_device_commercialization_growth_sig_21d_slope_v103_signal,
    f01dcg_f01_device_commercialization_growth_sig_21d_slope_v104_signal,
    f01dcg_f01_device_commercialization_growth_sig_21d_slope_v105_signal,
    f01dcg_f01_device_commercialization_growth_sig_63d_slope_v106_signal,
    f01dcg_f01_device_commercialization_growth_sig_63d_slope_v107_signal,
    f01dcg_f01_device_commercialization_growth_sig_63d_slope_v108_signal,
    f01dcg_f01_device_commercialization_growth_sig_63d_slope_v109_signal,
    f01dcg_f01_device_commercialization_growth_sig_63d_slope_v110_signal,
    f01dcg_f01_device_commercialization_growth_sig_126d_slope_v111_signal,
    f01dcg_f01_device_commercialization_growth_sig_126d_slope_v112_signal,
    f01dcg_f01_device_commercialization_growth_sig_126d_slope_v113_signal,
    f01dcg_f01_device_commercialization_growth_sig_126d_slope_v114_signal,
    f01dcg_f01_device_commercialization_growth_sig_126d_slope_v115_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v116_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v117_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v118_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v119_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v120_signal,
    f01dcg_f01_device_commercialization_growth_sigmean_21d_slope_v121_signal,
    f01dcg_f01_device_commercialization_growth_sigmean_21d_slope_v122_signal,
    f01dcg_f01_device_commercialization_growth_sigmean_63d_slope_v123_signal,
    f01dcg_f01_device_commercialization_growth_sigmean_63d_slope_v124_signal,
    f01dcg_f01_device_commercialization_growth_sigstd_21d_slope_v125_signal,
    f01dcg_f01_device_commercialization_growth_sigstd_21d_slope_v126_signal,
    f01dcg_f01_device_commercialization_growth_sigstd_63d_slope_v127_signal,
    f01dcg_f01_device_commercialization_growth_sigstd_63d_slope_v128_signal,
    f01dcg_f01_device_commercialization_growth_sigxinst_21d_slope_v129_signal,
    f01dcg_f01_device_commercialization_growth_sigxinst_21d_slope_v130_signal,
    f01dcg_f01_device_commercialization_growth_sigxinst_63d_slope_v131_signal,
    f01dcg_f01_device_commercialization_growth_sigxinst_63d_slope_v132_signal,
    f01dcg_f01_device_commercialization_growth_sigxrev_21d_slope_v133_signal,
    f01dcg_f01_device_commercialization_growth_sigxrev_21d_slope_v134_signal,
    f01dcg_f01_device_commercialization_growth_sigxrev_63d_slope_v135_signal,
    f01dcg_f01_device_commercialization_growth_sigxrev_63d_slope_v136_signal,
    f01dcg_f01_device_commercialization_growth_sigxcap_21d_slope_v137_signal,
    f01dcg_f01_device_commercialization_growth_sigxcap_21d_slope_v138_signal,
    f01dcg_f01_device_commercialization_growth_sigxcap_63d_slope_v139_signal,
    f01dcg_f01_device_commercialization_growth_sigxcap_63d_slope_v140_signal,
    f01dcg_f01_device_commercialization_growth_sig_42d_slope_v141_signal,
    f01dcg_f01_device_commercialization_growth_sig_42d_slope_v142_signal,
    f01dcg_f01_device_commercialization_growth_sig_189d_slope_v143_signal,
    f01dcg_f01_device_commercialization_growth_sig_189d_slope_v144_signal,
    f01dcg_f01_device_commercialization_growth_sig_378d_slope_v145_signal,
    f01dcg_f01_device_commercialization_growth_sig_378d_slope_v146_signal,
    f01dcg_f01_device_commercialization_growth_sigsq_21d_slope_v147_signal,
    f01dcg_f01_device_commercialization_growth_sigsq_63d_slope_v148_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v149_signal,
    f01dcg_f01_device_commercialization_growth_sig_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_DEVICE_COMMERCIALIZATION_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex, "ppnenet": ppnenet}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f01_revenue_accel", "_f01_launch_pulse", "_f01_commercialization_signature")
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
    print(f"OK f01_device_commercialization_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
