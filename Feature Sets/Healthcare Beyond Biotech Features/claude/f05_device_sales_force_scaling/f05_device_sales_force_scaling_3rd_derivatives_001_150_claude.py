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
def _f05_sga_to_revenue(sgna, revenue, w):
    ratio = sgna / revenue.replace(0, np.nan).abs()
    base = ratio.rolling(w * 4, min_periods=max(1, w)).mean()
    return (ratio - base) / base.replace(0, np.nan).abs()


def _f05_sga_growth_gap(sgna, revenue, w):
    s_g = sgna.pct_change(periods=w)
    r_g = revenue.pct_change(periods=w)
    return s_g - r_g


def _f05_sga_leverage_score(sgna, revenue, w):
    s_g = sgna.pct_change(periods=w)
    r_g = revenue.pct_change(periods=w)
    return r_g - 0.5 * s_g


# Build features programmatically to ensure uniqueness.
# Layout (150 features): 50 accel-slopes, 50 pulse-slopes, 50 sig-slopes.
# Each slot varies (base_window, slope_window, scaling) so bodies are unique.

# ---- accel slopes (v001-v050) ----

def f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v001_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v002_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v003_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v004_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v005_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v006_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v007_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v008_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v009_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v010_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v011_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v012_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v013_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v014_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v015_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v016_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v017_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v018_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v019_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v020_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelmean_21d_jerk_v021_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_growth_gap(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelmean_21d_jerk_v022_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_growth_gap(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelmean_63d_jerk_v023_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_growth_gap(sgna, revenue, 63), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelmean_63d_jerk_v024_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_growth_gap(sgna, revenue, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelstd_21d_jerk_v025_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_growth_gap(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelstd_21d_jerk_v026_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_growth_gap(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelstd_63d_jerk_v027_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_growth_gap(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelstd_63d_jerk_v028_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_growth_gap(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxinst_21d_jerk_v029_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxinst_21d_jerk_v030_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxinst_63d_jerk_v031_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxinst_63d_jerk_v032_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxcap_21d_jerk_v033_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxcap_21d_jerk_v034_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxcap_63d_jerk_v035_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxcap_63d_jerk_v036_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxrev_21d_jerk_v037_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxrev_21d_jerk_v038_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxrev_63d_jerk_v039_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelxrev_63d_jerk_v040_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_42d_jerk_v041_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_42d_jerk_v042_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_189d_jerk_v043_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_189d_jerk_v044_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_378d_jerk_v045_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_378d_jerk_v046_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_504d_jerk_v047_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accel_504d_jerk_v048_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelsq_21d_jerk_v049_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 21)
    base = a * a.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_accelsq_63d_jerk_v050_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 63)
    base = a * a.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- pulse slopes (v051-v100) ----

def f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v051_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v052_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v053_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v054_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v055_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v056_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v057_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v058_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v059_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v060_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v061_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v062_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v063_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v064_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v065_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v066_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v067_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v068_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v069_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v070_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsemean_21d_jerk_v071_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_to_revenue(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsemean_21d_jerk_v072_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_to_revenue(sgna, revenue, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsemean_63d_jerk_v073_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_to_revenue(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsemean_63d_jerk_v074_signal(sgna, revenue, closeadj):
    base = _mean(_f05_sga_to_revenue(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsestd_21d_jerk_v075_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_to_revenue(sgna, revenue, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsestd_21d_jerk_v076_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_to_revenue(sgna, revenue, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsestd_63d_jerk_v077_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_to_revenue(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsestd_63d_jerk_v078_signal(sgna, revenue, closeadj):
    base = _std(_f05_sga_to_revenue(sgna, revenue, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexinst_21d_jerk_v079_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexinst_21d_jerk_v080_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexinst_63d_jerk_v081_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexinst_63d_jerk_v082_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexcap_21d_jerk_v083_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexcap_21d_jerk_v084_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexcap_63d_jerk_v085_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexcap_63d_jerk_v086_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexrev_21d_jerk_v087_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexrev_21d_jerk_v088_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexrev_63d_jerk_v089_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsexrev_63d_jerk_v090_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_42d_jerk_v091_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_42d_jerk_v092_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_189d_jerk_v093_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_189d_jerk_v094_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_378d_jerk_v095_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_378d_jerk_v096_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsesq_21d_jerk_v097_signal(sgna, revenue, closeadj):
    p = _f05_sga_to_revenue(sgna, revenue, 21)
    base = p * p.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulsesq_63d_jerk_v098_signal(sgna, revenue, closeadj):
    p = _f05_sga_to_revenue(sgna, revenue, 63)
    base = p * p.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_5d_jerk_v099_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_pulse_5d_jerk_v100_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# ---- sig slopes (v101-v150) ----

def f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v101_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v102_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v103_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v104_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v105_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * closeadj
    result = _jerk_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v106_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v107_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v108_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v109_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v110_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v111_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v112_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v113_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v114_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v115_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 126) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v116_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v117_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v118_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v119_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v120_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigmean_21d_jerk_v121_signal(sgna, closeadj):
    base = _mean(_f05_sga_leverage_score(sgna, sgna, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigmean_21d_jerk_v122_signal(sgna, closeadj):
    base = _mean(_f05_sga_leverage_score(sgna, sgna, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigmean_63d_jerk_v123_signal(sgna, closeadj):
    base = _mean(_f05_sga_leverage_score(sgna, sgna, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigmean_63d_jerk_v124_signal(sgna, closeadj):
    base = _mean(_f05_sga_leverage_score(sgna, sgna, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigstd_21d_jerk_v125_signal(sgna, closeadj):
    base = _std(_f05_sga_leverage_score(sgna, sgna, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigstd_21d_jerk_v126_signal(sgna, closeadj):
    base = _std(_f05_sga_leverage_score(sgna, sgna, 21), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigstd_63d_jerk_v127_signal(sgna, closeadj):
    base = _std(_f05_sga_leverage_score(sgna, sgna, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigstd_63d_jerk_v128_signal(sgna, closeadj):
    base = _std(_f05_sga_leverage_score(sgna, sgna, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxinst_21d_jerk_v129_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxinst_21d_jerk_v130_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxinst_63d_jerk_v131_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxinst_63d_jerk_v132_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * opex / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxrev_21d_jerk_v133_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxrev_21d_jerk_v134_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxrev_63d_jerk_v135_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxrev_63d_jerk_v136_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * (sgna * 10.0) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxcap_21d_jerk_v137_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxcap_21d_jerk_v138_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxcap_63d_jerk_v139_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigxcap_63d_jerk_v140_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63) * sgna / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_42d_jerk_v141_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_42d_jerk_v142_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_189d_jerk_v143_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_189d_jerk_v144_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_378d_jerk_v145_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_378d_jerk_v146_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigsq_21d_jerk_v147_signal(sgna, closeadj):
    s = _f05_sga_leverage_score(sgna, sgna, 21)
    base = s * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sigsq_63d_jerk_v148_signal(sgna, closeadj):
    s = _f05_sga_leverage_score(sgna, sgna, 63)
    base = s * s.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v149_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v150_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 252) * closeadj
    result = _jerk_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v001_signal,
    f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v002_signal,
    f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v003_signal,
    f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v004_signal,
    f05dsf_f05_device_sales_force_scaling_accel_21d_jerk_v005_signal,
    f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v006_signal,
    f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v007_signal,
    f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v008_signal,
    f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v009_signal,
    f05dsf_f05_device_sales_force_scaling_accel_63d_jerk_v010_signal,
    f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v011_signal,
    f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v012_signal,
    f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v013_signal,
    f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v014_signal,
    f05dsf_f05_device_sales_force_scaling_accel_126d_jerk_v015_signal,
    f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v016_signal,
    f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v017_signal,
    f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v018_signal,
    f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v019_signal,
    f05dsf_f05_device_sales_force_scaling_accel_252d_jerk_v020_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_21d_jerk_v021_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_21d_jerk_v022_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_63d_jerk_v023_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_63d_jerk_v024_signal,
    f05dsf_f05_device_sales_force_scaling_accelstd_21d_jerk_v025_signal,
    f05dsf_f05_device_sales_force_scaling_accelstd_21d_jerk_v026_signal,
    f05dsf_f05_device_sales_force_scaling_accelstd_63d_jerk_v027_signal,
    f05dsf_f05_device_sales_force_scaling_accelstd_63d_jerk_v028_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinst_21d_jerk_v029_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinst_21d_jerk_v030_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinst_63d_jerk_v031_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinst_63d_jerk_v032_signal,
    f05dsf_f05_device_sales_force_scaling_accelxcap_21d_jerk_v033_signal,
    f05dsf_f05_device_sales_force_scaling_accelxcap_21d_jerk_v034_signal,
    f05dsf_f05_device_sales_force_scaling_accelxcap_63d_jerk_v035_signal,
    f05dsf_f05_device_sales_force_scaling_accelxcap_63d_jerk_v036_signal,
    f05dsf_f05_device_sales_force_scaling_accelxrev_21d_jerk_v037_signal,
    f05dsf_f05_device_sales_force_scaling_accelxrev_21d_jerk_v038_signal,
    f05dsf_f05_device_sales_force_scaling_accelxrev_63d_jerk_v039_signal,
    f05dsf_f05_device_sales_force_scaling_accelxrev_63d_jerk_v040_signal,
    f05dsf_f05_device_sales_force_scaling_accel_42d_jerk_v041_signal,
    f05dsf_f05_device_sales_force_scaling_accel_42d_jerk_v042_signal,
    f05dsf_f05_device_sales_force_scaling_accel_189d_jerk_v043_signal,
    f05dsf_f05_device_sales_force_scaling_accel_189d_jerk_v044_signal,
    f05dsf_f05_device_sales_force_scaling_accel_378d_jerk_v045_signal,
    f05dsf_f05_device_sales_force_scaling_accel_378d_jerk_v046_signal,
    f05dsf_f05_device_sales_force_scaling_accel_504d_jerk_v047_signal,
    f05dsf_f05_device_sales_force_scaling_accel_504d_jerk_v048_signal,
    f05dsf_f05_device_sales_force_scaling_accelsq_21d_jerk_v049_signal,
    f05dsf_f05_device_sales_force_scaling_accelsq_63d_jerk_v050_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v051_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v052_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v053_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v054_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_21d_jerk_v055_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v056_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v057_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v058_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v059_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_63d_jerk_v060_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v061_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v062_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v063_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v064_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_126d_jerk_v065_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v066_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v067_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v068_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v069_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_252d_jerk_v070_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_21d_jerk_v071_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_21d_jerk_v072_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_63d_jerk_v073_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_63d_jerk_v074_signal,
    f05dsf_f05_device_sales_force_scaling_pulsestd_21d_jerk_v075_signal,
    f05dsf_f05_device_sales_force_scaling_pulsestd_21d_jerk_v076_signal,
    f05dsf_f05_device_sales_force_scaling_pulsestd_63d_jerk_v077_signal,
    f05dsf_f05_device_sales_force_scaling_pulsestd_63d_jerk_v078_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinst_21d_jerk_v079_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinst_21d_jerk_v080_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinst_63d_jerk_v081_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinst_63d_jerk_v082_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexcap_21d_jerk_v083_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexcap_21d_jerk_v084_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexcap_63d_jerk_v085_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexcap_63d_jerk_v086_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexrev_21d_jerk_v087_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexrev_21d_jerk_v088_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexrev_63d_jerk_v089_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexrev_63d_jerk_v090_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_42d_jerk_v091_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_42d_jerk_v092_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_189d_jerk_v093_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_189d_jerk_v094_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_378d_jerk_v095_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_378d_jerk_v096_signal,
    f05dsf_f05_device_sales_force_scaling_pulsesq_21d_jerk_v097_signal,
    f05dsf_f05_device_sales_force_scaling_pulsesq_63d_jerk_v098_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_5d_jerk_v099_signal,
    f05dsf_f05_device_sales_force_scaling_pulse_5d_jerk_v100_signal,
    f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v101_signal,
    f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v102_signal,
    f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v103_signal,
    f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v104_signal,
    f05dsf_f05_device_sales_force_scaling_sig_21d_jerk_v105_signal,
    f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v106_signal,
    f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v107_signal,
    f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v108_signal,
    f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v109_signal,
    f05dsf_f05_device_sales_force_scaling_sig_63d_jerk_v110_signal,
    f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v111_signal,
    f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v112_signal,
    f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v113_signal,
    f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v114_signal,
    f05dsf_f05_device_sales_force_scaling_sig_126d_jerk_v115_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v116_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v117_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v118_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v119_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v120_signal,
    f05dsf_f05_device_sales_force_scaling_sigmean_21d_jerk_v121_signal,
    f05dsf_f05_device_sales_force_scaling_sigmean_21d_jerk_v122_signal,
    f05dsf_f05_device_sales_force_scaling_sigmean_63d_jerk_v123_signal,
    f05dsf_f05_device_sales_force_scaling_sigmean_63d_jerk_v124_signal,
    f05dsf_f05_device_sales_force_scaling_sigstd_21d_jerk_v125_signal,
    f05dsf_f05_device_sales_force_scaling_sigstd_21d_jerk_v126_signal,
    f05dsf_f05_device_sales_force_scaling_sigstd_63d_jerk_v127_signal,
    f05dsf_f05_device_sales_force_scaling_sigstd_63d_jerk_v128_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinst_21d_jerk_v129_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinst_21d_jerk_v130_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinst_63d_jerk_v131_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinst_63d_jerk_v132_signal,
    f05dsf_f05_device_sales_force_scaling_sigxrev_21d_jerk_v133_signal,
    f05dsf_f05_device_sales_force_scaling_sigxrev_21d_jerk_v134_signal,
    f05dsf_f05_device_sales_force_scaling_sigxrev_63d_jerk_v135_signal,
    f05dsf_f05_device_sales_force_scaling_sigxrev_63d_jerk_v136_signal,
    f05dsf_f05_device_sales_force_scaling_sigxcap_21d_jerk_v137_signal,
    f05dsf_f05_device_sales_force_scaling_sigxcap_21d_jerk_v138_signal,
    f05dsf_f05_device_sales_force_scaling_sigxcap_63d_jerk_v139_signal,
    f05dsf_f05_device_sales_force_scaling_sigxcap_63d_jerk_v140_signal,
    f05dsf_f05_device_sales_force_scaling_sig_42d_jerk_v141_signal,
    f05dsf_f05_device_sales_force_scaling_sig_42d_jerk_v142_signal,
    f05dsf_f05_device_sales_force_scaling_sig_189d_jerk_v143_signal,
    f05dsf_f05_device_sales_force_scaling_sig_189d_jerk_v144_signal,
    f05dsf_f05_device_sales_force_scaling_sig_378d_jerk_v145_signal,
    f05dsf_f05_device_sales_force_scaling_sig_378d_jerk_v146_signal,
    f05dsf_f05_device_sales_force_scaling_sigsq_21d_jerk_v147_signal,
    f05dsf_f05_device_sales_force_scaling_sigsq_63d_jerk_v148_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v149_signal,
    f05dsf_f05_device_sales_force_scaling_sig_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_DEVICE_SALES_FORCE_SCALING_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    sgna = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")

    cols = {"closeadj": closeadj, "sgna": sgna, "revenue": revenue, "opex": opex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f05_sga_growth_gap", "_f05_sga_to_revenue", "_f05_sga_leverage_score")
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
    print(f"OK f05_device_sales_force_scaling_3rd_derivatives_001_150_claude: {n_features} features pass")
